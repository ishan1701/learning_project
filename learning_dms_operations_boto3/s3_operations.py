import logging
from datetime import date

import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

client = boto3.client("s3", region_name="eu-west-1")


def _archive_s3_data(source_bucket: str, table: str, files_prefix: str):
    target_s3 = "-".join([source_bucket, "archive"])
    s3_session = boto3.resource("s3")
    bucket = s3_session.Bucket(target_s3)
    logger.info("Starting data archive for table - {}".format(table))
    paginator = client.get_paginator("list_objects_v2")
    pages = paginator.paginate(Bucket=source_bucket, Prefix=files_prefix)
    target_s3_prefix = str(date.today())
    for page in pages:
        if page.get("Contents") is not None:
            contents = page["Contents"]
            for content in contents:
                key_to_copy = content["Key"]

                copy_source = {"Bucket": source_bucket, "Key": key_to_copy}
                bucket.copy(copy_source, "/".join([target_s3_prefix, key_to_copy]))
        else:
            logger.info("Found no files to archive")
    logger.info("Archiving completed for table -{}".format(table))


def delete_s3_data(
    bucket: str, prefix: str, schema: str, tables: list, archive_flag: bool = False
):
    """
    Purpose: Delete the s3 files
    :param archive_flag:
    :param bucket:  bucket name
    :param prefix:  DMS task name
    :param schema:  DMS schema name
    :param tables:  DMS table name
    :return: None
    """
    for table in tables:
        if schema is None:
            files_prefix = "/".join([prefix, table])
        else:
            files_prefix = "/".join([prefix, schema, table])
        if archive_flag:
            _archive_s3_data(
                source_bucket=bucket, table=table, files_prefix=files_prefix
            )
        logger.info("Flushing s3 data for table {}".format(table))
        paginator = client.get_paginator("list_objects_v2")
        pages = paginator.paginate(Bucket=bucket, Prefix=files_prefix)
        files_to_delete = dict(Objects=[])
        for page in pages:
            if page.get("Contents") is not None:
                contents = page["Contents"]
                for content in contents:
                    files_to_delete["Objects"].append({"Key": content["Key"]})
                # flush the files once threshold is reached
                if len(files_to_delete["Objects"]) >= 1000:
                    client.delete_objects(Bucket=bucket, Delete=files_to_delete)
                    files_to_delete = dict(Objects=[])

                # flush rest
                if len(files_to_delete["Objects"]):
                    client.delete_objects(Bucket=bucket, Delete=files_to_delete)
            else:
                logger.info("Found no files to delete")

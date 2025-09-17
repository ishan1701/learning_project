import logging

import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

client = boto3.client("dms", region_name="eu-west-1")


def __dms_task_status(task_id: str):
    """
    Purpose: Get DMS Task status
    :param task_id: DMS Task id
    :return: task status
    """
    response = client.describe_replication_tasks(
        Filters=[{"Name": "replication-task-id", "Values": [task_id]}]
    )
    return response["ReplicationTasks"][0]["Status"]


def __get_dms_task_arn(task_id: str):
    """
    :Purpose: Retrun DMS task ARN based on the task name
    :param task_id: task name
    :return: DMS task ARN
    """
    try:
        response = client.describe_replication_tasks(
            Filters=[
                {"Name": "replication-task-id", "Values": [task_id]},
            ]
        )
        return response["ReplicationTasks"][0]["ReplicationTaskArn"]
    except Exception as e:
        logger.error("Error while getting DMS task ARN")
        raise Exception("Error while getting DMS task ARN - {}".format(e))


def stop_dms_task(task_id: str):
    """
    :param task_id:
    :Purpose: Stop the DMS task
    :param arn: DMS task ARN
    :return: None
    """
    logger.info("Getting DMS task ARN")
    arn = __get_dms_task_arn(task_id)
    dms_task_status = __dms_task_status(task_id=task_id)
    if dms_task_status == "stopped":
        logger.info("Task already stopped")
    else:
        logger.info("Stopping DMS task")
        try:
            response = client.stop_replication_task(ReplicationTaskArn=arn)
            waiter = client.get_waiter("replication_task_stopped")
            waiter.wait(
                Filters=[
                    {"Name": "replication-task-arn", "Values": [arn]},
                ],
                WaiterConfig={"Delay": 30, "MaxAttempts": 60},
            )
        except Exception as e:
            logger.error("Error while stopping the DMS task")
            raise Exception("Error while stopping the DMS task {}".format(e))


def start_dms_task(task_id: str):
    """
    :param task_id:
    :Purpose: Stop the DMS task
    :param arn: DMS task ARN
    :return: None
    """
    logger.info("Getting DMS task ARN")
    arn = __get_dms_task_arn(task_id)
    dms_task_status = __dms_task_status(task_id=task_id)
    if dms_task_status == "running":
        logger.info("Task already running")
    else:
        logger.info("starting DMS task")
        try:
            response = client.start_replication_task(
                ReplicationTaskArn=arn, StartReplicationTaskType="resume-processing"
            )
            waiter = client.get_waiter("replication_task_running")
            waiter.wait(
                Filters=[
                    {"Name": "replication-task-arn", "Values": [arn]},
                ],
                WaiterConfig={"Delay": 30, "MaxAttempts": 60},
            )
        except Exception as e:
            logger.error("Error while resuming the DMS task ")
            raise Exception("Error while resuming the DMS task {}".format(e))


def reload_table(task_id: str, schema: str, tables: list):
    """
    :param task_id:
    :Purpose: reload the list of tables with DMS task
    :param arn: DMS task ARN
    :param schema: DMS schema
    :param tables: list of DMS tables to load
    :return: None
    """
    logger.info("Getting DMS task ARN")
    arn = __get_dms_task_arn(task_id)
    logger.info("starting the table reload for tables {}".format(tables))
    table_to_reload = []
    for table in tables:
        table_to_reload.append({"SchemaName": schema, "TableName": table})

    try:
        client.reload_tables(
            ReplicationTaskArn=arn,
            TablesToReload=table_to_reload,
            ReloadOption="data-reload",
        )
    except Exception as e:
        logger.error("Error while reload the DMS table")
        raise Exception("Error while reload the DMS table {}".format(e))

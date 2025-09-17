import logging
from abc import ABC, abstractmethod

from credential_handler import CredentialHandler
from google.cloud import bigquery


def get_bq_client(
    credential_handler: CredentialHandler, project_id: str
) -> bigquery.client:
    credentials = credential_handler.get_credentials()
    print(f"credentials are {credentials}")
    bq_client = bigquery.Client(credentials=credentials, project=project_id)
    return bq_client


def run_bq_query(query: str, project_id: str, credential_handler: CredentialHandler):
    bq_client = get_bq_client(credential_handler, project_id)
    results = bq_client.query(query).result()
    return results


# file loader using strategy design pattern
class GCSBQFileLoader(ABC):
    @staticmethod
    @abstractmethod
    def load_file(
        gcs_path,
        credential_handler: CredentialHandler,
        bq_project_id,
        bq_table_str,
        bq_dataset: str,
        **kwargs,
    ):
        pass


# https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv#python
class CSVFileLoader(GCSBQFileLoader):
    file_type = "csv"

    @staticmethod
    def load_file(
        gcs_path,
        credential_handler: CredentialHandler,
        bq_project_id: str,
        bq_table: str,
        bq_dataset: str,
        **kwargs,
    ):
        # skip_leading_rows = 1 if not 'skip_first_row' in kwargs else 0

        bq_client = get_bq_client(
            credential_handler=credential_handler, project_id=bq_project_id
        )

        load_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.CSV,
            skip_leading_rows=1,
            field_delimiter=kwargs["delimiter"] if "field_delimiter" in kwargs else ",",
            autodetect=True,
        )
        bq_client.load_table_from_uri(
            source_uris=gcs_path,
            destination=f"{bq_project_id}.{bq_dataset}.{bq_table}",
            job_config=load_config,
        )
        logging.info("csv file(s) loaded to bq table")


class ParquetFileLoader(GCSBQFileLoader):
    file_type = "parquet"

    @staticmethod
    def load_file(
        gcs_path,
        credential_handler: CredentialHandler,
        bq_project_id: str,
        bq_table: str,
        bq_dataset: str,
        **kwargs,
    ):
        bq_client = get_bq_client(
            credential_handler=credential_handler, project_id=bq_project_id
        )

        load_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.PARQUET, autodetect=True
        )
        bq_client.load_table_from_uri(
            source_uris=gcs_path,
            destination=f"{bq_project_id}.{bq_dataset}.{bq_table}",
            job_config=load_config,
        )
        logging.info("parquet file(s) loaded to bq table")


class FileLoader:
    def __init__(self, file_loader: GCSBQFileLoader):
        self._file_loader = file_loader

    @property
    def file_loader(self):
        return self._file_loader

    @file_loader.setter
    def file_loader(self, file_loder: GCSBQFileLoader):
        self._file_loader = file_loder

    def load_file(
        self,
        gcs_path,
        credential_handler: CredentialHandler,
        bq_project_id: str,
        bq_table: str,
        bq_dataset: str,
        **kwargs,
    ):
        self.file_loader.load_file(
            gcs_path, credential_handler, bq_project_id, bq_table, bq_dataset, **kwargs
        )


# local_testing
# if __name__ == '__main__':
#     from some_assignment.plugins.credential_handler import CredentialHandler, FileBasedCredentialAuthenticator
#     from some_assignment.plugins.cons import PROJECT_ID, DATASET
#
#     key_file_path = '/Users/ishan.kumar/keys/gcp_service_account.json'
#     file_loader_strategy = CSVFileLoader()
#     file_loader = FileLoader(file_loader=file_loader_strategy)
#
#     print('starting the file loader')
#     file_loader.load_file(gcs_path='gs://some_assignment/csvs/*.csv',
#                           credential_handler=CredentialHandler(
#                               FileBasedCredentialAuthenticator(credentials_file_path=key_file_path)),
#                           bq_project_id=PROJECT_ID,
#                           bq_table='test_load_csv',
#                           bq_dataset=DATASET)
#
#     file_loader_strategy = ParquetFileLoader()
#     file_loader = FileLoader(file_loader=file_loader_strategy)
#     print('starting the file loader')
#     file_loader.load_file(gcs_path='gs://some_assignment/parquets/*.parquet',
#                           credential_handler=CredentialHandler(
#                               FileBasedCredentialAuthenticator(credentials_file_path=key_file_path)),
#                           bq_project_id=PROJECT_ID,
#                           bq_table='test_load_pqt',
#                           bq_dataset=DATASET)

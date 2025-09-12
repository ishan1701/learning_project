import logging
from abc import ABC, abstractmethod

from airflow.providers.google.common.hooks.base_google import GoogleBaseHook
from google.oauth2 import service_account
from google.oauth2.service_account import Credentials


class GCPAuthenticationException(Exception):
    pass


# create credential module to authenticate the gcp via a strategy design pattern
class GCPCredentialAuthenticator(ABC):
    @abstractmethod
    def get_gcp_credentials(self) -> Credentials:
        pass


class AirflowBasedCredentialAuthenticator(GCPCredentialAuthenticator):
    def __init__(self, gcp_conn_id):
        self.conn_id = gcp_conn_id

    def get_gcp_credentials(self):
        credentials = GoogleBaseHook(gcp_conn_id=self.conn_id).get_credentials()
        return credentials


class FileBasedCredentialAuthenticator(GCPCredentialAuthenticator):
    def __init__(self, credentials_file_path):
        self.credentials_file_path = credentials_file_path

    def get_gcp_credentials(self) -> Credentials:
        logging.info("Reading credentials from file")
        print("Reading credentials from file")
        print(self.credentials_file_path)
        credentials = service_account.Credentials.from_service_account_file(
            self.credentials_file_path,
            scopes=["https://www.googleapis.com/auth/cloud-platform"],
        )

        print("Credentials are {}".format(credentials))
        return credentials


# context class
class CredentialHandler:
    def __init__(self, authenticator: GCPCredentialAuthenticator):
        self._authenticator = authenticator

    @property
    def authenticator(self):
        return self._authenticator

    @authenticator.setter
    def authenticator(self, authenticator):
        self._authenticator = authenticator

    def get_credentials(self):
        return self.authenticator.get_gcp_credentials()


# local testing
# if __name__ == '__main__':
#     from some_assignment.plugins.cons import PROJECT_ID
#     from some_assignment.plugins.bigquery import run_bq_query
#
#     KEY_FILE_PATH = '/Users/ishan.kumar/keys/gcp_service_account.json'
#     query = 'select * from `some-project-456015.sample_dataset.test_load_pqt`'
#
#     gcp_credential_handler = CredentialHandler(FileBasedCredentialAuthenticator(credentials_file_path=KEY_FILE_PATH))
#
#     results = run_bq_query(query, credential_handler=gcp_credential_handler, project_id=PROJECT_ID)
#     for row in results:
#         for key, value in row.items():
#             print(key, value)

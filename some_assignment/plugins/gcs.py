from credential_handler import CredentialHandler
import logging
from google.cloud import storage


def get_storage_client(credential_handler: CredentialHandler, project_id: str):
    logging.info('Retrieving gcs credentials')
    credentials = credential_handler.get_credentials()
    gcs_client = storage.Client(credentials=credentials, project=project_id)
    return gcs_client




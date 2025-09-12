import json
import os

import requests

# Replace these with your actual credentials
LOOKER_API_URL = os.getenv("LOOKER_API_URL")


def _get_access_token():
    # Endpoint for token authentication
    AUTH_URL = f"{LOOKER_API_URL}/login"

    # Payload for the POST request
    payload = {
        "client_id": os.getenv("LOOKER_CLIENT_ID"),
        "client_secret": os.getenv("LOOKER_CLIENT_SECRET"),
    }

    # Make the POST request to get the token
    response = requests.post(AUTH_URL, data=payload)

    # Check if the request was successful
    if response.status_code == 200:
        token_data = response.json()
        print(token_data)
        access_token = token_data["access_token"]
        print(f"Access Token: {access_token}")
        return access_token
    else:
        print(f"Failed to authenticate: {response.status_code} - {response.text}")


def _get_project_files(access_token, project_id, file):
    # Example API endpoint (e.g., to get all users)
    API_ENDPOINT = f"{LOOKER_API_URL}/projects/{project_id}/files/file"

    # Headers including the access token
    headers = {"Authorization": f"Bearer {access_token}"}

    params = {
        "file_id": "some_file_id",
        # 'fields': 'content'
    }

    # Make a GET request to the API endpoint
    response = requests.get(API_ENDPOINT, headers=headers, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # data = response.json()
        # print(data)
        # print(response.content)
        print(response.text)
        # with open('output.json', 'w') as outfile:
        #     json.dump(data, outfile)
    else:
        print(f"Failed to fetch : {response.status_code} - {response.text}")


def _get_looks(access_token):
    API_ENDPOINT = f"{LOOKER_API_URL}/looks"

    # Headers including the access token
    headers = {"Authorization": f"Bearer {access_token}"}

    # Make a GET request to the API endpoint
    response = requests.get(API_ENDPOINT, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        print(response.text)
        with open("../../output.json", "w") as outfile:
            json.dump(data, outfile)
    else:
        print(f"Failed to fetch : {response.status_code} - {response.text}")


if __name__ == "__main__":
    access_token = _get_access_token()
    _get_project_files(access_token=access_token, project_id="some", file="some")
    _get_looks(access_token=access_token)

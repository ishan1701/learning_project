# TRACT Coding Challenge

## Background

The main goal of interviews at TRACT is to find a good fit. We hope that you will enjoy working with us and be able to perform your best work in our environment. To this end, our interviews are not filled with gotchas and brainteasers, but attempt to let us work together in well-reasoned scenarios that mimic a collaborative environment.

## The Challenge

Isabel works for a food distributor. Her company buys agricultural products and sells them on the market. Isabel's company wants to analyze the impact of their suppliers on the environment. The first analysis they've decided to do is to provide deforestation of shipments from the affected farms.

## The Interview Format

You will pair with an interviewer who will observe you code through your solutions. The interviewer may ask questions or offer suggestions, but you will choose the areas of code to work on. You may use any reference materials and tools that you use in your normal course of work. We believe that the best engineers will use references when needed, but have enough mastery of basic syntax, skills and best practices that they can work independently to a large measure. You should feel comfortable using your normal workflow.

### Be prepared for the next tasks

Here are some examples of things you might work on:
- Add additional reports or analysis
- Make improvements to the current processes
- Refactor or reformat code to be more performant and readable
- Make architecture more efficient and maintainable

## Prep Work

Please clone this repo, look through the code, and complete the setup steps before your interview. You should also have an idea of areas of the code you will want to work on during the interview, so that we don't spend time during the interview trying to find work rather than coding.

While not required, it may help you to spend a few minutes coding in the project to see how it works. You may make any changes you'd like.

## Running the Project Locally
To run Apache Airflow locally for development and testing purposes, you'll need Docker and Docker Compose installed on your machine.

### Prerequisites
- Docker
- Docker Compose
- Google IAM identity granted permission to project
- Google Cloud service account key with appropriate permissions for BigQuery and Google Cloud Storage access.

### Setup Steps

1. **Clone the repository:**

2. **Place your Google Cloud service account key in the root directory:**
Rename your service account key file to `gcp_service_account.json` and place it in the root directory of the cloned repository. This file is mounted into the Airflow containers to authenticate with Google Cloud.

3. **Start Apache Airflow locally:**
Use Docker Compose to build and start the Airflow environment:
`docker-compose up`

4. **Access the Airflow Web UI:**
Open `http://localhost:8080` in your web browser to access the Airflow web interface. The default login credentials are:
- Username: `airflow`
- Password: `airflow`

5. **Trigger the DAGs manually:**
- Navigate to the DAGs list in the Airflow web UI.
- Find the `deforestation_row_count` and `read_and_insert_shipmentdata` DAGs.
- Trigger each DAG manually and monitor the execution status.

## DAGs Overview

### 1. Deforestation Status Reporting (`deforestation_dag.py`)
This DAG queries a BigQuery table to log the deforestation status for farms. It aggregates the data by deforestation status, providing insights into the count of farms affected by each status.

**Key Features:**
- Queries BigQuery to aggregate data by `DeforestationStatus`.
- Logs the count of unique `FarmID` associated with each deforestation status.

### 2. Shipment Report Generation (`farms_volume_dag.py`)
This DAG generates a report for shipments per country by pulling data from Google Cloud Storage and inserting the aggregated results into BigQuery.

**Key Features:**
- Pulls shipment data from Google Cloud Storage.
- Aggregates shipment volume by country.
- Inserts aggregated data into a BigQuery table for analysis.

### 3. European Union Countries List (`static.py`)
The repository includes a Python file named `static.py`, which defines a list of countries that are members of the European Union (EU). This list is crucial for filtering or aggregating data based on whether shipments are coming from or going to EU countries.

# Use the official Apache Airflow image as the base image
FROM apache/airflow:2.10.5-python3.10

WORKDIR /app
# Switch to the root user to install system dependencies
USER root

# Install any system dependencies required for dbt
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Switch back to the airflow user
USER airflow

# Install dbt and the required adapter (e.g., dbt-postgres, dbt-snowflake, etc.)
RUN pip install  --no-cache-dir \
    dbt-core \
    dbt-postgres  # Replace with the appropriate adapter if needed

# Set the environment variable to include the user's Python packages
ENV PATH="/home/airflow/.local/bin:${PATH}"

# Optionally, you can add dbt profiles and project files if needed
# COPY dbt_profiles.yml /home/airflow/.dbt/profiles.yml
# COPY dbt_project /home/airflow/dbt_project

# Switch back to the airflow user (if not already)
USER airflow




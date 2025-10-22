from pathlib import Path

from pyspark.sql import DataFrame, SparkSession
from utils import get_pyspark_session, load_yaml
import os

CONFIG_PATH = "config.yaml"
APP_NAME = "pyspark_app"
OPEN_TABLE_FORMAT = "iceberg"
SAMPLE_JSON_DATA = "sample_data.json"
NEW_NAMESPACE = "demo_namespace"


def _exercise_1_basic_iceberg(spark: SparkSession):
    # list all the namespaes in the catalog
    spark.sql("show namespaces in nessie").show(truncate=False)

    # List existing catalogs
    spark.sql("show catalogs").show(truncate=False)

    # list all databases
    spark.sql("show databases in nessie").show(truncate=False)

    # # list branches in nessie
    # spark.sql("list branches in nessie").show(truncate=False)

    spark.sql("create namespace if not exists nessie.demo_namespace").show(
        truncate=False
    )

    spark.sql("show namespaces in nessie").show(truncate=False)

    spark.sql("create database if not exists nessie.demo_db")

    spark.sql("show databases in nessie").show(truncate=False)

    spark.sql(
        "create table if not exists nessie.demo_namespace.employee (id int, name string, age int, profession string, city string) using iceberg"
    ).show(truncate=False)

    spark.sql("show catalogs").show(truncate=False)

    spark.sql("show namespaces").show(truncate=False)
    spark.sql("show tables in nessie.demo_namespace").show(truncate=False)


def _exercise_2_iceberg_operations():
    nessie_url = os.getenv("NESIE_URL")
    print(f"NESIE URL: {nessie_url}")

    # client = NessieClient(nessie_url)
    # print(client)
    #
    # print(client.get_base_url())



def _exercise_3_transformations(spark: SparkSession):
    pass


def _exercise_4_schema_evolution(spark: SparkSession):
    pass


def _exercise_5_time_travel(spark: SparkSession):
    pass


def main(config: dict):
    # spark = get_pyspark_session(
    #     config=config, app_name=APP_NAME, open_table_format=OPEN_TABLE_FORMAT
    # )

    # _exercise_1_basic_iceberg(spark=spark)
    _exercise_2_iceberg_operations()

if __name__ == "__main__":

    import attr
    print(attr.__version__)
    config = load_yaml(file_path=CONFIG_PATH)
    main(config=config)
    os.getenv("AWS_ACCESS_KEY_ID")
    os.getenv("AWS_SECRET_ACCESS_KEY")
    os.getenv("AWS_EC2_METADATA_DISABLED")
    os.getenv("AWS_REGION")

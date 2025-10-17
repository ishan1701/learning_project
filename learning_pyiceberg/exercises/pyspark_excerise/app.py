# to do
# 1. create spark session and connect to nessie
# 2. create a simple json and read it as dataframe
# 3. check if iceberg table is existing
# 4. First create a table based on the schema provided
# 5. Pyspark should not create the table. Its only insert the dataclasses


from pyspark.sql import DataFrame
from utils import get_pyspark_session, load_yaml
from pathlib import Path

CONFIG_PATH = "config.yaml"
APP_NAME = "pyspark_app"
OPEN_TABLE_FORMAT = "iceberg"
SAMPLE_JSON_DATA = "sample_data.json"
NEW_NAMESPACE = "demo_namespace"


def main(config: dict):
    spark = get_pyspark_session(config=config, app_name=APP_NAME, open_table_format=OPEN_TABLE_FORMAT)
    data_file = str(Path(__file__).parent.parent.joinpath("data", SAMPLE_JSON_DATA))
    print(f"Loading data from {data_file}")


    df = spark.read.format("json").load(data_file)
    df.printSchema()

    # list all the namespaes in the catalog


    # List existing catalogs and branches in Nessie.
    spark.sql("show catalogs").show(truncate=False)
    #
    # spark.sql("show databases").show(truncate=False)
    #
    spark.sql("show namespaces").show(truncate=False)

    # spark.sql("show tables").show(truncate=False)

    spark.sql("create namespace if not exists nessie.demo_namespace").show(truncate=False)

    spark.sql("show namespaces").show(truncate=False)

    spark.sql("create table if not exists nessie.demo_namespace.demo_table (id int, name string, age int) using iceberg").show(truncate=False)

    spark.sql("show catalogs").show(truncate=False)

    spark.sql("show namespaces").show(truncate=False)
    spark.sql("show tables in nessie.demo_namespace").show(truncate=False)





if __name__ == '__main__':
    config = load_yaml(file_path=CONFIG_PATH)

main(config=config)

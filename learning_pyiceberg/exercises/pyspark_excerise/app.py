from pathlib import Path

from pyspark.sql import DataFrame, SparkSession
from utils import get_pyspark_session, load_yaml
import os
from datetime import date
from loguru import logger

from pyspark.sql.types import StringType, StructField, StructType, IntegerType, DateType

CONFIG_PATH = "config.yaml"
APP_NAME = "pyspark_app"
OPEN_TABLE_FORMAT = "iceberg"
SAMPLE_JSON_DATA = "sample_data.json"
NEW_NAMESPACE = "demo_namespace"
TABLE_NAME = "employee_partitioned_wth_df_write_save_with_create_one_more"
schema = StructType(
    [
        StructField("id", IntegerType(), True),
        StructField("name", StringType(), True),
        StructField("age", IntegerType(), True),
        StructField("profession", StringType(), True),
        StructField("city", StringType(), True),
        StructField("dob", DateType(), True),
    ]
)

new_schema = StructType(
    [
        StructField("id", IntegerType(), True),
        StructField("name", StringType(), True),
        StructField("age", IntegerType(), True),
        StructField("profession", StringType(), True),
        StructField("city", StringType(), True),
        StructField("dob", DateType(), True),
        StructField("department", StringType(), True),
    ]
)


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
        f"""
        CREATE TABLE IF NOT EXISTS nessie.demo_namespace.{TABLE_NAME}
           (
               id  int,
               name string,
               age  int,
               profession string,
               city string,
               dob date
           ) USING iceberg 
            PARTITIONED BY (month(dob))
        """
    ).show(truncate=False)

    data = [
        (101, "Alice Johnson", 34, "Software Engineer", "New York", date(1991, 3, 15)),
        (102, "Bob Smith", 48, "Architect", "London", date(1977, 11, 20)),
        (103, "Charlie Brown", 22, "Student", "Paris", date(2003, 7, 1)),
        (104, "Diana Lee", 55, "Doctor", "Sydney", date(1970, 1, 10)),
        (105, "Ethan Wang", 29, "Data Scientist", "San Francisco", date(1996, 5, 25)),
        (106, "Fiona Garcia", 41, "Teacher", "Madrid", date(1984, 9, 8)),
        (107, "George Harris", 62, "Retired", "Tokyo", date(1963, 4, 19)),
        (108, "Hannah Kim", 27, "Financial Analyst", "Toronto", date(1998, 12, 3)),
        (109, "Ivan Petrova", 38, "Chef", "Berlin", date(1987, 6, 12)),
        (110, "Jasmine Kaur", 31, "Journalist", "Mumbai", date(1994, 10, 28)),
    ]

    spark.sql("show catalogs").show(truncate=False)

    spark.sql("show namespaces").show(truncate=False)
    spark.sql("show tables in nessie.demo_namespace").show(truncate=False)

    df = spark.createDataFrame(data, schema)

    df.printSchema()

    df.writeTo(f"nessie.demo_namespace.{TABLE_NAME}").append()
    # df.write.format("iceberg").mode("append").save(f"nessie.demo_namespace.{TABLE_NAME}")

def _exercise_2_iceberg_operations():
    nessie_url = os.getenv("NESIE_URL")
    print(f"NESIE URL: {nessie_url}")

    # client = NessieClient(nessie_url)
    # print(client)
    #
    # print(client.get_base_url())


def _exercise_3_transformations(spark: SparkSession):
    pass


def _exercise_4_schema_evolution(spark: SparkSession, is_add_column: bool = False, column_name:str =None, column_type:str =None):

    ## lets chnage the schema by adding a new column 'department'
    spark.sql("show namespaces in nessie").show(truncate=False)
    if is_add_column:
        assert column_name is not None, "column_name must be provided when is_add_column is True"
        assert column_type is not None, "column_type must be provided when is_add_column is True"

        logger.info("changing schema by adding new column 'department'")
        spark.sql(
            f"alter table nessie.demo_namespace.{TABLE_NAME} add column if not exists {column_name} {column_type}"
        )

    logger.info("describing the table after schema evolution")
    spark.sql(f"describe table formatted nessie.demo_namespace.{TABLE_NAME}").show(
        truncate=False
    )

    # ## add new data without department column
    # data_batch_2 = [
    #     (111, "Kevin Chen", 25, "Graphic Designer", "Shanghai", date(2000, 2, 18)),
    #     (112, "Laura Mendes", 51, "Nurse", "São Paulo", date(1974, 8, 7)),
    #     (113, "Mark Wilsons", 36, "Electrician", "Chicago", date(1989, 11, 29)),
    #     (114, "Nancy Drew", 68, "Librarian", "Boston", date(1957, 1, 5)),
    #     (115, "Oscar Rodriguez", 44, "Sales Manager", "Mexico City", date(1981, 4, 14)),
    #     (116, "Penny Hofstadter", 23, "Waitress", "Los Angeles", date(2002, 10, 17)),
    #     (117, "Quentin Jones", 59, "University Professor", "Cambridge", date(1966, 7, 22)),
    #     (118, "Ruby Singh", 30, "Marketing Specialist", "Delhi", date(1995, 9, 3)),
    #     (119, "Sam Fischer", 47, "Pilot", "Dubai", date(1978, 5, 11)),
    #     (120, "Tracy Lee", 33, "Fitness Instructor", "Seoul", date(1992, 12, 6))
    # ]
    #
    # df= spark.createDataFrame(data_batch_2, schema)
    # df.writeTo("nessie.demo_namespace.employee_partitioned").append()

    ## add new data with department column
    data_batch_3 = [
        (
            121,
            "Victor Schmidt",
            39,
            "Biologist",
            "Munich",
            date(1986, 2, 5),
            "Research",
        ),
        (
            122,
            "Wendy Torres",
            26,
            "Software Developer",
            "Seattle",
            date(1999, 8, 11),
            "Technology",
        ),
        (
            123,
            "Xavier Stone",
            45,
            "Legal Counsel",
            "Brussels",
            date(1980, 4, 20),
            "Legal",
        ),
        (
            124,
            "Yara Al-Farsi",
            32,
            "Product Manager",
            "Dubai",
            date(1993, 11, 15),
            "Product",
        ),
        (125, "Zane Powell", 58, "Geologist", "Denver", date(1967, 6, 28), "Energy"),
        (126, "Amy Baker", 24, "Accountant", "Dublin", date(2001, 9, 10), "Finance"),
        (
            127,
            "Ben Carter",
            40,
            "Firefighter",
            "Houston",
            date(1985, 3, 23),
            "Emergency",
        ),
        (128, "Chloe Evans", 35, "Photographer", "Rome", date(1990, 7, 7), "Media"),
        (
            129,
            "Daniel King",
            53,
            "Construction Manager",
            "Miami",
            date(1972, 1, 30),
            "Operations",
        ),
        (
            130,
            "Ella Reed",
            28,
            "HR Specialist",
            "Amsterdam",
            date(1997, 10, 4),
            "Human Resources",
        ),
    ]

    df = spark.createDataFrame(data_batch_3, new_schema)
    logger.info("printting schema of new dataframe to be appended")
    df.printSchema()
    df.writeTo("nessie.demo_namespace.employee_partitioned").append()


def _print_table_records(spark: SparkSession, iceberg_table_fqdn: str) -> None:
    df = spark.read.format("iceberg").load(iceberg_table_fqdn)
    df.printSchema()
    df.createOrReplaceTempView("t1")
    spark.sql("select * from t1").show(truncate=False)


def _exercise_5_time_travel(spark: SparkSession):
    pass


def main(config: dict):
    spark = get_pyspark_session(
        config=config, app_name=APP_NAME, open_table_format=OPEN_TABLE_FORMAT
    )

    _exercise_1_basic_iceberg(spark=spark)
    _print_table_records(
        spark=spark, iceberg_table_fqdn=f"nessie.demo_namespace.{TABLE_NAME}"
    )
    # _exercise_4_schema_evolution(spark=spark, is_add_column=False)
    # _print_table_records(
    #     spark=spark, iceberg_table_fqdn=f"nessie.demo_namespace.{TABLE_NAME}"
    # )


if __name__ == "__main__":
    import attr

    print(attr.__version__)
    config = load_yaml(file_path=CONFIG_PATH)

    aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
    os.getenv("AWS_SECRET_ACCESS_KEY")
    os.getenv("AWS_EC2_METADATA_DISABLED")
    os.getenv("AWS_REGION")

    print(f" the is {aws_access_key}")
    main(config=config)

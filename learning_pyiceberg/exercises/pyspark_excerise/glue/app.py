import random
from datetime import datetime

from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType, StructField,
    LongType, StringType,
    DoubleType, DateType, TimestampType
)

S3_TABLE_NAMESPACE = "s3_dr_poc"
S3_TABLE_NAME = "orders_glue"
ROLL_BACK_SNAPSHOT_ID = "4525037377477492118"

SCHEMA = StructType([
    StructField("order_id", LongType(), False),
    StructField("customer_id", LongType(), False),
    StructField("order_status", StringType(), False),
    StructField("order_amount", DoubleType(), False),
    StructField("order_date", StringType(), False),
    StructField("created_ts", StringType(), False),
    StructField("debug_flag", StringType(), True)
])

today = datetime.today().strftime("%Y-%m-%d")
now = str(datetime.now())
data_dict = {
    "CREATED": [
        (310001, 11001, "CREATED", 101.10, today, now, None),
        (310002, 11002, "CREATED", 102.20, today, now, None),
        (310003, 11003, "CREATED", 103.30, today, now, None),
        (310004, 11004, "CREATED", 104.40, today, now, None),
        (310005, 11005, "CREATED", 105.50, today, now, None),
        (310006, 11006, "CREATED", 106.60, today, now, None),
        (310007, 11007, "CREATED", 107.70, today, now, None),
        (310008, 11008, "CREATED", 108.80, today, now, None),
        (310009, 11009, "CREATED", 109.90, today, now, None),
        (310010, 11010, "CREATED", 110.00, today, now, None),
    ],
    "PAID": [
        (320001, 12001, "PAID", 201.10, today, now, None),
        (320002, 12002, "PAID", 202.20, today, now, None),
        (320003, 12003, "PAID", 203.30, today, now, None),
        (320004, 12004, "PAID", 204.40, today, now, None),
        (320005, 12005, "PAID", 205.50, today, now, None),
        (320006, 12006, "PAID", 206.60, today, now, None),
        (320007, 12007, "PAID", 207.70, today, now, None),
        (320008, 12008, "PAID", 208.80, today, now, None),
        (320009, 12009, "PAID", 209.90, today, now, None),
        (320010, 12010, "PAID", 210.00, today, now, None),
    ],
    "SHIPPED": [
        (330001, 13001, "SHIPPED", 301.10, today, now, None),
        (330002, 13002, "SHIPPED", 302.20, today, now, None),
        (330003, 13003, "SHIPPED", 303.30, today, now, None),
        (330004, 13004, "SHIPPED", 304.40, today, now, None),
        (330005, 13005, "SHIPPED", 305.50, today, now, None),
        (330006, 13006, "SHIPPED", 306.60, today, now, None),
        (330007, 13007, "SHIPPED", 307.70, today, now, None),
        (330008, 13008, "SHIPPED", 308.80, today, now, None),
        (330009, 13009, "SHIPPED", 309.90, today, now, None),
        (330010, 13010, "SHIPPED", 310.00, today, now, None),
    ],
    "JUNKED": [
        (990001, 99001, "JUNK", 0.01, today, now, "BAD_DEBUG"),
        (990002, 99002, "JUNK", 0.01, today, now, "BAD_DEBUG"),
        (990003, 99003, "JUNK", 0.01, today, now, "BAD_DEBUG"),
        (990004, 99004, "JUNK", 0.01, today, now, "BAD_DEBUG"),
        (990005, 99005, "JUNK", 0.01, today, now, "BAD_DEBUG"),
        (990006, 99006, "JUNK", 0.01, today, now, "BAD_DEBUG"),
        (990007, 99007, "JUNK", 0.01, today, now, "BAD_DEBUG"),
        (990008, 99008, "JUNK", 0.01, today, now, "BAD_DEBUG"),
        (990009, 99009, "JUNK", 0.01, today, now, "BAD_DEBUG"),
        (990010, 99010, "JUNK", 0.01, today, now, "BAD_DEBUG"),
    ],
}


def _get_pyspark_session(app_name) -> SparkSession:
    """return spark session"""
    spark = (
        SparkSession.builder.appName(app_name)
        .config(
            "spark.jars.packages",
            "org.apache.iceberg:iceberg-spark-runtime-3.4_2.12:1.4.2",
        )
        .config(
            "spark.sql.extensions",
            "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions",
        )
        .config("spark.sql.defaultCatalog", "s3tables")
        .config("spark.sql.catalog.s3tables", "org.apache.iceberg.spark.SparkCatalog")
        .config(
            "spark.sql.catalog.s3tables.catalog-impl",
            "org.apache.iceberg.aws.glue.GlueCatalog",
        )
        .config(
            "spark.sql.catalog.s3tables.glue.id",
            "acccount:s3tablescatalog/lake-formation-poc",
        )
        .config(
            "spark.sql.catalog.s3tables.warehouse",
            "s3://lf-poc-lakeformation/aws_glue_warehouse/",
        )
        .getOrCreate()
    )
    return spark


def _create_iceberg_table(spark: SparkSession):
    spark.sql(
        f"""CREATE TABLE IF NOT EXISTS s3tables.{S3_TABLE_NAMESPACE}.{S3_TABLE_NAME} (
                    order_id        BIGINT,
                    customer_id     BIGINT,
                    order_status    string,
                    order_amount    DECIMAL(10,2),
                    order_date      string,
                    created_ts      string,
                    debug_flag      string
                )
                TBLPROPERTIES (
                  'table_type' = 'iceberg',
                  'write_compression'='zstd'
                );"""
    )
    print("Iceberg table created")


def _insert_batch_data(spark: SparkSession, selected_status=None):
    if not selected_status:
        selected_status = random.choice(["CREATED", "PAID", "SHIPPED"])
    rows_to_insert = data_dict[selected_status]
    print(f"Inserting {len(rows_to_insert)} rows for status: {selected_status}")

    df = spark.createDataFrame(rows_to_insert, schema=SCHEMA)
    df.printSchema()

    print("Data to be inserted")
    df.show(truncate=False)
    df.writeTo(f"s3tables.{S3_TABLE_NAMESPACE}.{S3_TABLE_NAME}").append()
    print(f"data inserted for status: {selected_status}")


def _iceberg_table_metadata(spark: SparkSession):
    spark.sql(f"show tables in s3tables.{S3_TABLE_NAMESPACE}").show(truncate=False)
    spark.sql(f"select * from s3tables.{S3_TABLE_NAMESPACE}.{S3_TABLE_NAME}").show(
        truncate=False
    )

    table_df = spark.sql(f"describe s3tables.{S3_TABLE_NAMESPACE}.{S3_TABLE_NAME}")
    table_df.printSchema()

    # Get the snapshot infos
    snapshots_df = spark.sql(
        f"""
         SELECT committed_at,
                snapshot_id,
                parent_id,
                operation
         FROM s3tables.{S3_TABLE_NAMESPACE}.{S3_TABLE_NAME}.snapshots
         ORDER BY committed_at desc
         """
    )

    print("______________________ICEBERG TABLE SNAPSHOTS______________________")
    snapshots_df.show(truncate=False)


def _rollback_iceberg_table(spark: SparkSession, snapshot_id: str):
    print(f"Rolling back to snapshot id: {snapshot_id}")
    spark.sql(f"""
                CALL s3tables.system.rollback_to_snapshot(
                    table => '{S3_TABLE_NAMESPACE}.{S3_TABLE_NAME}',
                    snapshot_id => {snapshot_id}
                )
            """)

    print(f"Successfully rolled back table to snapshot {snapshot_id}")


def main():
    spark = _get_pyspark_session(app_name="AWS_GLUE_LOCAL_DR_POC")
    _create_iceberg_table(spark=spark)  # create the iceberg table
    for _ in range(5):
        _insert_batch_data(spark=spark)  # insert the batch
        _iceberg_table_metadata(spark=spark)  # check the snapshot details

    _insert_batch_data(spark=spark, selected_status="JUNKED")  # insert the batch of corrupted data

    # rollback to a specific snapshot id
    _rollback_iceberg_table(spark=spark, snapshot_id=ROLL_BACK_SNAPSHOT_ID)

    _insert_batch_data(spark=spark, selected_status="PAID")
    _iceberg_table_metadata(spark=spark)




if __name__ == "__main__":
    main()

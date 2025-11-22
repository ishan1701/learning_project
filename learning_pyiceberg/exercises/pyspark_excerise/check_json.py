from pyspark.sql import SparkSession
from pyspark import SparkConf


def _create_spark_session() -> SparkSession:
    spark_conf = (
        SparkConf()
        .setAppName("sne")
        .set("spark.driver.host", "127.0.0.1")
        .set("spark.driver.bindAddress", "0.0.0.0")
    )
    spark = SparkSession.builder.config(conf=spark_conf).getOrCreate()
    return spark


if __name__ == '__main__':
    spark = _create_spark_session()
    df = spark.read.json(
        "/Users/ishan.kumar/PycharmProjects/learning_project/learning_pyiceberg/exercises/data/data.jsonl")

    df.printSchema()

    print(df.schema.json())



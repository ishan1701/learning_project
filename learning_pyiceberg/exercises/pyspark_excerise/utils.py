# utility functions for pyspark exercises
from pyspark.sql import SparkSession, DataFrame
from pyspark import SparkConf
from loguru import logger
import yaml
from pathlib import Path


def _create_spark_conf(app_name: str, config: dict, open_table_format, catalog_type: str = "nessie") -> SparkConf:
    """create spark conf"""
    config = config["open_table_format"][open_table_format]['catalog'][catalog_type]

    spark_conf = SparkConf().setAppName(app_name).set("spark.driver.host", "127.0.0.1").set("spark.driver.bindAddress",
                                                                                            "0.0.0.0")
    for key, value in config.items():
        spark_conf.set(key, value)

    return spark_conf


def get_pyspark_session(config: dict, app_name, open_table_format) -> SparkSession:
    """return spark session"""
    logger.info(f"Getting pyspark session for {app_name}")
    spark_conf = _create_spark_conf(app_name=app_name, config=config, open_table_format=open_table_format)
    logger.info(f"spark conf: {spark_conf.__dict__}")
    logger.info("creating spark session")
    spark = SparkSession.builder.config(conf=spark_conf).getOrCreate()
    return spark


def load_yaml(file_path: str) -> dict:
    """Load yaml config"""
    with open(Path(file_path)) as yaml_file:
        data = yaml.load(yaml_file, Loader=yaml.FullLoader)

    return data

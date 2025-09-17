import json
import logging
import os

import job_creator
from ops_config import load_op_job_configs

logger = logging.getLogger()
logger.setLevel(logging.INFO)


env = os.environ.get("")
CONFIG_BUCKET = "-".join([os.environ.get("OPERATION_CONFIG_BUCKET"), env])


def lambda_handler(event, context):
    logger.info(f"Initializing Lambda with the event: {event}")
    # 1: get bucket and object key from event pointing to the config yml
    # 2: get the config yml object
    # 3: create the task dag
    # 4: process the dag

    op_configs = load_op_job_configs(CONFIG_BUCKET, "config.yml", env)

    for config in op_configs:
        dag = job_creator.get_creator(config.action, config).create_op_dag()
        logger.info(f"printing dag ::{dag.print_task()}")
        dag.process_task()

    logger.info("Lambda has finished its execution")
    return {"statusCode": 200, "body": json.dumps("SUCCESS")}


# Local testing purposes
# if __name__ == '__main__':
#      lambda_handler(None, None)

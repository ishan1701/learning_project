import yaml
import logging
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

_s3_client = boto3.client('s3')


class OpJobConfig:

    def __init__(self,
                 config,
                 dms_task,
                 env):
        self.dms_task = dms_task
        self.team = config['team']
        self.project = config['project']
        self.platform = config['platform']
        self.schema = config['schema']
        self.tables = config['tables']
        self.action = config['action']
        self.dms_s3_bucket = '-'.join([config['dms_s3_bucket'], env])
        self.hudi_table_bucket = '-'.join([config['hudi_table_bucket'], env])
        self.hudi_config_bucket = '-'.join([config['hudi_config_bucket'],env])


def _load_config_yml(s3_bucket: str, s3_object_key: str):
    logger.info(f"Getting the config.yml from the s3://{s3_bucket}/{s3_object_key}")
    response = _s3_client.get_object(Bucket=s3_bucket, Key=s3_object_key)
    logger.info(f"response:{response}")
    ops_config_yml = yaml.safe_load(response["Body"])
    return ops_config_yml


def load_op_job_configs(s3_bucket: str, s3_object_key: str,env:str):
    op_config_yml = _load_config_yml(s3_bucket, s3_object_key)
    op_tasks = op_config_yml['tasks']
    logger.info(f"tasks:{op_tasks}")
    config_list = []
    for dms_task, config in op_tasks.items():
        op_config = OpJobConfig(config, dms_task,env)
        config_list.append(op_config)
    logger.info(f"op_config_list:{config_list}")
    return config_list

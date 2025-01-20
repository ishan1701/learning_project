import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

_glue_client = boto3.client('glue')


def reset_glue_job_bookmark(team: str,
                            project: str,
                            platform: str,
                            schema: str,
                            tables: list):
    """
    Purpose: Reset the glue job bookmark
    :param project:
    :param team:
    :param platform:
    :param schema:
    :param tables:
    :return: None
    """


    for table in tables:
        job_name = '-'.join([team, project, platform, schema, table])
        try:
            _glue_client.reset_job_bookmark(
                JobName=job_name,
            )
        except Exception as e:
            logger.error(f'Error while resetting the glue job {job_name}')
            raise Exception(f'Error while resetting the glue job - {e}')


def run_glue_job(team: str,
                 project: str,
                 platform: str,
                 schema: str,
                 tables: list,
                 config_bucket: str,
                 worker_type='G.1X',
                 workers=60):
    for table in tables:
        job_name = '-'.join([team, project, platform, schema, table])
        task_name = '-'.join([team, platform, schema])
        config_filename = '/'.join(['script', task_name, 'config.yaml'])
        logger.info(f"Starting a Glue Job '{job_name}' with '{workers}' workers")

        response = _glue_client.start_job_run(
            JobName=job_name,
            Arguments={
                '--job-bookmark-option': 'job-bookmark-enable',
                '--enable-glue-datacatalog': '',
                '--enable-continuous-cloudwatch-log': 'true',
                '--enable-continuous-log-filter': 'true',
                '--config_filename': config_filename,
                '--bucket': config_bucket,
                '--task_name': task_name,
                '--table_name': table
            },
            Timeout=150,
            WorkerType=worker_type,
            NumberOfWorkers=workers
        )

        job_id = response['JobRunId']
        logger.info(f"The Glue Job '{job_id}' for the Job name '{job_name}' started successfully")

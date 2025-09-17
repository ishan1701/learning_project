from abc import ABC, abstractmethod
from typing import List

import dms_operations as dms
import hudi_glue as glue
import s3_operations as s3


class AbstractTask(ABC):
    @abstractmethod
    def process_task(self):
        pass

    @abstractmethod
    def print_task(self):
        pass


class StopDmsTask(AbstractTask):
    def __init__(self, config):
        self._op_config = config

    def process_task(self):
        dms.stop_dms_task(task_id=self._op_config.dms_task)

    def print_task(self):
        return __class__.__name__


class DeleteRawDataTask(AbstractTask):
    def __init__(self, config):
        self._op_config = config

    def process_task(self):
        s3.delete_s3_data(
            bucket=self._op_config.dms_s3_bucket,
            prefix=self._op_config.dms_task,
            schema=self._op_config.schema,
            tables=self._op_config.tables,
            archive_flag=True,
        )

    def print_task(self):
        return __class__.__name__


class DeleteProcessedDataTask(AbstractTask):
    def __init__(self, config):
        self._op_config = config

    def process_task(self):
        s3.delete_s3_data(
            bucket=self._op_config.hudi_table_bucket,
            prefix=self._op_config.dms_task,
            schema=None,
            tables=self._op_config.tables,
            archive_flag=False,
        )

    def print_task(self):
        return __class__.__name__


class StartDmsTask(AbstractTask):
    def __init__(self, config):
        self._op_config = config

    def process_task(self):
        dms.start_dms_task(task_id=self._op_config.dms_task)

    def print_task(self):
        return __class__.__name__


class ReloadTableTask(AbstractTask):
    def __init__(self, config):
        self._op_config = config

    def process_task(self):
        dms.reload_table(
            task_id=self._op_config.dms_task,
            schema=self._op_config.schema,
            tables=self._op_config.tables,
        )

    def print_task(self):
        return __class__.__name__


class ResetGlueBookmarkTask(AbstractTask):
    def __init__(self, config):
        self._op_config = config

    def process_task(self):
        glue.reset_glue_job_bookmark(
            team=self._op_config.team,
            project=self._op_config.project,
            platform=self._op_config.platform,
            schema=self._op_config.schema,
            tables=self._op_config.tables,
        )

    def print_task(self):
        return __class__.__name__


class RunGlueHudiTask(AbstractTask):
    def __init__(self, config):
        self._op_config = config

    def process_task(self):
        glue.run_glue_job(
            team=self._op_config.team,
            project=self._op_config.project,
            platform=self._op_config.platform,
            schema=self._op_config.schema,
            tables=self._op_config.tables,
            config_bucket=self._op_config.hudi_config_bucket,
        )

    def print_task(self):
        return __class__.__name__


class OperationJob(AbstractTask):
    tasks: List[AbstractTask] = None

    def __init__(self):
        self.tasks = list()

    def process_task(self):
        for task in self.tasks:
            task.process_task()

    def add_tasks(self, task):
        self.tasks.append(task)

    def print_task(self):
        tasks_string = ""
        for task in self.tasks:
            tasks_string += task.print_task() + "->"
        return tasks_string


def get_task(op, config) -> AbstractTask:
    if op == "stop_dms_task":
        return StopDmsTask(config)
    elif op == "delete_raw_data":
        return DeleteRawDataTask(config)
    elif op == "delete_processed_data":
        return DeleteProcessedDataTask(config)
    elif op == "reset_job_bookmark":
        return ResetGlueBookmarkTask(config)
    elif op == "start_dms_task":
        return StartDmsTask(config)
    elif op == "reload_table":
        return ReloadTableTask(config)
    elif op == "run_glue_job":
        return RunGlueHudiTask(config)
    else:
        raise Exception(f"Wrong operation found -{op}")

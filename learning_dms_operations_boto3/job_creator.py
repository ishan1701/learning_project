from abc import ABC, abstractmethod
from task_node import AbstractTask, OperationJob, get_task


class JobCreator(ABC):

    @abstractmethod
    def create_op_dag(self) -> AbstractTask:
        pass


class ReloadAllCreator(JobCreator):

    def __init__(self, config):
        self.config = config

    def create_op_dag(self) -> AbstractTask:
        tasks = OperationJob()
        tasks.add_tasks(get_task('stop_dms_task', self.config))
        tasks.add_tasks(get_task('delete_raw_data', self.config))
        tasks.add_tasks(get_task('delete_processed_data', self.config))
        tasks.add_tasks(get_task('reset_job_bookmark',self.config))
        tasks.add_tasks(get_task('start_dms_task', self.config))
        tasks.add_tasks(get_task('reload_table', self.config))
        return tasks


class ReloadStandardDataCreator(JobCreator):

    def __init__(self, config):
        self.config = config

    def create_op_dag(self) -> AbstractTask:
        tasks = OperationJob()
        tasks.add_tasks(get_task('delete_processed_data', self.config))
        tasks.add_tasks(get_task('reset_job_bookmark', self.config))
        tasks.add_tasks(get_task('run_glue_job', self.config))
        return tasks


class CustomOpsCreator(JobCreator):

    def __init__(self, action, config):
        self.action = action
        self.config = config

    def create_op_dag(self) -> AbstractTask:
        tasks = OperationJob()
        ops = self.action.split('->')
        for op in ops:
            tasks.add_tasks(get_task(op, self.config))
        return tasks


def get_creator(action, config) -> JobCreator:
    if action == 'reload_all':
        return ReloadAllCreator(config)
    elif action == 'reload_standard_data':
        return ReloadStandardDataCreator(config)
    else:
        return CustomOpsCreator(action, config)

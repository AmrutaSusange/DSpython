import logging.config
from logging import LoggerAdapter
from typing import Optional


class OnlyOneInstanceEnforcer:
    """Ensures that only a single instance of any class inheriting from this class can exist."""
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
        return cls._instances[cls]

class ContextualLoggerAdapter(LoggerAdapter):
    def process(self, msg, kwargs):
        if "extra" not in kwargs:
            kwargs["extra"] = {}
        kwargs["extra"].update(self.extra)

        prefix = self.extra.get("cat_src_vs_target_prefix", "")
        return f"{prefix}{msg}", kwargs

class Logger(OnlyOneInstanceEnforcer):
    """Inherits from InstanceEnforcer to guarantee a single logger instance
    throughout the program's lifecycle. The logging.config.dictConfig method
    is employed, as recommended in PEP-0391 for configuring logging.
    """

    @staticmethod
    def initialize(
            project_name: str = "genaimatcher",
            job_id: Optional[str] = None,
            job_run_id: Optional[str] = None,
            job_name: Optional[str] = None,
            task_key: Optional[str] = None,
            workspace_url: Optional[str] = None,
    ) -> LoggerAdapter:

        from genaimatcher.utils.log.config.dict_config import LOGGING
        logging.config.dictConfig(LOGGING)

        if job_run_id is not None:
            context = {
                "job_id": job_id,
                "job_run_id": job_run_id,
                "job_name": job_name,
                "task_key": task_key,
                "workspace_url": workspace_url,
            }
        else:

            from genaimatcher.utils.databricks.functions import get_databricks_job_and_run_id
            job_id, job_run_id, job_name, task_key, workspace_url = get_databricks_job_and_run_id()
            context = {
                "job_id": job_id,
                "job_run_id": job_run_id,
                "job_name": job_name,
                "task_key": task_key,
                "workspace_url": workspace_url
            }

        return ContextualLoggerAdapter(logging.getLogger(project_name), extra=context)
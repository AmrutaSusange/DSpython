import asyncio
import time
from typing import Callable, Dict, Any
from pyspark import Row
from pyspark.sql import SparkSession
from genaimatcher.utils.log.logger import Logger
from functools import wraps
import os
import inspect
import logging


def get_indentation():
    """
    Calculates the depth of the current call stack for determining indentation.
    Adjusts to ensure no indentation for the root-level logs.
    """
    # Stack depth minus the decorator's own stack overhead
    depth = len(inspect.stack()) - 1  # Subtract decorator overhead
    return max(0, depth - 2)

def log_method_calls(cls):
    """
    Class decorator to automatically log the start, completion, and errors
    of all public methods in a class. Skips special methods (e.g., dunder methods)
    and respects pytest environments to avoid unnecessary logging during tests.

    :param cls: The class whose methods will be decorated for logging.
    :type cls: class

    :return: decorated class
    """

    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value) and not attr_name.startswith("__"):
            setattr(cls, attr_name, _log_wrapper_with_module(cls, attr_name, attr_value))
    return cls

def _log_wrapper_with_module(cls, method_name, method):
    """
    Internal helper to wrap a method with logging for start, completion, and error states.
    Logging is skipped when running under pytest. replace: depth = "  " * get_indentation()

    :param cls: The class to which the method belongs.
    :type cls: cls
    :param method_name: The name of the method being wrapped.
    :type method_name: str
    :param method: The original method to be wrapped.
    :type method: Callable

    :return: wrapped method
    :type: Callable
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):

        depth = ""
        if os.getenv("PYTEST_CURRENT_TEST"):
            return method(self, *args, **kwargs)

        logger = Logger().initialize()
        method_signature = f"{cls.__module__}.{cls.__name__}.{method_name}"

        log_message = f"Started - {method_signature} "

        logger.debug(log_message)

        try:
            result = method(self, *args, **kwargs)
            logger.debug(f"{depth}Completed - {method_signature}")
            return result
        except Exception as e:
            if os.getenv("PYTEST_CURRENT_TEST"):
                raise
            logger.error(f"{depth}Error in: {method_signature} - {e}", exc_info=True)
            raise
    return wrapper


def log_function_calls(log_level="INFO"):
    """
    Decorator to log function calls (not methods). Logs function entry, exit, and exceptions.
    This decorator works for standalone functions only.

    :param log_level: The logging level to use for the log messages. Default is "INFO".
    :type log_level: str
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if os.getenv("PYTEST_CURRENT_TEST"):
                return func(*args, **kwargs)

            method_signature = f"{func.__module__}.{func.__name__}"

            logger = Logger().initialize()

            log_method = getattr(logger, log_level.lower(), logger.info)

            log_message = f"Started - {method_signature}"

            log_method(log_message)

            try:
                result = func(*args, **kwargs)
                log_method(f"Completed - {method_signature}")
                return result
            except Exception as e:
                if os.getenv("PYTEST_CURRENT_TEST"):
                    raise
                logger.error(f"Error in: {method_signature} - {e}", exc_info=True)
                raise

        return wrapper

    return decorator


def convert_conf_into_table(data):
    import pandas as pd

    rows = []

    for key, value in data.items():
        row = {"name": key}
        for sub_key, sub_value in value.items():
            if isinstance(sub_value, dict):
                row[sub_key] = sub_value
        rows.append(row)

    return pd.DataFrame(rows).to_string(index=True)

def log_configuration_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        logger = logging.getLogger(__name__)
        logger.info(f"\n\n----------------module configuration---------------- \n{convert_conf_into_table(args[2])}\n")
        return func(*args, **kwargs)
    return wrapper


from functools import wraps
from typing import Callable, Any

def log_partition_processing(func: Callable) -> Callable:
    """
    A decorator to log partition processing for async row functions.

    :param func: The row processing function to be wrapped
    :return: wrapped function with logging
    """

    @wraps(func)
    async def wrapper(logger, fn, row: Row, partition_index: int, semaphore: asyncio.Semaphore,
                      param: Dict[str, Any], row_index: int, total_rows, total_partitions, rows_in_partition, client) -> Any:

        result = await func(logger, fn, row, partition_index, semaphore, param, row_index, total_rows, total_partitions, rows_in_partition, client)

        progress = ((row_index+1) / rows_in_partition) * 100

        if int(progress) % 5 == 0:
            logger.info(f"[Partition: {partition_index}/{total_partitions}], [Rows: {rows_in_partition}/{total_rows}], [Partition {partition_index} Progress: {round(progress, 2)}%, At {row_index}/{rows_in_partition} row]")

        return result

    return wrapper

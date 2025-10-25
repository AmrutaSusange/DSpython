"""PEP-0391 recommended way of configuring logging"""

from genaimatcher.utils.log.config.filters import NoPasswordFilter, DebugLevelFilter
from genaimatcher.utils.log.config.formatters import TrimmedFormatter
import sys
import os

project_name = 'genaimatcher'
dyntrace_custom_log_handler = 'genaimatcher.utils.log.config.handlers.DynatraceHttpHandler'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        'genaimatcher': {
            'level': 'DEBUG',
            'handlers': ['consoleLogHandler', 'dynatraceLogHandler'],
            'propagate': False
        },
        'genaimatcher-summary': {
            'level': 'DEBUG',
            'handlers': ['consoleLogHandler', 'dynatraceLogHandlerScoringMonitor'],
            'propagate': False
        },
        'test-genaimatcher': {
            'level': 'DEBUG',
            'handlers': ['consoleLogHandler', 'testDynatraceLogHandler'],
            'propagate': False
        },
        'test-genaimatcher-summary': {
            'level': 'DEBUG',
            'handlers': ['consoleLogHandler', 'testDynatraceLogHandlerScoringMonitor'],
            'propagate': False
        },

    },
    'handlers': {
        'consoleLogHandler': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'consoleLogFormatter',
            'stream': sys.stdout,
            # 'filters': ['debug_message_filter']
        },
        'dynatraceLogHandler': {
            'class': dyntrace_custom_log_handler,
            'level': 'DEBUG',
            'formatter': 'trimmedLogFormatter',
            'dynatrace_url': os.getenv("dynatrace_api_url"),
            'api_token': os.getenv("dynatrace_api_token"),
            'source_name_for_dynatrace': 'genaimatcher',
            'verify_ssl': True,
        },
        'dynatraceLogHandlerScoringMonitor': {

            'level': 'DEBUG',
            'formatter': 'trimmedLogFormatter',
            'filters': ['debug_message_filter'],

            'class': dyntrace_custom_log_handler,
            'dynatrace_url': os.getenv("dynatrace_api_url"),
            'api_token': os.getenv("dynatrace_api_token"),
            'source_name_for_dynatrace': 'genaimatcher-summary',
            'verify_ssl': True,
        },
        'testDynatraceLogHandler': {
            'class': dyntrace_custom_log_handler,
            'level': 'DEBUG',
            'formatter': 'trimmedLogFormatter',
            'dynatrace_url': os.getenv("dynatrace_api_url"),
            'api_token': os.getenv("dynatrace_api_token"),
            'source_name_for_dynatrace': 'test-genaimatcher',
            'verify_ssl': True,
        },
        'testDynatraceLogHandlerScoringMonitor': {
            'class': dyntrace_custom_log_handler,
            'level': 'DEBUG',
            'formatter': 'trimmedLogFormatter',
            'dynatrace_url': os.getenv("dynatrace_api_url"),
            'api_token': os.getenv("dynatrace_api_token"),
            'source_name_for_dynatrace': 'test-genaimatcher-summary',
            'verify_ssl': True,
        },

    },
    'formatters': {
        'consoleLogFormatter': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
        'fileLogFormatter': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
        'trimmedLogFormatter': {
            '()': TrimmedFormatter,
            'format': '%(asctime)s %(levelname)s %(name)s %(pathname)s:%(lineno)d %(funcName)s() - %(message)s',
        },
    },
    'filters': {
        'noPasswordFilter': {
            '()': NoPasswordFilter,
        },
        'debug_message_filter': {
            '()': DebugLevelFilter,
        },
    }
}

import logging

logging.config.dictConfig(LOGGING)

logger = logging.getLogger('genaimatcher')

logger.info("....")
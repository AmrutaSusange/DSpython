import logging

class NoPasswordFilter(logging.Filter):
    """Filter out logs containing 'password' in the message."""
    def filter(self, record):
        return "password" not in record.getMessage()

class DebugLevelFilter(logging.Filter):
    """Allow only debug level logs."""
    def filter(self, record):
        return record.levelno == logging.DEBUG
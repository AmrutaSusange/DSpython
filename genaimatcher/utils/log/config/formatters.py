import logging

class TrimmedFormatter(logging.Formatter):
    def format(self, record):
        if isinstance(record.msg, str):
            record.msg = record.msg.strip()

        return super().format(record)

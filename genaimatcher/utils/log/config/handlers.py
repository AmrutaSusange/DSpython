import logging
import requests
import json
from datetime import datetime, timezone

class DynatraceHttpHandler(logging.Handler):

    def __init__(self, dynatrace_url, api_token, source_name_for_dynatrace,
                 verify_ssl=True):

        super().__init__()
        self.dynatrace_url = dynatrace_url.rstrip('/')
        self.api_token = api_token
        self.source_name_for_dynatrace = source_name_for_dynatrace
        self.verify_ssl = verify_ssl

    def emit(self, record):
        try:
            dt = datetime.now(timezone.utc)
            iso_string = dt.replace(microsecond=0).isoformat()

            headers = {
                "Authorization": f"Api-Token {self.api_token}",
                "Content-Type": "application/json; charset=utf-8"
            }

            attributes = {
                "asctime": iso_string,
                "levelname": record.levelname,
                "name": record.name,
                "pathname": record.pathname,
                "lineno": record.lineno,
                "funcName": record.funcName,
                "message": record.getMessage(),
                "exc_info": record.exc_info,
            }


            payload = {
                "log.source": self.source_name_for_dynatrace,
                "loglevel": record.levelname,
                "attributes": attributes
            }

            response = requests.post(
                self.dynatrace_url,
                headers=headers,
                data=json.dumps(payload),
                verify=self.verify_ssl
            )

            if response.status_code != 204:
                print(f"Failed to send log to Dynatrace: {response.status_code} {response.text}")

        except Exception as e:
            print(f"Exception in {self.__class__.__name__}: {e}")
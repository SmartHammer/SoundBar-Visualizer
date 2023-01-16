# This Python file uses the following encoding: utf-8
import logging


class NetworkChecker:
    def __init__(self, timeoutSec: int = 5):
        self._url = "https://www.python.org/"
        self._timeoutSec = timeoutSec

    def check(self):
        result = True
        try:
            request = requests.get(self._url, timeout=self._timeoutSec)
        except (requests.ConnectionError, requests.Timeout) as exception:
            logging.error(exception)
            result = False
        return result

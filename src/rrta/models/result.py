from typing import List, Dict
from requests.structures import CaseInsensitiveDict


class Result:
    def __init__(
        self,
        status_code: int,
        headers: CaseInsensitiveDict,
        message: str = "",
        data: List[Dict] = None,
    ):
        """
        Result returned from low-level RestAdapter
        :param status_code: Standard HTTP Status code
        :param message: Human readable result
        :param data: Python List of Dictionaries (or maybe just a single Dictionary on error)
        """
        self.status_code = int(status_code)
        self.headers = headers
        self.message = str(message)
        self.data = data if data else []

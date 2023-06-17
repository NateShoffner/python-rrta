import aiohttp
import logging
from typing import Dict
from json import JSONDecodeError
from .models.result import Result
from .exceptions import MyStopApiException


class RestAdapter:
    def __init__(
        self,
        session: aiohttp.ClientSession,
        hostname: str = "",
        base: str = "",
        user_agent: str = "",
        ssl_verify: bool = True,
        logger: logging.Logger = None,
    ):
        """
        Constructor for RestAdapter
        :param session: Client session to use for requests
        :param hostname: Hostname of the API server
        :param base (optional): Base URL of the API server
        :param user_agent (optional):  User-Agent string to use when making HTTP requests
        :param ssl_verify: (optional) Verify SSL certificates. Defaults to True.
        :param logger: (optional) If your app has a logger, pass it in here.
        """
        self.session = session
        self._logger = logger or logging.getLogger(__name__)
        self.url = f"https://{hostname}/"

        if base:
            self.url = f"{self.url}{base}/"

        self.user_agent = user_agent
        self._ssl_verify = ssl_verify
        if not ssl_verify:
            self.session.verify_ssl = False

    async def _do(
        self, http_method: str, endpoint: str, ep_params: Dict = None, data: Dict = None
    ) -> Result:
        """
        Private method for get(), post(), delete(), etc. methods
        :param http_method: GET, POST, DELETE, etc.
        :param endpoint: URL Endpoint as a string
        :param ep_params: Dictionary of endpoint parameters (Optional)
        :param data: Dictionary of data to pass in the request (Optional)
        :return: a Result object
        """
        full_url = self.url + endpoint
        headers = {}
        if self.user_agent:
            headers["User-Agent"] = self.user_agent
        log_line_pre = f"method={http_method}, url={full_url}, params={ep_params}"
        log_line_post = ", ".join(
            (log_line_pre, "success={}, status_code={}, message={}")
        )

        try:
            self._logger.debug(msg=log_line_pre)
            response = await self.session.request(
                method=http_method,
                url=full_url,
                verify_ssl=self._ssl_verify,
                headers=headers,
                params=ep_params,
                json=data,
            )
        except aiohttp.ClientError as e:
            self._logger.error(msg=(str(e)))
            raise MyStopApiException("Request failed") from e

        # deserialize
        try:
            data_out = await response.json()
        except (ValueError, TypeError, JSONDecodeError) as e:
            self._logger.error(msg=log_line_post.format(False, None, e))
            raise MyStopApiException("Bad JSON in response") from e

        status_code = response.status
        # If status_code in 200-299 range, return success Result with data, otherwise raise exception
        is_success = 299 >= status_code >= 200  # 200 to 299 is OK
        log_line = log_line_post.format(is_success, status_code, response.reason)
        if is_success:
            self._logger.debug(msg=log_line)
            return Result(
                status_code,
                headers=response.headers,
                message=response.reason,
                data=data_out,
            )
        self._logger.error(msg=log_line)
        raise MyStopApiException(f"{status_code}: {response.reason}")

    async def get(self, endpoint: str, ep_params: Dict = None) -> Result:
        return await self._do(http_method="GET", endpoint=endpoint, ep_params=ep_params)

    async def post(
        self, endpoint: str, ep_params: Dict = None, data: Dict = None
    ) -> Result:
        return await self._do(
            http_method="POST", endpoint=endpoint, ep_params=ep_params, data=data
        )

    async def delete(
        self, endpoint: str, ep_params: Dict = None, data: Dict = None
    ) -> Result:
        return await self._do(
            http_method="DELETE", endpoint=endpoint, ep_params=ep_params, data=data
        )

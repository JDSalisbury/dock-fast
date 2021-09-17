import logging
from fastapi import Request
import random
import string
import time
from starlette.middleware.base import BaseHTTPMiddleware

# logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

logger = logging.getLogger(__name__)


class LogRequests(BaseHTTPMiddleware):
    def __init__(self, app, header_value='HTTP') -> None:
        super().__init__(app)
        self.header_value = header_value

    async def dispatch(self, request: Request, call_next) -> None:
        idem = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=6))
        logger.info(f"rid={idem} start request path={request.url.path}")
        start_time = time.time()

        response = await call_next(request)

        process_time = (time.time() - start_time) * 1000
        formatted_process_time = '{0:.2f}'.format(process_time)
        logger.info(
            f"rid={idem} completed_in={formatted_process_time}ms status_code={response.status_code}")

        print(
            f"rid={idem} completed_in={formatted_process_time}ms status_code={response.status_code}")

        return response

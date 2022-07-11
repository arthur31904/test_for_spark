import requests
from core.logger import Logger, LogLevel
import traceback
from schemas.exception import BizException

class http_requests():
    def get_and_log(self, url):
        try:
            RedisResponseSet = requests.get(url)
            Logger.log(LogLevel.INFO, "get_and_log", url, None, "success")
        except BizException as e:
            tb = traceback.format_exc()
            Logger.log(LogLevel.WARN, "get_and_log", url, e.message, tb)
            raise BizException(
                status_code=500,
                message=str(e.args)
            )
        except Exception as e:
            tb = traceback.format_exc()
            Logger.log(LogLevel.WARN, "get_and_log", url, e, tb)
            raise BizException(
                status_code=500,
                message=str(e.args)
            )

    def post_and_log(self, url, data, headers):
        try:
            check_requests = requests.post(url, json=data, headers=headers)
            Logger.log(LogLevel.INFO, "post_and_log", data, None, "success")
        except BizException as e:
            tb = traceback.format_exc()
            Logger.log(LogLevel.WARN, "post_and_log", data, e.message, tb)
            raise BizException(
                status_code=500,
                message=str(e.args)
            )
        except Exception as e:
            tb = traceback.format_exc()
            Logger.log(LogLevel.WARN, "post_and_log", data, e, tb)
            raise BizException(
                status_code=500,
                message=str(e.args)
            )
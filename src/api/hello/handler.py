import logging

import boto3
import common
import common_db
import constants
from botocore.config import Config
from common_decorators import log_event
from common_exception import CommonException
from common_marshmallow import BaseRequestSchema, BaseResponseSchema, TrimmedField
from marshmallow import fields
from marshmallow.validate import Length, OneOf

LOGGER = logging.getLogger()

DYNAMODB = boto3.resource(
    "dynamodb",
    constants.REGION,
    config=Config(tcp_keepalive=True),
)

{TODO:MODULE_NAME}_HELLO_TABLE = DYNAMODB.Table({TODO:module_name}_constants.{TODO:MODULE_NAME}_HELLO_TABLE_NAME)


class RequestSchema(BaseRequestSchema):
    pass

class ResponseSchema(BaseResponseSchema):
    pass

@log_event
def handler(event, context):
    try:
        req = RequestSchema().load_and_dump(event)

        # TODO: Implement logic

        return common.gen_api_resp(
            code=2000,
            payload=ResponseSchema().load_and_dump({}),
        )

    except CommonException as err:
        return common.gen_api_resp(code=err.code, msg=err.msg)

    except Exception as err:
        LOGGER.exception(err)
        return common.gen_api_resp(code=5000)

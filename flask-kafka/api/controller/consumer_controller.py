from flasgger import swag_from
from flask import request, Blueprint
from marshmallow import ValidationError
from api.domain.consumer import Consumer
from api.util import exception_util, service_util
from api.constant.message_code import MessageCode
from api.schema.consumer_schema import ConsumerSchema
from api.exception.service_exception import ServiceException
from api.business_logic.consumer_service import ConsumerService

consumer = Blueprint('consumer', __name__)

"""
Author          : Neda Peyrone
Create Date     : 30-08-2023
File            : consumer_controller.py
Purpose         : This Python file is responsible for controlling HTTP requests from clients. 
                  It validates and transforms them into consumer instances before passing them 
                  to the consumer service.
"""


@swag_from('../../docs/consume.yml')
@consumer.route("/consume", methods=['POST'])
def consume():
  payload = request.get_json()

  try:
    validated_data = ConsumerSchema().load(payload)
    consumer = Consumer(**validated_data)

    msg = ConsumerService().consume(consumer)
    return service_util.build_server_response(MessageCode.SUCCESS, msg)
  except (ValidationError, ServiceException) as err:
    return exception_util.handler(err)
from flasgger import swag_from
from flask import request, Blueprint
from marshmallow import ValidationError
from api.domain.producer import Producer
from api.constant.message_code import MessageCode
from api.util import exception_util, service_util
from api.schema.producer_schema import ProducerSchema
from api.exception.service_exception import ServiceException
from api.business_logic.producer_service import ProducerService

producer = Blueprint('producer', __name__)

"""
Author          : Neda Peyrone
Create Date     : 30-08-2023
File            : producer_controller.py
Purpose         : This Python file is responsible for controlling HTTP requests from clients. 
                  It validates and transforms them into consumer instances before passing them 
                  to the produce service.
"""


@swag_from('../../docs/produce.yml')
@producer.route("/produce", methods=['POST'])
def consume():
  payload = request.get_json()

  try:
    validated_data = ProducerSchema().load(payload)
    producer = Producer(**validated_data)

    ProducerService().produce(producer)
    return service_util.build_status_response(MessageCode.SUCCESS.name, MessageCode.SUCCESS.value)
  except (ValidationError, ServiceException) as err:
    return exception_util.handler(err)
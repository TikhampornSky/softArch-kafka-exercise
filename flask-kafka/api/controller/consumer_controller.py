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
    topic_names = ["Italian", "Japanese", "Chinese", "Thai", "Indian"]
    group_id_names = ["Kitchen 1", "Kitchen 2", "Kitchen 3", "Kitchen 4"]
    if consumer.topic not in topic_names:
      return exception_util.handler("Topic must be one of the following: Italian, Japanese, Chinese, Thai, Indian")
    if consumer.group_id not in group_id_names:
      return exception_util.handler("Group ID must be one of the following: Kitchen 1, Kitchen 2, Kitchen 3, Kitchen 4")
    if not consumerRules(consumer.group_id, consumer.topic):
      return exception_util.handler("Group ID and Topic do not match")

    msg = ConsumerService().consume(consumer)
    return service_util.build_server_response(MessageCode.SUCCESS, msg)
  except (ValidationError, ServiceException) as err:
    return exception_util.handler(err)
  
def consumerRules(group_id, topic):
  rules = {
    "Kitchen 1": ["Italian"],
    "Kitchen 2": ["Japanese", "Chinese"],
    "Kitchen 3": ["Japanese", "Thai", "Indian"],
    "Kitchen 4": ["Italian", "Japanese", "Chinese", "Thai", "Indian"]
  }

  if topic in rules[group_id]:
    return True
  else:
    return False
from enum import Enum

"""
Author          : Neda Peyrone
Create Date     : 30-08-2023
File            : message_code.py
Purpose         : The MessageCode class encapsulates enums to represent service responses.
"""


class MessageCode(Enum):
  def __str__(self):
    return str(self.value)

  SUCCESS = 'Service Success.'
  ERROR_INVALID_PARAM = 'Invalid parameter.'
  ERROR_KAFKA = 'Invalid Kafka logic.'
  UNKNOWN_ERROR = 'Unknown error.'
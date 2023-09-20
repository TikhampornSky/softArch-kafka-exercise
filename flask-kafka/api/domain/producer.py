from typing import Dict

"""
Author          : Neda Peyrone
Create Date     : 30-08-2023
File            : producer.py
Purpose         : The Producer class contains attributes essential for publishing 
                  a message to a Kafka topic.
"""


class Producer(object):
    topic: str
    message: str
    config: Dict[str, any] = {}

    def __init__(
      self,
      topic=None,
      message=None,
      config=None
    ):
      super(Producer, self).__init__()
      self.topic = topic
      self.message = message
      self.config = config
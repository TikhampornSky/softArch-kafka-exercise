"""
Author          : Neda Peyrone
Create Date     : 30-08-2023
File            : kafka_config.py
Purpose         : The KafkaConfig class encapsulates the necessary parameters for connecting to Apache Kafka.
"""


class KafkaConfig:
    bootstrap_servers: str
    auto_offset_reset: str

    def __init__(self, bootstrap_servers, auto_offset_reset):
      self.bootstrap_servers = bootstrap_servers
      self.auto_offset_reset = auto_offset_reset

    def __repr__(self):
      return "<KafkaConfig(name={self.name!r})>".format(self=self)
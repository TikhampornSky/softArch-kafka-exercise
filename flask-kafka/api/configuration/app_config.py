from api.util.singleton import Singleton

"""
Author          : Neda Peyrone
Create Date     : 30-08-2023
File            : app_config.py
Purpose         : The AppConfig class encapsulates the necessary parameters for the application.
"""


class AppConfig(metaclass=Singleton):

  def __init__(self, params):
    self.params = params
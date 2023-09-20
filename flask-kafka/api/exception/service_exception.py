"""
Author          : Neda Peyrone
Create Date     : 30-08-2023
File            : service_exception.py
Purpose         : -
"""

class ServiceException(Exception):
  def __init__(self, msg):
    self.msg = msg

  def __str__(self):
    return repr(self.msg)
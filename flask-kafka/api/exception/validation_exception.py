"""
Author          : Neda Peyrone
Create Date     : 30-08-2023
File            : validation_exception.py
Purpose         : -
"""

class ValidationException(Exception):
  def __init__(self, msg):
    self.msg = msg

  def __str__(self):
    return repr(self.msg)
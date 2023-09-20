import json
import enum
from datetime import date
from datetime import time
from datetime import datetime

"""
Author          : Neda Peyrone
Create Date     : 30-08-2023
File            : json_util.py
Purpose         : This Python file contains utilities for serializing and converting to JSON format.
"""


def to_serializable(val):
  """JSON serializer for objects not serializable by default"""
  
  if isinstance(val, (datetime, date, time)):
    return val.isoformat()
  elif isinstance(val, enum.Enum):
    return val.value
  elif hasattr(val, '__dict__'):
    return val.__dict__


def to_json(data):
  """Converts object to JSON formatted string"""
  return json.dumps(data, default=to_serializable)
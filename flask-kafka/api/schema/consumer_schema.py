from marshmallow import Schema, fields

"""
Author          : Neda Peyrone
Create Date     : 30-08-2023
File            : consumer_schema.py
Purpose         : The ConsumerSchema class uses the Marshmallow library to 
                  validate and transform an HTTP request into a consumer instance.
"""


class ConsumerSchema(Schema):
  group_id = fields.Str(required=True)
  topic = fields.Str(required=True)
  config = fields.Dict()

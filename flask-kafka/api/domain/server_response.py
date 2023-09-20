from api.domain.status_response import StatusResponse

"""
Author          : Neda Peyrone
Create Date     : 30-08-2023
File            : server_response.py
Purpose         : The ServerReponse class contains attributes essential for service responses.
"""


class ServerReponse(object):
  statusResponse: StatusResponse
  body: any

  def __init__(self, statusResponse, body):
    self.statusResponse = statusResponse
    self.body = body
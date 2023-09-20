import sys
from flask import Flask
from pathlib import Path
from flasgger import Swagger
from api.bootstrap import Bootstrap

from api.controller.consumer_controller import consumer
from api.controller.producer_controller import producer

"""
Author          : Neda Peyrone
Create Date     : 30-08-2023
File            : app.py
Purpose         : This Python file is used to establish a Flask application instance.
"""


def create_app():
  path = Path().absolute()
  Bootstrap(path)

  app = Flask(__name__)

  template = {
    "swagger": "2.0",
    "info": {
      "title": "Flask Kafka API",
      "description": "This API was developed using Python Flask, which provides an interface for producing and consuming messages with Apache Kafka topics via HTTP endpoints.",
      "version": "1.0"
    }
  }
  app.config['SWAGGER'] = {
    'title': 'Flask Kafka API',
    'uiversion': 2,
    'template': './resources/flasgger/swagger_ui.html'
  }
  Swagger(app, template=template)

  app.register_blueprint(consumer)
  app.register_blueprint(producer)

  return app


if __name__ == '__main__':
  try:
    port = int(sys.argv[1])
  except Exception:
    port = 8081

  create_app().run(host='0.0.0.0', port=port, debug=True, use_reloader=True)
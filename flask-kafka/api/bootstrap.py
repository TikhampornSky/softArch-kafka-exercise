from api.util.file_util import read_yaml_file
from api.configuration.app_config import AppConfig

"""
Author          : Neda Peyrone
Create Date     : 30-08-2023
File            : bootstrap.py
Purpose         : The Bootstrap class facilitates loading requisite parameters 
                  from the YAML file configuration into its instance.
"""


class Bootstrap:

  def __init__(self, path) -> None:
    self.path = path
    self.load_app_config()

  def load_app_config(self):
    d = read_yaml_file(f"{self.path}/resources/config.yaml")
    cfg = AppConfig(d)
    print(f"O:--Load App Config--:bootstrap_servers/{cfg.params['kafka']['bootstrap_servers']}")
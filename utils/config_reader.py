import configparser
import os

class ConfigReader:
    _config = None

    @classmethod
    def load_config(cls):
        if cls._config is None:
            cls._config = configparser.ConfigParser()
            root_dir = os.path.dirname(os.path.dirname(__file__))
            cls._config.read(os.path.join(root_dir, 'config.ini'))

    @classmethod
    def get(cls, section, key):
        cls.load_config()
        return cls._config.get(section, key)
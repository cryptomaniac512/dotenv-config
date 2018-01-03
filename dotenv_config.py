import os

from dotenv import load_dotenv


class ConfigValueNotFound(Exception):
    pass


class Config:

    conversion = {
        bool: lambda v: bool(int(v)),
    }

    def __init__(self, path='.env'):
        load_dotenv(path)

    def __call__(self, name, conversion=str, default=None):
        value = os.environ.get(name, None)
        if not value:
            if not default:
                raise ConfigValueNotFound(
                    f'"{name}" not found in your configuration.')
            else:
                return default

        converter = self.conversion.get(conversion, conversion)
        return converter(value)

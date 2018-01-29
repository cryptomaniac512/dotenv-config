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

    def __call__(self, name, conversion=str, **kwargs):
        value = os.environ.get(name, None)
        if not value:
            if 'default' not in kwargs:
                raise ConfigValueNotFound(
                    f'"{name}" not found in your configuration.')
            else:
                return kwargs['default']

        converter = self.conversion.get(conversion, conversion)
        return converter(value)

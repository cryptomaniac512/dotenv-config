Dotenv config
===
Simple `.env` config loader with type casting.

[![Build Status](https://travis-ci.org/sivakov512/dotenv-config.svg?branch=master)](https://travis-ci.org/sivakov512/dotenv-config)
[![Coverage Status](https://coveralls.io/repos/github/sivakov512/dotenv-config/badge.svg?branch=master)](https://coveralls.io/github/sivakov512/dotenv-config?branch=master)
![Python versions](https://img.shields.io/badge/python-3.6-blue.svg)
[![PyPi](https://img.shields.io/badge/PyPi-0.1.2-yellow.svg)](https://pypi.python.org/pypi/dotenv-config)

Installation
---

``` shell
pip3 install dotenv-config  # or pip if python3 is your default interpreter
```

Usage
---
All you need is instantiate the `Config` class. As an optional argument you can specify the path to your config file, by default this is `.env`

``` python
from dotenv_config import Config

config = Config('.env-test')
```

To read the configuration, call the `Config` instance. By default the returned value is a string.

``` python
some_str_option = config('SOME_OPTION_FROM_YOUR_ENV_FILE_OR_ENVIRONMENT')  # str
```

To cast a type, any callable object can be passed as second argument or `conversion`.
As an argument, it must accept the value read from the config and return the result of type casting.
For example, if you have `SOME_INT=123` in your `.env` and need to load it as `int`, call `config` like this:

``` python
int_option = config('SOME_INT', int)
# or
int_option = config('SOME_INT', conversion=int)
```

You can perform a cast to boolean if the option is specified in the config as `0` or `1`.
For example, if you have a `TRUE_OPTION=1` and `FALSE_OPTION=0`:

``` python
true_option = config('TRUE_OPTION', bool)  # True
false_option = config('FALSE_OPTION', bool)  # false
```

Also, you can specify a default value for situations when the requested option may not be:

``` python
some_value = config('SOME_VALUE', default='my english is bad')
```

If the requested option does not exist and the default value is not specified, an `ConfigValueNotFound` exception will be raised.


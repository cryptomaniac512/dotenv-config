Dotenv config
===
Simple `.env` config loader with the possibility of casting types

[![Build Status](https://travis-ci.org/cryptomaniac512/dotenv-config.svg?branch=master)](https://travis-ci.org/cryptomaniac512/dotenv-config)
[![Coverage Status](https://coveralls.io/repos/github/cryptomaniac512/dotenv-config/badge.svg?branch=master)](https://coveralls.io/github/cryptomaniac512/dotenv-config?branch=master)
![Python versions](https://img.shields.io/badge/python-3.6-blue.svg)
[![PyPi](https://img.shields.io/badge/PyPi-0.0.1-yellow.svg)](https://pypi.python.org/pypi/dotenv-config)

Installation
---

``` shell
pip3 install dotenv-config  # or pip if python3 is your default interpreter
```

Usage
---
All you need is instantiate `Config` class. By default it will look for `.env` file at place where it was called.
You can specify your `.env` locations like this:

``` python
from dotenv_config import Config

config = Config('.env-test')
```

Load configration option with call of `config`. By default loaded options is strings:

``` python
some_str_option = config('SOME_OPTION_FROM_YOUR_ENV_FILE_OR_ENVIRONMENT')  # str
```

You can pass any callable to convert loaded value. For example, if you has `SOME_INT=123` in your `.env` and need to load it as `int`, call `config` like this:

``` python
int_option = config('SOME_INT', int)
# or
int_option = config('SOME_INT', conversion=int)
```

You can load your options as booleans if you define them as `0` or `1`. For example you have a `TRUE_OPTION=1` and `FALSE_OPTION=0`:

``` python
true_option = config('TRUE_OPTION', bool)  # True
false_option = config('FALSE_OPTION', bool)  # false
```

Also you can pass default value for situations when required options may not exists:

``` python
some_value = config('SOME_VALUE', default='my english is bad')
```

If options does not exists and you does not provide default value config will raise `ConfigValueNotFound` exception.


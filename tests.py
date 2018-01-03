import os
import shutil

import pytest

from dotenv_config import Config, ConfigValueNotFound

CONFIG_NAME = '.env'
CONFIG_CONTENT = (
    'MUST_BE_INT=12345',
    'MUST_BE_TRUE=1',
    'MUST_BE_FALSE=0',
    'MUST_BE_STRING=Awesome string',
)


@pytest.fixture()
def config(tmpdir):
    config_path = os.path.join(tmpdir, CONFIG_NAME)

    lines = map(lambda x: f'{x}\n', CONFIG_CONTENT)
    with open(config_path, 'w') as cf:
        cf.writelines(lines)

    config = Config(config_path)
    yield config

    shutil.rmtree(tmpdir, ignore_errors=True)


@pytest.mark.parametrize('value, conversion, expected', (
    ('MUST_BE_INT', int, 12345),
    ('MUST_BE_TRUE', bool, True),
    ('MUST_BE_FALSE', bool, False),
    ('MUST_BE_STRING', str, 'Awesome string'),
))
def test_load(value, conversion, expected, config):
    assert config(value, conversion) == expected


@pytest.mark.parametrize('value, expected', (
    ('MUST_BE_INT', '12345'),
    ('MUST_BE_TRUE', '1'),
    ('MUST_BE_FALSE', '0'),
    ('MUST_BE_STRING', 'Awesome string'),
))
def test_load_as_sring_by_default(value, expected, config):
    assert config(value) == expected


def test_uses_default_if_nothing_provided(config):
    assert config(
        'LolKekMakarek', default='Default string') == 'Default string'


def test_raises_if_not_found_and_no_default(config):
    with pytest.raises(
            ConfigValueNotFound,
            message='"Lol Kek" not found in your configuration.'):
        config('Lol Kek')

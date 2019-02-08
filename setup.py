import os

from setuptools import setup


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as _f:
        return _f.read()


setup(
    author="Nikita Sivakov",
    author_email="sivakov512@gmail.com",
    description="Simple dotenv loader with the possibility of casting types",
    install_requires=['python-dotenv'],
    keywords="dotenv config env types cast",
    license="MIT",
    long_description=read("README.md"),
    name="dotenv-config",
    py_modules=['dotenv_config'],
    python_requires='>=3.6',
    url="https://github.com/sivakov512/dotenv-config",
    version="0.1.3",
)

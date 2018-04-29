from setuptools import setup

setup(
    author="Nikita Sivakov",
    author_email="sivakov512@gmail.com",
    description="Simple dotenv loader with the possibility of casting types",
    install_requires=['python-dotenv'],
    keywords="dotenv config env types cast",
    license="MIT",
    long_description_markdown_filename='README.md',
    name="dotenv-config",
    py_modules=['dotenv_config'],
    python_requires='>=3.6',
    setup_requires=['setuptools-markdown'],
    url="https://github.com/sivakov512/dotenv-config",
    version="0.1.2",
)

"""
      configure the library to be installed
"""

from setuptools import find_packages, setup

setup(
    name="lib_formatter_logger",
    version="1.1.0",
    description="Formatter Logger libraries",
    url="",
    author="Erick Henrique",
    author_email="ericles.system@gmail.com",
    license="Public",
    install_requires=["jsonschema==2.6.0"],
    packages=find_packages(),
    zip_safe=False,
)

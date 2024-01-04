"""
Setup script for the owmTestTask package.

This script uses setuptools to define the package metadata, dependencies, and other configuration.

Attributes:
    name (str): The name of the package.
    version (str): The version of the package.
    packages (List[str]): A list of all Python packages to include.
    install_requires (List[str]): A list of dependencies required for the package.

Example:
    To install the package along with its dependencies, use the following command:
        $ pip install .
"""

from setuptools import find_packages, setup

setup(
    name='owmTestTask',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)

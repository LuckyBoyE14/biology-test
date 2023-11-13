from setuptools import setup, find_packages

setup(
    name='biology-test',
    version='0.1.0',
    packages=find_packages(include=['biology_test', 'biology_test.*'])
)

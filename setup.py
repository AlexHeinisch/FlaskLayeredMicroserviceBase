from setuptools import setup, find_packages

setup(
    name='application',
    version='0.1',
    packages=find_packages(include=['application', 'application.*'])
)

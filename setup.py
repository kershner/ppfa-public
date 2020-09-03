#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name='ppfa-takehome',
    version='1.0',
    description='PPFA Take Home Assignment',
    long_description='',
    author='Philip Kalinsky',
    author_email='philip.kalinsky@ppfa.org',
    url='https://github.com/ppfa/backend-takehome-assignment/',
    packages=find_packages(),
    scripts=[
        'scripts/manage.py'
    ],
    package_data={
        'pp': ['templates/*.*'],
    },
    include_package_data=True,
    install_requires=[
        # Requirements need to be installed separately using pip.
        # Refer the docs.
    ],
)

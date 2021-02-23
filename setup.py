#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from os import path
from setuptools import setup, find_packages

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='datetimeLib',
    version='1.0',
    author='GeekDot',
    author_email='zhang.yi10@21vianet.com',
    description='datetimeLib',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=['arrow'],
    project_urls={
        'Source': 'https://github.com/GeekDot/datetimeLib',
    },
)

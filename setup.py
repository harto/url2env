#!/usr/bin/env python

from os import popen
from setuptools import setup, find_packages
import re

package = 'url2env'

version = popen('git describe --tags').read().strip()
if not re.match(r'^\d+\.\d+(\.\d+)?$', version):
    raise Exception('unexpected version: %s' % version)

with open('README.rst') as f:
    long_description = f.read()

setup(
    name=package,
    version=version,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'url2env = url2env:main'
        ],
    },

    description='Produces env vars from Heroku-style database URLs',
    long_description=long_description,
    license='MIT',
    keywords='heroku postgresql shell',
    author='Stuart Campbell',
    author_email='stuart@harto.org',
    url='https://github.com/harto/url2env',
)

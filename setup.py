#!/usr/bin/env python3

from setuptools import setup, find_packages

package = 'url2env'
version = '1.0'
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

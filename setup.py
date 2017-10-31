#!/usr/bin/env python3

from setuptools import setup, find_packages


setup(
    name="mod",
    author="yoeo",
    version="0.1",
    url="https://github.deezerdev.com/ysomda/mod",
    license="MIT",
    description="Mod arithmetics with integers in Python",
    tests_require='pytest',
    packages=find_packages(exclude=['tests']),
    setup_requires=['pytest-runner'],
)

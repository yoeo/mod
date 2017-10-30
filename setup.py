#!/usr/bin/env python3

from pathlib import Path

from setuptools import setup, find_packages


setup(
    name="modulint",
    author="yoeo",
    version="0.1",
    url="https://github.deezerdev.com/ysomda/modulint",
    license="MIT",
    description="Modular arithmetics with integers in Python",
    install_requires=Path('requirements.txt').read_text(),
    tests_require='pytest',
    packages=find_packages(exclude=['tests']),
    setup_requires=['pytest-runner'],
)

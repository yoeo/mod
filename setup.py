#!/usr/bin/env python3
"""
* Install with pip (recommended):
    pip3 install .

* Install with setuptools:
    python setup.py install

* Run tests:
    python setup.py pytest

* Build documentation:
    pip install -r requirements-doc.txt
    cd docs/
    make clean html
"""

from pathlib import Path
from setuptools import setup

import mod


def long_description():
    banned = ('.. toctree', '.. autoclass', '* :ref:', '.. image:: _static/')
    comment = '.. '

    text = Path(__file__).parent.joinpath('docs', 'index.rst').read_text()
    for word in banned:
        text = text.replace(word, comment)

    return text


setup(
    # Package info
    name="mod",
    author="Y. SOMDA",
    version=mod.__version__,
    url="https://github.com/yoeo/mod",
    description="Modular arithmetic in Python",
    long_description=long_description(),
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    # Install setup
    python_requires='>=3',
    platforms='any',
    py_modules=['mod'],
    zip_safe=True,
    # Test setup
    setup_requires=['pytest-runner'],
    tests_require='pytest',
)

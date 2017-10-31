# modulint [![Build Status](https://travis-ci.org/yoeo/modulint.svg?branch=master)](https://travis-ci.org/yoeo/modulint) [![Documentation Status](https://readthedocs.org/projects/modulint/badge/?version=latest)](http://modulint.readthedocs.io/en/latest/?badge=latest)

``modulint`` implements modular arithmetic in Python3.

Modular arithmetic is arithmetic using the modulo operation, ex:

```text
(1 + 0) % 3 = 1
(1 + 1) % 3 = 2
(1 + 2) % 3 = 0
(1 + 3) % 3 = 1
```

Modular arithmetic is used in many fields like music (octaves),
banking (IBAN error check), book publishing (ISBN checksum),
cryptography (RSA, DSA algorithms)
and of course... math.

## Install

```bash
pip3 install .
```

## Usage

```python
>>> from modulint import Modular
>>> x = Modular(3, 7)
>>> x
3
>>> x + 3
6
>>> x + 4  # (3 + 4) % 7
0
>>> x * 4  # (3 * 4) % 7
5
>>> x / 2  # (3 + k*7) / 2 ==> (3 + 1*7) / 2 ==> 10 / 2
5
>>> x**2
2
```

# License

modulint — Copyright (c) 2017 Y. SOMDA, [MIT License](LICENSE)

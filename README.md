# mod [![Build Status](https://travis-ci.org/yoeo/mod.svg?branch=master)](https://travis-ci.org/yoeo/mod) [![Documentation Status](https://readthedocs.org/projects/mod/badge/?version=latest)](http://mod.readthedocs.io/en/latest/?badge=latest)

``mod`` implements modular arithmetic in Python3.

Mod arithmetic is arithmetic using the modulo operation, ex:

```text
(1 + 0) % 3 = 1
(1 + 1) % 3 = 2
(1 + 2) % 3 = 0
(1 + 3) % 3 = 1
```

Mod arithmetic is used in many fields like music (octaves),
banking (IBAN error check), book publishing (ISBN checksum),
cryptography (RSA, DSA algorithms)
and of course... math.

## Install

```bash
pip3 install .
```

## Usage

```python
>>> from mod import Mod
>>> x = Mod(3, 7)
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

mod — Copyright (c) 2017 Y. SOMDA, [MIT License](LICENSE)

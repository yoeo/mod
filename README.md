# modulint

Modular arithmetics with integers in Python

## Install

```bash
pip3 install .
```

## Usage

```python
>>> from modulint import IntMod
>>> x = IntMod(3, 7)
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

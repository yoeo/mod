.. toctree::
   :maxdepth: 2
   :caption: Contents:

**mod** -- modular arithmetic in Python
=======================================

.. image:: https://travis-ci.org/yoeo/mod.svg?branch=master
  :target: https://github.org/yoeo/mod
  :alt: Build Status

.. image:: https://readthedocs.org/projects/mod/badge/?version=latest
  :target: http://mod.readthedocs.io/en/latest/?badge=latest
  :alt: Documentation Status


Description
-----------

`Modular arithmetic <https://en.wikipedia.org/wiki/Modular_arithmetic>`_
is arithmetic for integers, where numbers wrap around
when reaching a given value called `modulus`.
For example ``6 ≡ 1 (mod 5)``.
Modular arithmetic has several many practical applications including:
`music <https://en.wikipedia.org/wiki/Octave>`_,
`banking <https://en.wikipedia.org/wiki/International_Bank_Account_Number#Check_digits>`_,
`book publishing <https://en.wikipedia.org/wiki/International_Standard_Book_Number#Check_digits>`_,
`cryptography <https://en.wikipedia.org/wiki/RSA_%28cryptosystem%29>`_...
and of course math.

The purpose of this package is to simplify
the use of modular operations in **Python3**.

.. image:: _static/images/mod.png

Install
-------

Run the following command to install `mod` package

.. code-block:: bash

  pip3 install mod

Usage
-----

``mod.Mod`` objects are integer numbers that integrate a modulus
to arithmetic operations ``+ - * // **``:

.. code-block:: python

  from mod import Mod

  # Let's have some fun with math

  x = Mod(5, 7)           # x ≡ 5 (mod 7)

  (x + 2) == 0            # 5 + 2 ≡ 7 ≡ 0 (mod 7)
  (x + 7) == x            # 5 + 7 ≡ 12 ≡ 5 (mod 7)
  (x**3) == (x + 1)       # 5³ ≡ 125 ≡ 6 (mod 7)
  (1 // x) == 3           # 5 × 3 ≡ 15 ≡ 1 (mod 7) ⇒ 5⁻¹ ≡ 3 (mod 7)

A naive implementation of
`RSA encryption algorithm <https://en.wikipedia.org/wiki/RSA_%28cryptosystem%29#Encryption>`_
using ``mod`` package:

.. code-block:: python

  from mod import Mod


  # My RSA keys
  public_key = Mod(3, 61423)
  private_key = Mod(40619, 61423)

  # My very secret message
  top_secret_message = 666

  # RSA encryption
  encrypted = top_secret_message**public_key

  # RSA decryption
  decrypted = encrypted**private_key

  # My secret message have been correctly encrypted and decrypted :-)
  assert decrypted == top_secret_message

.. note::

  * ``Mod`` is based on integer modulo operation ``%``, not ``math.fmod``
  * the result of an operation between a ``Mod`` and an ``int`` is a ``Mod``
  * the result of an operation between a ``Mod`` and a ``float`` is a ``float``

Package documentation ``mod.Mod``
---------------------------------

.. autoclass:: mod.Mod
  :members:

Links
-----

* `mod` package documentation located at http://mod.readthedocs.io/en/latest/
* `mod` Python package available at https://pypi.python.org/pypi/mod
* `mod` source code repository: https://github.com/yoeo/mod

**mod** — Copyright (c) 2017 Y. SOMDA, `MIT License <https://github.com/yoeo/mod/blob/master/LICENSE>`_

Indices
-------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

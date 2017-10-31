``modulint`` documentation
==========================

``modulint`` implements ``modular arithmetic`` in Python3.

``modular arithmetic`` is arithmetic using the modulo operation, ex:

.. code-block:: text

  (1 + 0) % 3 = 1
  (1 + 1) % 3 = 2
  (1 + 2) % 3 = 0
  (1 + 3) % 3 = 1
  ...

``modular arithmetic`` is used in many fields like music (octaves),
banking (IBAN error check), book publishing (ISBN checksum),
cryptography (RSA, DSA algorithms)
and of course... math.

Module usage:

.. code-block:: python

  from modulint import Modular


  number = Modular(7, 9)
  print(number + 3)  # prints: (1 % 9)

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Indices
=======

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

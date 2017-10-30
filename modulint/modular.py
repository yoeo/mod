"""
Modular arithmetics operations.

More details on https://en.wikipedia.org/wiki/Modular_arithmetic

"""

from functools import total_ordering
from numbers import Number


@total_ordering
class Modular:
    """Integer Modulo operations"""

    def __init__(self, value, modulo):
        super().__init__()

        if not isinstance(value, Number):
            raise ValueError("Value is not a number")

        if modulo == 0:
            raise ValueError("Modulo value cannot be zero")
        if not isinstance(modulo, Number):
            raise ValueError("Modulo is not a number")
        if modulo != int(modulo):
            raise ValueError("Modulo is not a 'full' integer value")

        self._modulo = int(modulo)
        self._value = int(value) % self._modulo

    def __repr__(self):
        return '({} % {})'.format(self._value, self._modulo)

    def __int__(self):
        return self._value

    def __hash__(self):
        return hash(self._value)

    @property
    def modulo(self):
        """Value of the modulo"""
        return self._modulo

    def copy(self, modulo=None):
        return Modular(self._value, modulo if modulo else self._modulo)

    # Comparison operators

    def __eq__(self, other):
        if not isinstance(other, Number):
            return False

        if isinstance(other, Modular):
            modulo = min((self._modulo, other._modulo))
        else:
            modulo = self._modulo
        return int(self) % modulo == int(other) % modulo

    def __lt__(self, other):
        if not isinstance(other, Number):
            return False

        if isinstance(other, Modular):
            modulo = min((self._modulo, other._modulo))
        else:
            modulo = self._modulo
        return int(self) % modulo < int(other) % modulo

    # Arithmetic operations

    def __pos__(slef):
        return self.copy()

    def __neg__(self):
        return Modular(-self._value, self._modulo)

    def _convert(self, other):
        if isinstance(other, Modular):
            if other._modulo != self._modulo:
                raise ValueError("Modulo values are different {} != {}".format(
                    self._modulo, other._modulo))
            return other

        if isinstance(other, int):
            return Modular(other, self._modulo)

        return None

    def __add__(self, other):
        converted = self._convert(other)
        if converted is None:
            return (other + self._value) % self._modulo

        return Modular(self._value + converted._value, self._modulo)

    __radd__ = __add__

    def __sub__(self, other):
        converted = self._convert(other)
        if converted is None:
            return (other - self._value) % self._modulo

        return Modular(self._value - converted._value, self._modulo)

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        converted = self._convert(other)
        if converted is None:
            return (other * self._value) % self._modulo

        return Modular(self._value * converted._value, self._modulo)

    __rmul__ = __mul__

    def __truediv__(self, other):
        converted = self._convert(other)
        if converted is not None:
            other = converted._value

        return self._value / other

    def __rtruediv__(self, other):
        converted = self._convert(other)
        if converted is not None:
            other = converted._value

        return other / self._value

    def __floordiv__(self, other):
        return NotImplemented

    def __rfloordiv__(self, other):
        return NotImplemented

    def __pow__(self, other):
        return NotImplemented

    def __rpow__(self, other):
        return NotImplemented


Number.register(Modular)

"""Implements modular arithmetic operations on integers.

See: https://en.wikipedia.org/wiki/Modular_arithmetic

"""

from functools import total_ordering
from numbers import Number


@total_ordering
class Mod:
    """Integer number that automatically adds a modulus
    to arithmetic operations

    ``value`` -- integer value

    ``modulo`` -- modulus associated with the value

    """

    def __init__(self, value, modulo):
        if not isinstance(value, Number):
            raise ValueError("Value is not a number")

        if not isinstance(modulo, Number):
            raise ValueError("Modulo is not a number")

        if modulo == 0:
            raise ValueError("Modulo value cannot be zero")

        if modulo != int(modulo):
            raise ValueError("Modulo is not an integer")

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
        """Returns the modulus value"""
        return self._modulo

    def copy(self, modulo=None):
        """Copy a **Mod** number

        ``modulo`` -- modulus of the new **Mod** number

        """
        return Mod(self._value, modulo if modulo else self._modulo)

    def _extended_gcd(self):
        t_value = 0
        new_t = 1
        r_value = self._modulo
        new_r = self._value
        while True:
            if new_r == 0:
                return [r_value, t_value]
            quotient = r_value // new_r
            t_value, new_t = new_t, t_value - quotient * new_t
            r_value, new_r = new_r, r_value - quotient * new_r

    def inverse(self):
        """Modular inverse of the number.

        **y** is the inverse of **x** with the modulus **n** when:

        .. math::
            y × x ≡ 1 (mod. n)

        """
        r_value, t_value = self._extended_gcd()
        if r_value != 1:
            raise ValueError("the value cannot be inverted")

        value = t_value + (self._modulo if t_value < 0 else 0)
        return Mod(value, self._modulo)

    # Comparison operators

    def __eq__(self, other):
        if not isinstance(other, Number):
            return False

        if isinstance(other, Mod):
            modulo = min((self._modulo, other._modulo))
        else:
            modulo = self._modulo
        return int(self) % modulo == int(other) % modulo

    def __lt__(self, other):
        if not isinstance(other, Number):
            return False

        if isinstance(other, Mod):
            modulo = min((self._modulo, other._modulo))
        else:
            modulo = self._modulo
        return int(self) % modulo < int(other) % modulo

    # Arithmetic operations

    def __pos__(slef):
        return self.copy()

    def __neg__(self):
        return Mod(-self._value, self._modulo)

    def _convert(self, other):
        if isinstance(other, Mod):
            if other._modulo != self._modulo:
                raise ValueError("Modulo values are different {} != {}".format(
                    self._modulo, other._modulo))
            return other

        if isinstance(other, int):
            return Mod(other, self._modulo)

        return None

    def __add__(self, other):
        converted = self._convert(other)
        if converted is None:
            return (other + self._value) % self._modulo

        return Mod(self._value + converted._value, self._modulo)

    __radd__ = __add__

    def __sub__(self, other):
        converted = self._convert(other)
        if converted is None:
            return (other - self._value) % self._modulo

        return Mod(self._value - converted._value, self._modulo)

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        converted = self._convert(other)
        if converted is None:
            return (other * self._value) % self._modulo

        return Mod(self._value * converted._value, self._modulo)

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
        converted = self._convert(other)
        if converted is None:
            return (self._value // other) % self._modulo

        print(self, converted, converted.inverse())
        return self * converted.inverse()

    def __rfloordiv__(self, other):
        converted = self._convert(other)
        if converted is None:
            return (other // self._value) % self._modulo

        return converted * self.inverse()

    def __pow__(self, other):
        converted = self._convert(other)
        if converted is None:
            return pow(self._value, other, self._modulo)

        result = pow(self._value, converted._value, self._modulo)
        return Mod(result, self._modulo)

    def __rpow__(self, other):
        converted = self._convert(other)
        if converted is None:
            return pow(other, self._value, self._modulo)

        result = pow(converted._value, self._value, self._modulo)
        return Mod(result, self._modulo)


Number.register(Mod)

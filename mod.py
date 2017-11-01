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

    ``modulus`` -- modulus associated with the value

    """

    def __init__(self, value, modulus):
        if not isinstance(value, Number):
            raise ValueError("Value is not a number")

        if not isinstance(modulus, Number):
            raise ValueError("Modulus is not a number")

        if modulus == 0:
            raise ValueError("Modulus value cannot be zero")

        if modulus != int(modulus):
            raise ValueError("Modulus is not an integer")

        self._modulus = int(modulus)
        self._value = int(value) % self._modulus

    def __repr__(self):
        return '({} % {})'.format(self._value, self._modulus)

    def __int__(self):
        return self._value

    def __hash__(self):
        return hash(self._value)

    @property
    def modulus(self):
        """Returns the modulus value"""
        return self._modulus

    def copy(self, modulus=None):
        """Copy a **Mod** number

        ``modulus`` -- modulus of the new **Mod** number

        """
        return Mod(self._value, modulus if modulus else self._modulus)

    def _extended_gcd(self):
        t_value = 0
        new_t = 1
        r_value = self._modulus
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

        value = t_value + (self._modulus if t_value < 0 else 0)
        return Mod(value, self._modulus)

    # Comparison operators

    def __eq__(self, other):
        if not isinstance(other, Number):
            return False

        if isinstance(other, Mod):
            modulus = min((self._modulus, other._modulus))
        else:
            modulus = self._modulus
        return int(self) % modulus == int(other) % modulus

    def __lt__(self, other):
        if not isinstance(other, Number):
            return False

        if isinstance(other, Mod):
            modulus = min((self._modulus, other._modulus))
        else:
            modulus = self._modulus
        return int(self) % modulus < int(other) % modulus

    # Arithmetic operations

    def __pos__(slef):
        return self.copy()

    def __neg__(self):
        return Mod(-self._value, self._modulus)

    def _convert(self, other):
        if isinstance(other, Mod):
            if other._modulus != self._modulus:
                raise ValueError("Not same modulus: {} != {}".format(
                    self._modulus, other._modulus))
            return other

        if isinstance(other, int):
            return Mod(other, self._modulus)

        return None

    def __add__(self, other):
        converted = self._convert(other)
        if converted is None:
            return (other + self._value) % self._modulus

        return Mod(self._value + converted._value, self._modulus)

    __radd__ = __add__

    def __sub__(self, other):
        converted = self._convert(other)
        if converted is None:
            return (other - self._value) % self._modulus

        return Mod(self._value - converted._value, self._modulus)

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        converted = self._convert(other)
        if converted is None:
            return (other * self._value) % self._modulus

        return Mod(self._value * converted._value, self._modulus)

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
            return (self._value // other) % self._modulus

        print(self, converted, converted.inverse())
        return self * converted.inverse()

    def __rfloordiv__(self, other):
        converted = self._convert(other)
        if converted is None:
            return (other // self._value) % self._modulus

        return converted * self.inverse()

    def __pow__(self, other):
        converted = self._convert(other)
        if converted is None:
            return pow(self._value, other, self._modulus)

        result = pow(self._value, converted._value, self._modulus)
        return Mod(result, self._modulus)

    def __rpow__(self, other):
        converted = self._convert(other)
        if converted is None:
            return pow(other, self._value, self._modulus)

        result = pow(converted._value, self._value, self._modulus)
        return Mod(result, self._modulus)


Number.register(Mod)

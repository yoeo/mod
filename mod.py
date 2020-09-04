"""Implements modular arithmetic operations on integers.

See: https://en.wikipedia.org/wiki/Modular_arithmetic

"""

from functools import total_ordering
from numbers import Number


__version__ = "0.3.0"


@total_ordering
class Mod:
    """Integer number that automatically adds a modulus
    to arithmetic operations.

    The floor division ``//`` implements the inverse of a multiplication
    with a modulus. Therefore, it should be used with care to avoid errors.

    >>> number = Mod(2, 3)
    >>> number
    (2 % 3)
    >>> quintuple = 5 * number
    >>> quintuple // 5
    (2 % 3)
    >>>

    :param int value: Mod number value
    :param int modulus: modulus associated with the value
    :raises ValueError: one of the parameters is not a number or *modulus* == 0
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
        return "({} % {})".format(self._value, self._modulus)

    def __int__(self):
        return self._value

    def __float__(self):
        return float(self._value)

    def __hash__(self):
        return hash(self._value)

    @property
    def modulus(self):
        """Modulus value

        :rtype: int
        """
        return self._modulus

    def copy(self, modulus=None):
        """Copy the Mod number

        :param int modulus: modulus of the new Mod number
        :rtype: Mod
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

    @property
    def inverse(self):
        """Modular inverse of the number.

        **y** is the inverse of **x** with the modulus **n** when:

        .. math::
            y × x ≡ 1 (mod. n)

        :rtype: Mod
        """
        r_value, t_value = self._extended_gcd()
        if r_value != 1:
            raise ValueError("the value {} cannot be inverted".format(self))

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

    def __pos__(self):
        return self.copy()

    def __neg__(self):
        return Mod(-self._value, self._modulus)

    def _convert(self, other):
        if isinstance(other, Mod):
            if other._modulus != self._modulus:
                raise ValueError(
                    "Not same modulus: {} != {}".format(
                        self._modulus, other._modulus
                    )
                )
            return other

        if isinstance(other, int):
            return Mod(other, self._modulus)

        return None

    def __add__(self, other):
        converted = self._convert(other)
        if converted is None:
            return self._value + other

        return Mod(self._value + converted._value, self._modulus)

    __radd__ = __add__

    def __sub__(self, other):
        converted = self._convert(other)
        if converted is None:
            return self._value - other

        return Mod(self._value - converted._value, self._modulus)

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        converted = self._convert(other)
        if converted is None:
            return self._value * other

        return Mod(self._value * converted._value, self._modulus)

    __rmul__ = __mul__

    def __truediv__(self, other):
        return float(self) / float(other)

    def __rtruediv__(self, other):
        return float(other) / float(self)

    def __floordiv__(self, other):
        converted = self._convert(other)
        if converted is None:
            return self._value // other

        if converted._value == 0:
            raise ZeroDivisionError(
                'integer division by {}'.format(converted)
            )

        inverted = (other * self.inverse)
        return inverted.inverse

    def __rfloordiv__(self, other):
        converted = self._convert(other)
        if converted is None:
            return other // self._value

        return converted * self.inverse

    def __pow__(self, other):
        converted = self._convert(other)
        if converted is None:
            return self._value ** other

        if isinstance(other, Mod):
            result = pow(self._value, other._value, self._modulus)
        else:
            result = pow(self._value, other, self._modulus)

        return Mod(result, self._modulus)

    def __rpow__(self, other):
        converted = self._convert(other)
        if converted is None:
            return pow(other, self._value, self._modulus)

        result = pow(converted._value, self._value, self._modulus)
        return Mod(result, self._modulus)


Number.register(Mod)

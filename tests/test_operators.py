import pytest

from mod import Mod


def test_pos():
    number = Mod(7, 17)
    modified = +number
    assert modified == 7
    assert modified.modulus == 17
    assert modified == number


def test_neg():
    number = Mod(7, 17)
    modified = -number
    assert modified == 10
    assert modified.modulus == 17
    assert modified + number == 0


def test_add():
    number = Mod(7, 17)
    assert number == 7

    modified = number + 7
    assert modified == 14
    assert modified.modulus == 17

    modified = number + 11
    assert modified == 1
    assert modified.modulus == 17

    modified = 7 + number
    assert modified == 14
    assert modified.modulus == 17

    modified = 11 + number
    assert modified == 1
    assert modified.modulus == 17


def test_add_float():
    number = Mod(2, 3)
    modified = number + 2.5
    assert modified == 4.5
    assert isinstance(modified, float)


def test_iadd():
    number = Mod(7, 17)
    assert number == 7

    modified = number
    modified += 7
    assert modified == 14
    assert modified.modulus == 17

    modified = number
    modified += 11
    assert modified == 1
    assert modified.modulus == 17


def test_iadd_float():
    number = Mod(2, 3)
    modified = number
    modified += 2.1
    assert modified == 4.1
    assert isinstance(modified, float)


def test_sub():
    number = Mod(7, 17)
    assert number == 7

    modified = number - 5
    assert modified == 2
    assert modified.modulus == 17

    modified = number - 11
    assert modified == 13
    assert modified.modulus == 17

    modified = 5 - number
    assert modified == 15
    assert modified.modulus == 17

    modified = 11 - number
    assert modified == 4
    assert modified.modulus == 17


def test_sub_float():
    number = Mod(2, 3)
    modified = number - 4.5
    assert modified == -2.5
    assert isinstance(modified, float)


def test_isub():
    number = Mod(7, 17)
    assert number == 7

    modified = number
    modified -= 5
    assert modified == 2
    assert modified.modulus == 17

    modified = number
    modified -= 11
    assert modified == 13
    assert modified.modulus == 17


def test_isub_float():
    number = Mod(2, 3)
    modified = number
    modified -= 4.5
    assert modified == -2.5
    assert isinstance(modified, float)


def test_mul():
    number = Mod(7, 17)
    assert number == 7

    modified = number * 2
    assert modified == 14
    assert modified.modulus == 17

    modified = number * 3
    assert modified == 4
    assert modified.modulus == 17

    modified = 2 * number
    assert modified == 14
    assert modified.modulus == 17

    modified = 3 * number
    assert modified == 4
    assert modified.modulus == 17


def test_mult_float():
    number = Mod(2, 3)
    modified = number * 2.5
    assert modified == 5.0
    assert isinstance(modified, float)


def test_imul():
    number = Mod(7, 17)
    assert number == 7

    modified = number
    modified *= 2
    assert modified == 14
    assert modified.modulus == 17

    modified = number
    modified *= 3
    assert modified == 4
    assert modified.modulus == 17


def test_imult_float():
    number = Mod(2, 3)
    modified = number
    modified *= 2.5
    assert modified == 5.0
    assert isinstance(modified, float)


def test_floordiv():
    number = Mod(7, 17)
    assert number == 7

    modified = number // 6
    assert modified == 4
    assert modified.modulus == 17

    modified = number // 29
    assert modified == 2
    assert modified.modulus == 17

    modified = 14 // number
    assert modified == 2
    assert modified.modulus == 17

    modified = 4 // number
    assert modified == 3
    assert modified.modulus == 17


def test_floordiv_float():
    number = Mod(3, 5)
    modified = number // 1.2
    assert modified == 2.0
    assert isinstance(modified, float)


def test_floordiv_is_reversed_multiplication():
    number = Mod(2, 7)
    assert number == 2

    assert (number * 3) // 3 == number == 2
    assert (number * 8) // 2 == 4 * number == 1

    assert number * 7 == 0
    with pytest.raises(ZeroDivisionError):
        (number * 7) // 7


def test_ifloordiv():
    number = Mod(7, 17)
    assert number == 7

    modified = number
    modified //= 6
    assert modified == 4
    assert modified.modulus == 17

    modified = number
    modified //= 29
    assert modified == 2
    assert modified.modulus == 17


def test_ifloordiv_float():
    number = Mod(3, 5)
    modified = number
    modified //= 1.2
    assert modified == 2.0
    assert isinstance(modified, float)


def test_truediv():
    number = Mod(8, 17)
    assert number == 8

    modified = number / 4
    assert modified == 2.0
    assert isinstance(modified, float)

    modified = number / 5
    assert modified == 1.6
    assert isinstance(modified, float)

    modified = 16 / number
    assert modified == 2.0
    assert isinstance(modified, float)

    modified = 4 / number
    assert modified == 0.5
    assert isinstance(modified, float)

    modified = number / 100
    assert modified == 0.08
    assert isinstance(modified, float)


def test_truediv_float():
    number = Mod(3, 5)
    modified = number
    modified //= 1.5
    assert modified == 2.0
    assert isinstance(modified, float)


def test_itruediv():
    number = Mod(8, 17)
    assert number == 8

    modified = number
    modified /= 4
    assert modified == 2.0
    assert isinstance(modified, float)

    modified = number
    modified /= 5
    assert modified == 1.6
    assert isinstance(modified, float)


def test_itruediv_float():
    number = Mod(3, 5)
    modified = number
    modified /= 1.5
    assert modified == 2.0
    assert isinstance(modified, float)


def test_pow():
    number = Mod(7, 17)
    assert number == 7

    modified = number**2
    assert modified == 15
    assert modified.modulus == 17

    modified = number**3
    assert modified == 3
    assert modified.modulus == 17

    modified = 2**number
    assert modified == 9
    assert modified.modulus == 17

    modified = 4**number
    assert modified == 13
    assert modified.modulus == 17


def test_pow_float():
    number = Mod(3, 5)
    modified = number ** 2.0
    assert modified == 9.0
    assert isinstance(modified, float)


def test_pow_zero():
    number = Mod(2, 2)
    assert number == 0

    modified = number**2
    assert modified == 0
    assert modified.modulus == 2

    modified = number**0
    assert modified == 1
    assert modified.modulus == 2


def test_pow_is_multiple_multiplications():
    number = Mod(2, 3)
    assert number == 2

    modified = number**4
    assert modified == 1
    assert modified.modulus == 3
    assert modified == number * number * number * number


def test_ipow():
    number = Mod(7, 17)
    assert number == 7

    modified = number
    modified **= 2
    assert modified == 15
    assert modified.modulus == 17

    modified = number
    modified **= 3
    assert modified == 3
    assert modified.modulus == 17


def test_ipow_float():
    number = Mod(3, 5)
    modified = number
    modified **= 2.0
    assert modified == 9.0
    assert isinstance(modified, float)


def test_ipow_zero():
    number = Mod(2, 2)
    assert number == 0

    modified = number
    modified **= 2
    assert modified == 0
    assert modified.modulus == 2

    modified **= 0
    assert modified == 1
    assert modified.modulus == 2


def test_ipow_is_multiple_multiplications():
    number = Mod(2, 3)
    assert number == 2

    modified = number
    modified **= 4
    assert modified == 1
    assert modified.modulus == 3
    assert modified == number * number * number * number

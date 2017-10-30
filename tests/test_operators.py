from modulint import Modular


def test_add():
    number = Modular(7, 17)
    assert number == 7

    modified = number + 7
    assert modified == 14
    assert modified.modulo == 17

    modified = number + 11
    assert modified == 1
    assert modified.modulo == 17

    modified = 7 + number
    assert modified == 14
    assert modified.modulo == 17

    modified = 11 + number
    assert modified == 1
    assert modified.modulo == 17


def test_iadd():
    number = Modular(7, 17)
    assert number == 7

    modified = number
    modified += 7
    assert modified == 14
    assert modified.modulo == 17

    modified = number
    modified += 11
    assert modified == 1
    assert modified.modulo == 17


def test_sub():
    number = Modular(7, 17)
    assert number == 7

    modified = number - 5
    assert modified == 2
    assert modified.modulo == 17

    modified = number - 11
    assert modified == 13
    assert modified.modulo == 17

    modified = 5 - number
    assert modified == 15
    assert modified.modulo == 17

    modified = 11 - number
    assert modified == 4
    assert modified.modulo == 17


def test_isub():
    number = Modular(7, 17)
    assert number == 7

    modified = number
    modified -= 5
    assert modified == 2
    assert modified.modulo == 17

    modified = number
    modified -= 11
    assert modified == 13
    assert modified.modulo == 17


def test_mul():
    number = Modular(7, 17)
    assert number == 7

    modified = number * 2
    assert modified == 14
    assert modified.modulo == 17

    modified = number * 3
    assert modified == 4
    assert modified.modulo == 17

    modified = 2 * number
    assert modified == 14
    assert modified.modulo == 17

    modified = 3 * number
    assert modified == 4
    assert modified.modulo == 17


def test_imul():
    number = Modular(7, 17)
    assert number == 7

    modified = number
    modified *= 2
    assert modified == 14
    assert modified.modulo == 17

    modified = number
    modified *= 3
    assert modified == 4
    assert modified.modulo == 17


def test_floordiv():
    number = Modular(7, 17)
    assert number == 7

    modified = number // 6
    assert modified == 4
    assert modified.modulo == 17

    modified = number // 29
    assert modified == 2
    assert modified.modulo == 17

    modified = 14 // number
    assert modified == 2
    assert modified.modulo == 17

    modified = 4 // number
    assert modified == 3
    assert modified.modulo == 17


def test_ifloordiv():
    number = Modular(7, 17)
    assert number == 7

    modified = number
    modified //= 6
    assert modified == 4
    assert modified.modulo == 17

    modified = number
    modified //= 29
    assert modified == 2
    assert modified.modulo == 17


def test_truediv():
    number = Modular(8, 17)
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


def test_itruediv():
    number = Modular(8, 17)
    assert number == 8

    modified = number
    modified /= 4
    assert modified == 2.0
    assert isinstance(modified, float)

    modified = number
    modified /= 5
    assert modified == 1.6
    assert isinstance(modified, float)


def test_pow():
    number = Modular(7, 17)
    assert number == 7

    modified = number**2
    assert modified == 15
    assert modified.modulo == 17

    modified = number**3
    assert modified == 3
    assert modified.modulo == 17

    modified = 2**number
    assert modified == 9
    assert modified.modulo == 17

    modified = 4**number
    assert modified == 13
    assert modified.modulo == 17


def test_ipow():
    number = Modular(7, 17)
    assert number == 7

    modified = number
    modified **= 2
    assert modified == 15
    assert modified.modulo == 17

    modified = number
    modified **= 3
    assert modified == 3
    assert modified.modulo == 17

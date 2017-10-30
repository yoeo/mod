from pytest import raises

from modulint import Modular


def test_new_object():
    number = Modular(7, 17)
    assert int(number) == 7
    assert number.modulo == 17

    with raises(ValueError):
        Modular(15, 0)

    with raises(ValueError):
        Modular(15, 7.5)

    with raises(ValueError):
        Modular('15', 7)

    with raises(TypeError):
        Modular(15)


def test_number():
    number = Modular(7, 17)
    assert int(number) == 7


def test_modulo():
    number = Modular(7, 17)
    assert number.modulo == 17

    with raises(AttributeError):
        number.modulo = 21


def test_copy():
    number = Modular(7, 17)
    assert int(number) == 7
    assert number.modulo == 17

    other = number.copy()
    assert number == other
    assert int(other) == 7
    assert other.modulo == 17

    other = number.copy(modulo=5)
    assert number == other
    assert int(other) == 2
    assert other.modulo == 5


def test_objects_interaction():
    for other in [Modular(12, 17), 12]:
        number = Modular(7, 17) + other
        assert int(number) == 2
        assert number.modulo == 17

        number = other + Modular(7, 17)
        assert int(number) == 2
        assert number.modulo == 17

    number = Modular(7, 17) + 12.5
    assert isinstance(number, float)
    assert number == 2.5

    with raises(ValueError):
        Modular(7, 17) + Modular(12, 19)

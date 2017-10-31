from pytest import raises

from mod import Mod


def test_new_object():
    number = Mod(7, 17)
    assert int(number) == 7
    assert number.modulo == 17

    with raises(ValueError):
        Mod(15, 0)

    with raises(ValueError):
        Mod(15, 7.5)

    with raises(ValueError):
        Mod('15', 7)

    with raises(TypeError):
        Mod(15)


def test_number():
    number = Mod(7, 17)
    assert int(number) == 7


def test_modulo():
    number = Mod(7, 17)
    assert number.modulo == 17

    with raises(AttributeError):
        number.modulo = 21


def test_copy():
    number = Mod(7, 17)
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


def test_inverse():
    number = Mod(7, 17)
    assert int(number) == 7
    assert number.modulo == 17

    other = number.inverse()
    assert int(other) == 5
    assert other.modulo == 17

    product = number * other
    assert int(product) == 1
    assert product.modulo == 17


def test_objects_interaction():
    for other in [Mod(12, 17), 12]:
        number = Mod(7, 17) + other
        assert int(number) == 2
        assert number.modulo == 17

        number = other + Mod(7, 17)
        assert int(number) == 2
        assert number.modulo == 17

    number = Mod(7, 17) + 12.5
    assert isinstance(number, float)
    assert number == 2.5

    with raises(ValueError):
        Mod(7, 17) + Mod(12, 19)

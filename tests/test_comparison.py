from pytest import fixture

from mod import Mod


@fixture
def number():
    return Mod(7, 17)


@fixture
def same_list():
    return [7, 7.0, 24, Mod(7, 17), Mod(24, 17), Mod(2, 5)]


@fixture
def smaller_list():
    return [3, 3.0, 20, Mod(3, 17), Mod(20, 17), Mod(1, 5)]


@fixture
def bigger_list():
    return [8, 8.0, 28, Mod(8, 17), Mod(28, 17), Mod(3, 5)]


def test_eq(number, same_list, smaller_list, bigger_list):
    for other in same_list:
        assert number == other
        assert other == number

    for other in smaller_list + bigger_list:
        assert not number == other
        assert not other == number


def test_ne(number, same_list, smaller_list, bigger_list):
    for other in smaller_list + bigger_list:
        assert number != other
        assert other != number

    for other in same_list:
        assert not number != other
        assert not other != number


def test_lt(number, same_list, smaller_list, bigger_list):
    for other in bigger_list:
        assert number < other

    for other in smaller_list:
        assert other < number

    for other in same_list + smaller_list:
        assert not number < other

    for other in same_list + bigger_list:
        assert not other < number


def test_le(number, same_list, smaller_list, bigger_list):
    for other in same_list + bigger_list:
        assert number <= other

    for other in same_list + smaller_list:
        assert other <= number

    for other in smaller_list:
        assert not number <= other

    for other in bigger_list:
        assert not other <= number


def test_gt(number, same_list, smaller_list, bigger_list):
    for other in smaller_list:
        assert number > other

    for other in bigger_list:
        assert other > number

    for other in same_list + bigger_list:
        assert not number > other

    for other in same_list + smaller_list:
        assert not other > number


def test_ge(number, same_list, smaller_list, bigger_list):
    for other in same_list + smaller_list:
        assert number >= other

    for other in same_list + bigger_list:
        assert other >= number

    for other in bigger_list:
        assert not number >= other

    for other in smaller_list:
        assert not other >= number

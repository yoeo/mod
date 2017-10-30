from pytest import fixture

from modulint import Modular


@fixture
def number():
    return Modular(7, 17)


@fixture
def same_list():
    return [7, 7.0, 24, Modular(7, 17), Modular(24, 17), Modular(2, 5)]


@fixture
def smaller_list():
    return [3, 3.0, 20, Modular(3, 17), Modular(20, 17), Modular(1, 5)]


@fixture
def bigger_list():
    return [8, 8.0, 28, Modular(8, 17), Modular(28, 17), Modular(3, 5)]


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

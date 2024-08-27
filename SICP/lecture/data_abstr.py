from typing import List


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


def pair(x, y):
    """Return a function that represents a pair."""

    def get(index):
        if index == 0:
            return x
        else:
            return y

    return get


def select(p, i):
    """Return the element at index i"""
    return p(i)


def rationals(n: int, d: int) -> List[int]:
    """Return rational number by recieving numerator and denominator"""
    g = gcd(n, d)
    return [n // g, d // g]


def numer(x: List[int]) -> int:
    """Return numerator of rational number x"""
    return x[0]


def denom(x: List[int]) -> int:
    """Return denominator of rational number x"""
    return x[1]


def add_rationals(x: List[int], y: List[int]) -> List[int]:
    """Add two rational numbers"""
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rationals(nx * dy + ny * dx, dx * dy)


def mul_rationals(x: List[int], y: List[int]) -> List[int]:
    """Multiply two rational numbers"""
    return rationals(numer(x) * numer(y), denom(x) * denom(y))

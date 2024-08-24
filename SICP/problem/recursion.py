# 1
def stairs1(n: int) -> int:
    """Return the number of ways to take n steps, given that at each step
    , you can choose to take 1, 2, or 3 steps

    >>> stairs1(5)
    13
    >>> stairs1(10)
    274
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return stairs1(n - 1) + stairs1(n - 2) + stairs1(n - 3)


# 2
def stairs2(n: int, k: int) -> int:
    """Return the number of ways to take n steps, at each steps
        are 1, 2, ... , k - 1 or k steps

    >>> stairs2(5, 2)
    8
    >>> stairs2(5, 5)
    16
    >>> stairs2(10, 5)
    464
    """
    if n == 0:
        return 1
    if n < 0:
        return 0
    else:
        return sum([stairs2(n - i, k) for i in range(1, k + 1)])


# 3
"""I couldn't solve this at all"""


# 4

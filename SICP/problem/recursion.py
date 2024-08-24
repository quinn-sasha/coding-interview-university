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
def permutation(lst):
    """Lists all permutation of the given list.

    >>> permutation(['angie', 'cat'])
    [['angie', 'cat'], ['cat', 'angie']]
    >>> permutation([1, 2, 3])
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    if len(lst) <= 1:
        return [lst]
    total = []
    for i, val in enumerate(lst):
        total.extend([[val] + p for p in permutation(lst[:i] + lst[i + 1:])])
    return total

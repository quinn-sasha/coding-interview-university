from operator import mul, add
from typing import Callable, Iterable, List


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


def devisors(n):
    return [1] + [x for x in range(2, n) if n % x == 0]


# aggregation


def perfect_numbers(max: int) -> Iterable[int]:
    """Compute perfect numbers from 1 to n, which is given integer"""
    return [x for x in range(max) if sum(devisors(x)) == x]


def width(area: int, height: int) -> int:
    assert area % height == 0
    return area // height


def permiter(width: int, height: int) -> int:
    """Return permiter of rectangle"""
    return 2 * (width + height)


def minimum_permiter(area: int) -> int:
    """Return minimum permiter of given area's rectangle"""
    heights = devisors(area)
    permiters = [permiter(width(area, h), h) for h in heights]
    return min(permiters)


def reduce(reduce_fn: Callable, s: Iterable, initial: int):
    """Reduce callable into one aggreagated value"""
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced


assert reduce(mul, [1, 2, 3, 4], 1) == 24


def keep_if(filter_fn, s):
    return [x for x in s if filter_fn(x)]


def devisors_of(n: int) -> Iterable[int]:
    """Return all devisors of integer n"""

    def devisors(x):
        return n % x == 0

    return [1] + keep_if(devisors, range(2, n))


def sum_of_devisors(n: int) -> int:
    """Return sum of devisors of integer n"""
    return reduce(add, devisors_of(n), 0)


def perfect_nums(n: int) -> Iterable[int]:
    """Compute perfect numbers from 1 to n, which is given integer"""

    def is_perfect(x):
        return x == sum_of_devisors(x)

    return keep_if(is_perfect, range(1, n))


def tree(root_label, branches=[]):
    """data abstracton for tree"""
    for branch in branches:
        assert is_tree(branch), "Branches must be tree"
    return [root_label] + list(branches)


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    if not isinstance(tree, list) or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    return not branches(tree)


def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])


def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        count = [count_leaves(b) for b in branches(tree)]
        return sum(count)


def partition_tree(n, m):
    """Return partiton tree using the size up to m"""
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n - m, m)
        right = partition_tree(n, m - 1)
        return tree(m, [left, right])


def print_parts(tree, partition=[]):
    """Print all parts of partition tree"""
    if is_leaf(tree):
        if label(tree):
            print("+".join(partition))
    else:
        left, right = branches(tree)
        m = str(label(tree))
        print_parts(left, partition + [m])
        print_parts(right, partition)


def right_binary(tree):
    """Construct right balancing tree"""
    if is_leaf(tree):
        return tree
    if len(tree) > 2:
        tree = [tree[0], tree[1:]]
    return [right_binary(b) for b in tree]

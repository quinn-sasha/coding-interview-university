# Discussion 1


from operator import mul, add, sub, truediv


def race(x, y):
    """The tortoise always walks x feet per minute, while the hare repeatedly
    runs y feet per minute for 5 minutes, then rests for 5 minutes. Return how
    many minutes pass until the tortoise first catches up to the hare.

    >>> race(5, 7)  # After 7 minutes, both have gone 35 steps
    7
    >>> race(2, 4) # After 10 minutes, both have gone 20 steps
    10
    """
    assert y > x and y <= 2 * x, 'the hare must be fast but not too fast'
    tortoise, hare, minutes = 0, 0, 0
    while minutes == 0 or tortoise - hare:
        tortoise += x
        if minutes % 10 < 5:
            hare += y
        minutes += 1
    return minutes


def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """
    i = 1
    while i <= n:
        if (i % 3 == 0) and (i % 5 == 0):
            print("fizzbuzz")
        elif (i % 3 == 0):
            print("fizz")
        elif (i % 5 == 0):
            print("buzz")
        else:
            print(i)
        i += 1


def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    if n == 1:
        return False
    else:
        i = 2
        while i < n:
            if n % i == 0:
                return False
            i += 1
        return True


def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    unique_count = 0
    non_unique = []
    while n > 0:
        digit = n % 10
        n = n // 10
        if digit not in non_unique:
            unique_count += 1
        if has_digit(n, digit):
            non_unique.append(digit)
    print(unique_count)


def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    if (n // 10) == 0:
        return n == k
    else:
        while n > 0:
            digit = n % 10
            if digit == k:
                return True
            n = n // 10
        return False


def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False

    """
    if x <= 0:
        return False
    while (x // 10):
        left = x % 10
        right = (x // 10) % 10
        if left < right:
            return False
        x = x // 10
    return True

# Homework1
# Q3


def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    assert n > 1, "input integer should be greater than 1"
    factor = n - 1
    while factor > 0:
        if n % factor == 0:
            return factor
        factor -= 1


def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    step = 1
    while n > 1:
        print(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        step += 1
    if n == 1:
        print(n)
    return step


# absSICP.pdf

# function as arguments
def evaluator(polynominal, xs=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    return [(x, polynominal(x)) for x in xs]


# nested definition
def selection_sort(lst):
    """Sort a list by picking up minimum value and
       exchange it as front value in list

    >>> selection_sort([64, 25, 12, 22, 11])
    [11, 12, 22, 25, 64]
    """

    def min_index(lst, start):
        """return minimum value of index from start index in list"""

        assert 0 <= start < len(lst), 'Invalid index assigned'
        i, min, index = start, lst[start], start
        while i < len(lst):
            if lst[i] < min:
                min, index = lst[i], i
            i = i + 1
        return index
    for j in range(len(lst)):
        k = min_index(lst, j)
        lst[j], lst[k] = lst[k], lst[j]
    return lst


# function as return value
def deg5poly(a, b, c, d, e, f):
    """Return a polynominal as funciton with parameter x"""

    return lambda x: a * x**5 + b * x**4 + c * x**3 + d * x**2 + e * x + f


# 1.2 Problem-----------------------------------------------

# 1
def reverse1(lst):
    """Return reversed list using map instead of while, for, slicing

    >>> reverse1([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    def reversed_element(index_and_val):
        i, val = index_and_val
        return lst[len(lst) - i - 1]
    return list(map(reversed_element, enumerate(lst)))


# 2
def convert_digit_distance_from1(num):
    """Return num_string that each digit represents
    distance from the firtst 1 after the digit

    >>> convert_digit_distance_from1(2341)
    3210
    """

    def next_dist(last, dist):
        """Return next distance from the first1
        last: each digit
        """
        if last == 1:
            return 1
        return 0 if dist == 0 else dist + 1

    dist, i, new_num = 0, 0, 0  # i represents each digit
    while num:
        num, last = num // 10, num % 10
        new_num = new_num + (dist * 10**i)
        dist, i = next_dist(last, dist), i + 1
    return new_num


# 3
def next_look_and_say(n):
    """
    >>> next_look_and_say(1)
    11
    >>> next_look_and_say(11)
    21
    >>> next_look_and_say(21)
    1211
    """

    def add_into_nextterm(count, now, i, next_term):
        """Add count and digit(e.g. 21) into next_term
        i: represents digit
        """
        count = count * 10**(i + 1)
        digit = now * 10**i
        return next_term + count + digit

    count, i, next_term = 1, 0, 0
    while n:
        n, now, next = (n // 10), (n % 10), ((n // 10) % 10)
        if now == next:
            count += 1
        else:
            next_term = add_into_nextterm(count, now, i, next_term)
            count = 1  # reset count
            i += 2
    return next_term


# 4
def crypto_solver(nums, total, ops=[
        (mul, '*'), (add, '+'), (truediv, '/'), (sub, '-')]):
    """Crypto is a puzzle game, where players receive a total and a series of
    numbers. Assume we can only use multiply, divide, add, and subtract, and
    that order of operations doesn't apply ('4+4/2'=4). Write crypto_solver,
    which finds all possible permutations of mathematical operations that will
    yield the total. For example, given [6, 2, 2], total=4, return ['6+2/2']

    >>> soln = crypto_solver([6, 2, 2], 10)  # {'6*2-2', '6+2+2'}
    >>> len(soln)
    2
    >>> '6+2+2' in soln
    True
    >>> '6*2-2' in soln
    True
    """
    rest = nums[1:]
    solutions = {str(nums[0]): nums[0]}
    for n in rest:
        # temp_solutionsに今までの式と結果を移す
        # 今までの式に演算子全てを適用するため
        temp_solutions, solutions = solutions, {}
        for streq, subtotal in temp_solutions.items():
            for op, strop in ops:
                solutions[streq + strop + str(n)] = op(subtotal, n)
    return {eq for eq, t in solutions.items() if t == total}


# 5
def replace_item_with_sum_of_two_largest(lst):
    """Replace each element of list with sum of two largest num
       after the element.
       Element will be -1 if there is not enough numbers.

    >>> replace_item_with_sum_of_two_largest([2, 3, 4, 1, 5])
    [9, 9, 6, -1, -1]
    """

    def find_two_largest_num(lst):
        max, sec_max = 0, 0
        for n in lst:
            if n > max:
                max, sec_max = n, max
            elif n > sec_max:
                sec_max = n
        return max, sec_max

    length = len(lst)
    for i in range(length):
        rest = lst[i + 1:]
        if i > length - 3:
            lst[i] = -1
        else:
            max, sec_max = find_two_largest_num(rest)
            lst[i] = max + sec_max
    return lst


# 6
def matrix_product(A, B):
    """Compute the product of two matrix A and B. If matrix multiplication is
    impossible, raise an error. Recall that the number of columns in the first
    matrix must equal the number of rows in the second matrix.

    >>> I = [
    ... [1, 0, 0, 0],
    ... [0, 1, 0, 0],
    ... [0, 0, 1, 0],
    ... [0, 0, 0, 1]]
    >>> A = [
    ... [4, 3, 2, 1],
    ... [3, 2, 1, 4],
    ... [2, 1, 4, 3],
    ... [1, 4, 3, 2]]
    >>> matrix_product(A, I) == A
    True
    """
    colsA, rowsB = len(A[0]), len(B)
    assert colsA == rowsB, "You cannot product this two matrixes"
    producted_matrix, dot_product = [], []
    for a in A:
        dot_product = []
        for b in B:
            result = sum([i * j for i, j in zip(a, b)])
            dot_product.append(result)
        producted_matrix.append(dot_product)
    return producted_matrix

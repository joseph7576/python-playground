# from: https://www.digitalocean.com/community/tutorials/how-to-write-doctests-in-python

import doctest

def add(a:int|float, b:int|float) -> int | float: # is this allowed?
    """ 
    Given two integers, return the sum.

    :param a: int
    :param b: int
    :return: int

    >>> add(2, 3)
    5
    >>> add(0, 0)
    0
    """
    return a + b


def count_vowels(word:str) -> int:
    """
    Given a single word, return the total number of vowels in that single word.

    :param word: str
    :return: int

    >>> count_vowels('Cusco')
    2

    >>> count_vowels('Manila')
    3

    >>> count_vowels('Istanbul')
    3
    """
    total_vowels = 0
    for letter in word.lower():
        if letter in 'aeiou':
            total_vowels += 1
    return total_vowels


if __name__ == "__main__":
    print(doctest.testmod())
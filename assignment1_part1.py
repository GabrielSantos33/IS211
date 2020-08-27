#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Gabriel Santos IS211
"""Assignment 1 part 1"""


def listDivide(numbers=None, divide=2):
    """Create a function named listDivide that takes in two parameters.
    One parameter is a list called numbers. The second parameter is an integer
    called divide. The divide parameter should have a default value of 2.
    The function returns the number of elements in the numbers list that
    are divisible by divide."""

    if numbers is None:
        numbers = []

    even = list()

    for i in numbers:
        if i % divide == 0:
            even.append(i)
    return even


class ListDivideException(Exception):
    """Create a custom exception class called ‘ListDivideException’.
    This should be two lines of Python code."""
    pass


def testListDivide(listDivide):
    """Write another function called testListDivide that performs the following
    tests on listDivide:
    a. listDivide([1,2,3,4,5]) should return 2
    b. listDivide([2,4,6,8,10]) should return 5
    c. listDivide([30, 54, 63,98, 100], divide=10) should return 2
    d. listDivide([]) should return 0
    e. listDivide([1,2,3,4,5], 1) should return 5
    The function testListDivide does not return anything. However,
    if any of the tests fail, the function should raise the
    ListDivideException."""

    tests = [([1, 2, 3, 4, 5], 2, 2), ([2, 4, 6, 8, 10], 2, 5),
             ([30, 54, 63, 98, 100], 10, 2), ([], 2, 0),
             ([1, 2, 3, 4, 5], 1, 5)]
    for i in tests:
        if listDivide(i[0], i[1]) != i[2]:
            raise ListDivideException("Something wicked this way comes")


if __name__ == 'main':
    testListDivide()


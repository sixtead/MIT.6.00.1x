# -*- codinf: utf-8 -*-
"""
Consider the following sequence of expressions:

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

We want to write some simple procedures that work on dictionaries to return information.

First, write a procedure, called `how_many`, which returns the sum of the number of values associated with a dictionary. For example:

>>> print(how_many(animals))
6
"""


def how_many(aDict):
    """Calculates a sum of the number of values
        associated with dictionary.

    Vars:
        aDict (dictionary): Given dictionary.

    Returns:
        int: sum of number of values.
    """
    valuesList = []

    for val in aDict.values():
        valuesList += val

    return len(valuesList)


animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(how_many(animals))

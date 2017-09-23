# -*- coding: utf-8 -*-
"""
Write a procedure called `oddTuples`, which takes a tuple as input, and returns a new tuple as output, where every other element of the input tuple is copied, starting with the first one. So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), then evaluating `oddTuples` on this input would return the tuple ('I', 'a', 'tuple').
"""


def oddTuples(aTup):
    """Filter out elements of tuple, leaving only odd ones.

    Args:
        aTup (tuple): given tuple.

    Returns:
        tuple: every other element of aTup
    """
    rTup = ()
    for i in range(0, len(aTup), 2):
        rTup += (aTup[i],)
    return rTup


aTup = ('I', 'am', 'a', 'test', 'tuple')
print(oddTuples(aTup))

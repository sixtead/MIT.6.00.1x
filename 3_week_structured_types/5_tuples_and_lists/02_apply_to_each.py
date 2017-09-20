# -*- coding: utf-8 -*-
"""
Here is the code for a function `applyToEach`:

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

Assume that
`testList = [1, -4, 8, -9]`

For each of the following questions (which you may assume is evaluated independently of the previous questions, so that `testList` has the value indicated above), provide an expression using `applyToEach`, so that after evaluation `testList` has the indicated value. You may need to write a simple procedure in each question to help with this process.
"""

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])


testList = [1, -4, 8, -9]

# Case 1:
# >>> print(testList)
# [1, 4, 8, 9]

testList = [1, -4, 8, -9]
applyToEach(testList, abs)
print(testList)

# Case 2:
# >>> print testList
# [2, -3, 9, -8]


def increment(n):
    return n + 1


testList = [1, -4, 8, -9]
applyToEach(testList, increment)
print(testList)

# Case 3:
# >>> print testList
# [1, 16, 64, 81]


def square(n):
    return n * n


testList = [1, -4, 8, -9]
applyToEach(testList, square)
print(testList)

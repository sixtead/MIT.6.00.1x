"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string 's'. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

'Number of vowels: 5'
"""
# 's' is provided
# s = "fazcbobobegghakl"
vowels = ["a", "i", "e", "o", "u"]
num_vowels = 0
for char in s:
    if char in vowels:
        num_vowels += 1
print(num_vowels)

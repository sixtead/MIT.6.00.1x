"""
Assume 's' is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in 's'. For example, if s = 'azcbobobegghakl', then your program should print
"""
# s = "zcbobobegghaklbob"
len_s = len(s)
len_bob = len("bob")
count_bob = 0
for i in range(len_s - len_bob + 1):
    if s[i:i + len_bob] == "bob":
        count_bob += 1
print("Number of times bob occures is: " + str(count_bob))

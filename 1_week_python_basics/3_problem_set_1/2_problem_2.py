s = "zcbobobegghaklbob"
len_s = len(s)
len_bob = len("bob")
count_bob = 0
for i in range(len_s - len_bob + 1):
    if s[i:i+len_bob] == "bob":
        count_bob += 1
print("Number of times bob occures is: " + str(count_bob))


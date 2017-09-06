# 's' is provided
s = "fazcbobobegghakl"
vowels = ["a", "i", "e", "o", "u"]
num_vowels = 0
for char in s:
    if char in vowels:
        num_vowels += 1
print(num_vowels)

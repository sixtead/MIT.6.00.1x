s = "abcdefghijklmnopqrstuvwxyz"
# s = "azcbobobegghakl"
# s = 'fljdngwejnn'
# s = "abcbcd"
substr = " "
substr_list = []
for char in s:
    if char >= substr[-1]:
        if substr == " ":
            substr = char
        else:
            substr += char
    else:
        substr_list.append(substr)
        substr = char
substr_list.append(substr)
print ("Longest substring in alphabetical order is: " + max(substr_list, key=len))

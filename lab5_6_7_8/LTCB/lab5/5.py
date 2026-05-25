str1 = "abtfuc"
str2 = "xdttguyz"
result = ""
for i, j in zip(str1, str2):
    result += i + "-" + j + "-"
print(result[:-1])
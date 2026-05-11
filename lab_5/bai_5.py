s1 = input("str1 = ")
s2 = input("str2 = ")

result = []
limit = max(len(s1), len(s2))

for i in range(limit):
    if i < len(s1):
        result.append(s1[i])
    if i < len(s2):
        result.append(s2[i])

print("-".join(result))

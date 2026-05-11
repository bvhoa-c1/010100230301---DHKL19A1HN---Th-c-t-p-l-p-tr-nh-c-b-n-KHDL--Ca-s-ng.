s1 = input("str1 = ")
s2 = input("str2 = ")

common = set()

for i in range(len(s1)):
    for j in range(i + 1, len(s1) + 1):
        sub = s1[i:j]
        if sub in s2:
            common.add(sub)

if not common:
    print("")
else:
    shortest = min(len(x) for x in common)
    result = sorted(x for x in common if len(x) == shortest)
    print(result)

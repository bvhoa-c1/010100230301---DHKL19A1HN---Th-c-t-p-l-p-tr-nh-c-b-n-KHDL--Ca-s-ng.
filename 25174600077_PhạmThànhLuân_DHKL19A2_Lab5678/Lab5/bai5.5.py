s1 = input("Nhập chuỗi 1: ")
s2 = input("Nhập chuỗi 2: ")

res = []

m = max(len(s1), len(s2))

for i in range(m):
    if i < len(s1):
        res.append(s1[i])
    if i < len(s2):
        res.append(s2[i])

print("-".join(res))

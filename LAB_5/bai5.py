s1 = input("Nhap chuoi 1: ")
s2 = input("Nhap chuoi 2: ")

result = []

max_len = max(len(s1), len(s2))

for i in range(max_len):
    if i < len(s1):
        result.append(s1[i])
    if i < len(s2):
        result.append(s2[i])

print("-".join(result))
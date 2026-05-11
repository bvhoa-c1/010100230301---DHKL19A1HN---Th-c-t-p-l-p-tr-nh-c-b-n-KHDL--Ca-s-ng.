
str1 = input("Nhap chuoi 1: ")
str2 = input("Nhap chuoi 2: ")

result = []

max_len = max(len(str1), len(str2))

for i in range(max_len):
    if i < len(str1):
        result.append(str1[i])

    if i < len(str2):
        result.append(str2[i])

print("-".join(result))
s1 = input("Nhap chuoi 1: ")
s2 = input("Nhap chuoi 2: ")

result = ""

for i in range(len(s1)):
    result += s1[i]

    if i < len(s2):
        result += "-" + s2[i] + "-"

print(result)
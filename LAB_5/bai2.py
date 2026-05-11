str1 = input("Nhap chuoi 1: ")
str2 = input("Nhap chuoi 2: ")

common = ""

for i in range(len(str1)):
    for j in range(i + 1, len(str1) + 1):
        sub = str1[i:j]
        if sub in str2:
            if common == "" or len(sub) < len(common):
                common = sub

print("Chuoi con chung ngan nhat:", common)
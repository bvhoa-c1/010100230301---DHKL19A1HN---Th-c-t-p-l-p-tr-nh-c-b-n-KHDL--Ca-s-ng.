str1 = input("Nhập chuỗi 1: ")
str2 = input("Nhập chuỗi 2: ")

max_sub = ""

for i in range(len(str1)):
    for j in range(i + 1, len(str1) + 1):
        sub = str1[i:j]
        if sub in str2 and len(sub) > len(max_sub):
            max_sub = sub

print("Chuỗi con chung dài nhất:", max_sub)

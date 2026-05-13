# Bài 5.2: Tìm chuỗi con chung ngắn nhất giữa hai chuỗi

str1 = input("Nhập chuỗi thứ nhất: ")
str2 = input("Nhập chuỗi thứ hai: ")

min_length = min(len(str1), len(str2))
common_substrings = []

for length in range(1, min_length + 1):
    for i in range(len(str1) - length + 1):
        substring = str1[i:i + length]
        if substring in str2:
            common_substrings.append(substring)

if common_substrings:
    shortest = min(common_substrings, key=len)
    print(f"Chuỗi con chung ngắn nhất: '{shortest}'")
else:
    print("Không có chuỗi con chung!")

s1 = input("Nhập chuỗi 1: ")
s2 = input("Nhập chuỗi 2: ")
result = ""
i = 0
while i < len(s1) or i < len(s2):
    if i < len(s1):
        result += s1[i]
    result += "-"
    if i < len(s2):
        result += s2[i]
    result += "-"
    i += 1
result = result[:-1]  # bỏ dấu - cuối
print("Kết quả trộn:", result)
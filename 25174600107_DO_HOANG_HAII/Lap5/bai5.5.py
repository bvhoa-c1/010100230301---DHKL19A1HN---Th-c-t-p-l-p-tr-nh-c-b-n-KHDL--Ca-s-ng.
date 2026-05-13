str1 = input("Nhập chuỗi thứ nhất: ")
str2 = input("Nhập chuỗi thứ hai: ")

result = []
max_len = max(len(str1), len(str2))

for i in range(max_len):
    if i < len(str1):
        result.append(str1[i])
    if i < len(str2):
        result.append(str2[i])

mixed = '-'.join(result)
print(f"Chuỗi trộn kết quả: {mixed}")

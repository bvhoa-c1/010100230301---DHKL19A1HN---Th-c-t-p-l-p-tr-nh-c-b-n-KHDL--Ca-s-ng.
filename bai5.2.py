# Tìm chuỗi con chung ngắn nhất giữa hai chuỗi

str1 = input("Nhập chuỗi thứ nhất: ")
str2 = input("Nhập chuỗi thứ hai: ")

common_substrings = []

# Duyệt tất cả chuỗi con của str1
for i in range(len(str1)):
    for j in range(i + 1, len(str1) + 1):
        sub = str1[i:j]

        # Kiểm tra có tồn tại trong str2 không
        if sub in str2:
            common_substrings.append(sub)

if len(common_substrings) == 0:
    print("Không có chuỗi con chung.")
else:
    # Tìm chuỗi con chung ngan nhat
    shortest = common_substrings[0]

    for s in common_substrings:
        if len(s) < len(shortest):
            shortest = s

    print("Chuỗi con chung ngắn nhất là:", shortest)
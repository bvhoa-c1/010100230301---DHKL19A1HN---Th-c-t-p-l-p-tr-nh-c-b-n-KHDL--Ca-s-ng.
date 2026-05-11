# Kiểm tra khả năng chuyển đổi giữa hai chuỗi

str1 = input("Nhập chuỗi ban đầu: ")
str2 = input("Nhập chuỗi mục tiêu: ")

# Tính khoảng cách chỉnh sửa đơn giản
m = len(str1)
n = len(str2)

# Tạo ma trận
dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

# Khởi tạo
for i in range(m + 1):
    dp[i][0] = i

for j in range(n + 1):
    dp[0][j] = j

# Tính số thao tác tối thiểu
for i in range(1, m + 1):
    for j in range(1, n + 1):

        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = 1 + min(
                dp[i - 1][j],      # Xóa
                dp[i][j - 1],      # Thêm
                dp[i - 1][j - 1]   # Thay thế
            )

print("Số thao tác tối thiểu cần thực hiện là:", dp[m][n])
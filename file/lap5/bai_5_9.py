# Bài 5.9: Đánh giá khả năng chuyển đổi chuỗi thông qua thêm, xóa hoặc thay thế

def min_edit_distance(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # Xóa
                    dp[i][j-1],    # Thêm
                    dp[i-1][j-1]   # Thay thế
                )
    
    return dp[m][n]

str1 = input("Nhập chuỗi ban đầu: ")
str2 = input("Nhập chuỗi mục tiêu: ")

distance = min_edit_distance(str1, str2)
print(f"Khoảng cách chỉnh sửa (Edit Distance): {distance}")
print(f"Có thể chuyển đổi từ '{str1}' thành '{str2}' với {distance} thao tác!")

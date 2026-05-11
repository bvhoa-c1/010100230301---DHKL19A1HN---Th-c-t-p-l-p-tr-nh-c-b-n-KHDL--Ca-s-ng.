

str1 = input("Nhap chuoi ban dau: ")
str2 = input("Nhap chuoi muc tieu: ")

m = len(str1)
n = len(str2)

dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(m + 1):
    dp[i][0] = i

for j in range(n + 1):
    dp[0][j] = j

for i in range(1, m + 1):
    for j in range(1, n + 1):

        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = 1 + min(
                dp[i - 1][j],      # Xoa
                dp[i][j - 1],      # Them
                dp[i - 1][j - 1]   # Thay the
            )

print("So thao tac it nhat:", dp[m][n])
def edit_distance(source, target):
    m, n = len(source), len(target)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if source[i-1] == target[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
    return dp[m][n], dp

def get_operations(source, target, dp):
    m, n = len(source), len(target)
    operations = []
    i, j = m, n
    
    while i > 0 or j > 0:
        if i > 0 and j > 0 and source[i-1] == target[j-1]:
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and dp[i-1][j-1] < dp[i-1][j] and dp[i-1][j-1] < dp[i][j-1]:
            operations.append(f"Thay thế '{source[i-1]}' thành '{target[j-1]}' tại vị trí {i-1}")
            i -= 1
            j -= 1
        elif j > 0 and dp[i][j-1] < dp[i-1][j]:
            operations.append(f"Thêm '{target[j-1]}' tại vị trí {i}")
            j -= 1
        else:
            operations.append(f"Xóa '{source[i-1]}' tại vị trí {i-1}")
            i -= 1
    
    return reversed(operations)

source = input("Nhập chuỗi ban đầu: ")
target = input("Nhập chuỗi mục tiêu: ")

distance, dp = edit_distance(source, target)

print(f"\nChuỗi ban đầu: '{source}'")
print(f"Chuỗi mục tiêu: '{target}'")
print(f"Số thao tác tối thiểu: {distance}")

if distance == 0:
    print("Hai chuỗi đã giống nhau!")
else:
    print("\nCác thao tác cần thực hiện:")
    for i, op in enumerate(get_operations(source, target, dp), 1):
        print(f"{i}. {op}")

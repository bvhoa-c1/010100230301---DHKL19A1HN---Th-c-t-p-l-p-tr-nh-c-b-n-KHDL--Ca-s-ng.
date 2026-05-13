# Bài 6.8: Tính tích của hai ma trận

def input_matrix(m, n, name):
    matrix = []
    print(f"\nNhập ma trận {name} ({m}×{n}):")
    for i in range(m):
        row = []
        for j in range(n):
            num = int(input(f"Phần tử [{i+1}][{j+1}]: "))
            row.append(num)
        matrix.append(row)
    return matrix

def display_matrix(matrix, name):
    print(f"\nMa trận {name}:")
    for row in matrix:
        print(row)

def matrix_multiply(A, B):
    m = len(A)
    n = len(B[0])
    k = len(B)
    
    if len(A[0]) != k:
        return None
    
    result = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for p in range(k):
                result[i][j] += A[i][p] * B[p][j]
    
    return result

# Nhập kích thước
m = int(input("Nhập số hàng ma trận A (m): "))
k = int(input("Nhập số cột ma trận A / số hàng ma trận B (k): "))
n = int(input("Nhập số cột ma trận B (n): "))

# Nhập ma trận
A = input_matrix(m, k, "A")
B = input_matrix(k, n, "B")

# Hiển thị ma trận
display_matrix(A, "A")
display_matrix(B, "B")

# Tính tích
result = matrix_multiply(A, B)

if result:
    print(f"\nKết quả A × B ({m}×{n}):")
    for row in result:
        print(row)
else:
    print("Không thể nhân hai ma trận này!")

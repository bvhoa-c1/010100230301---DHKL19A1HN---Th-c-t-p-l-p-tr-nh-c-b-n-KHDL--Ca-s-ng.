# Bài 6.9: Ma trận chuyển vị và kiểm tra tính đối xứng

def input_square_matrix(n):
    matrix = []
    print(f"Nhập ma trận vuông {n}×{n}:")
    for i in range(n):
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

def transpose(matrix):
    n = len(matrix)
    result = [[matrix[j][i] for j in range(n)] for i in range(n)]
    return result

def is_symmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

# Nhập ma trận
n = int(input("Nhập cấp của ma trận vuông (n): "))
matrix = input_square_matrix(n)

# Hiển thị ma trận gốc
display_matrix(matrix, "gốc")

# Tính ma trận chuyển vị
transpose_matrix = transpose(matrix)
display_matrix(transpose_matrix, "chuyển vị")

# Kiểm tra tính đối xứng
if is_symmetric(matrix):
    print("\n✓ Ma trận là ma trận đối xứng (A = A^T)")
else:
    print("\n✗ Ma trận không phải ma trận đối xứng")

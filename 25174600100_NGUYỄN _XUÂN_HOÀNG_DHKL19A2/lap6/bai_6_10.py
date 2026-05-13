# Bài 6.10: Tìm ma trận nghịch đảo của ma trận vuông cấp n

def input_square_matrix(n):
    matrix = []
    print(f"Nhập ma trận vuông {n}×{n}:")
    for i in range(n):
        row = []
        for j in range(n):
            num = float(input(f"Phần tử [{i+1}][{j+1}]: "))
            row.append(num)
        matrix.append(row)
    return matrix

def display_matrix(matrix, name):
    print(f"\nMa trận {name}:")
    for row in matrix:
        print([f"{x:.4f}" if isinstance(x, float) else x for x in row])

def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for j in range(n):
        # Tính minor
        minor = [row[:j] + row[j+1:] for row in matrix[1:]]
        det += ((-1) ** j) * matrix[0][j] * determinant(minor)
    return det

def matrix_inverse(matrix):
    n = len(matrix)
    det = determinant(matrix)
    
    if det == 0:
        return None
    
    if n == 1:
        return [[1 / matrix[0][0]]]
    
    if n == 2:
        return [
            [matrix[1][1] / det, -matrix[0][1] / det],
            [-matrix[1][0] / det, matrix[0][0] / det]
        ]
    
    # Sử dụng phương pháp bổ sung ma trận
    # Tạo ma trận bổ sung (A | I)
    augmented = [row + [1.0 if i == j else 0.0 for j in range(n)] 
                 for i, row in enumerate(matrix)]
    
    # Gauss-Jordan elimination
    for i in range(n):
        # Tìm pivot
        max_row = i
        for k in range(i + 1, n):
            if abs(augmented[k][i]) > abs(augmented[max_row][i]):
                max_row = k
        augmented[i], augmented[max_row] = augmented[max_row], augmented[i]
        
        # Chia hàng i
        pivot = augmented[i][i]
        for j in range(2 * n):
            augmented[i][j] /= pivot
        
        # Khử cột
        for k in range(n):
            if k != i:
                factor = augmented[k][i]
                for j in range(2 * n):
                    augmented[k][j] -= factor * augmented[i][j]
    
    # Trích xuất ma trận nghịch đảo
    inverse = [row[n:] for row in augmented]
    return inverse

# Nhập ma trận
n = int(input("Nhập cấp của ma trận vuông (n): "))
matrix = input_square_matrix(n)

display_matrix(matrix, "gốc")

# Tính định thức
det = determinant(matrix)
print(f"\nĐịnh thức: {det:.4f}")

if abs(det) < 1e-10:
    print("✗ Ma trận không khả nghịch (det = 0)")
else:
    # Tính ma trận nghịch đảo
    inverse = matrix_inverse(matrix)
    if inverse:
        display_matrix(inverse, "nghịch đảo")
        print("✓ Ma trận khả nghịch!")
    else:
        print("✗ Lỗi khi tính ma trận nghịch đảo!")

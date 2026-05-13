def matrix_determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for j in range(n):
        sub_matrix = [row[:j] + row[j+1:] for row in matrix[1:]]
        det += ((-1) ** j) * matrix[0][j] * matrix_determinant(sub_matrix)
    return det

def matrix_inverse(matrix):
    n = len(matrix)
    
    det = matrix_determinant(matrix)
    if det == 0:
        return None
    
    augmented = [row + [0.0] * n for row in matrix]
    for i in range(n):
        augmented[i][n + i] = 1.0
    
    for i in range(n):
        max_row = i
        for k in range(i + 1, n):
            if abs(augmented[k][i]) > abs(augmented[max_row][i]):
                max_row = k
        augmented[i], augmented[max_row] = augmented[max_row], augmented[i]
        
        pivot = augmented[i][i]
        for j in range(2 * n):
            augmented[i][j] /= pivot
        
        for k in range(n):
            if k != i:
                factor = augmented[k][i]
                for j in range(2 * n):
                    augmented[k][j] -= factor * augmented[i][j]
    
    inverse = [[augmented[i][j + n] for j in range(n)] for i in range(n)]
    return inverse

n = int(input("Nhập kích thước ma trận vuông: "))

matrix = []
print(f"\nNhập các phần tử của ma trận {n}x{n}:")
for i in range(n):
    row = []
    for j in range(n):
        num = float(input(f"Phần tử [{i}][{j}]: "))
        row.append(num)
    matrix.append(row)

print(f"\nMa trận gốc:")
for row in matrix:
    print([f"{x:.2f}" for x in row])

det = matrix_determinant(matrix)
print(f"\nDịnh thức: {det:.6f}")

if det == 0:
    print("Ma trận không khả nghịch (định thức = 0)")
else:
    inverse = matrix_inverse(matrix)
    print(f"\nMa trận nghịch đảo:")
    for row in inverse:
        print([f"{x:.6f}" for x in row])

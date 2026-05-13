m1 = int(input("Nhập số hàng của ma trận 1: "))
n1 = int(input("Nhập số cột của ma trận 1: "))

matrix1 = []
print(f"\nNhập các phần tử của ma trận 1 ({m1}x{n1}):")
for i in range(m1):
    row = []
    for j in range(n1):
        num = float(input(f"Phần tử [{i}][{j}]: "))
        row.append(num)
    matrix1.append(row)

m2 = int(input(f"\nNhập số hàng của ma trận 2: "))
n2 = int(input("Nhập số cột của ma trận 2: "))

if n1 != m2:
    print(f"Không thể nhân! Số cột ma trận 1 ({n1}) phải bằng số hàng ma trận 2 ({m2})")
else:
    matrix2 = []
    print(f"\nNhập các phần tử của ma trận 2 ({m2}x{n2}):")
    for i in range(m2):
        row = []
        for j in range(n2):
            num = float(input(f"Phần tử [{i}][{j}]: "))
            row.append(num)
        matrix2.append(row)
    
    result = [[0] * n2 for _ in range(m1)]
    
    for i in range(m1):
        for j in range(n2):
            for k in range(n1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    print(f"\nMa trận 1:")
    for row in matrix1:
        print(row)
    
    print(f"\nMa trận 2:")
    for row in matrix2:
        print(row)
    
    print(f"\nTích của hai ma trận:")
    for row in result:
        print(row)

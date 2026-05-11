# Bai 6.10

import numpy as np

n = int(input("Nhap cap ma tran: "))

matrix = []

for i in range(n):
    row = list(map(float, input().split()))
    matrix.append(row)

A = np.array(matrix)

det = np.linalg.det(A)

if det == 0:
    print("Ma tran khong kha nghich")
else:
    inverse = np.linalg.inv(A)

    print("Ma tran nghich dao:")

    print(inverse)
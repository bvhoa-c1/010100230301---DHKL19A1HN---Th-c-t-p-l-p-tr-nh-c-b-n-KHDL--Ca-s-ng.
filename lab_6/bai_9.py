m = int(input("rows = "))
n = int(input("cols = "))
matrix = []

for i in range(m):
    matrix.append(list(map(float, input(f"row {i + 1} = ").split()))[:n])

transpose = [[matrix[i][j] for i in range(m)] for j in range(n)]

for row in transpose:
    print(*row)

if m == n:
    print(matrix == transpose)
else:
    print(False)

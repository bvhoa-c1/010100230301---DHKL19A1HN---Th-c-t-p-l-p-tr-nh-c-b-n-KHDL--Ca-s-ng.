def inverse_matrix(matrix):
    n = len(matrix)
    a = [[float(matrix[i][j]) for j in range(n)] + [1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

    for col in range(n):
        pivot = col
        for row in range(col + 1, n):
            if abs(a[row][col]) > abs(a[pivot][col]):
                pivot = row

        if abs(a[pivot][col]) < 1e-12:
            return None

        a[col], a[pivot] = a[pivot], a[col]
        value = a[col][col]
        a[col] = [x / value for x in a[col]]

        for row in range(n):
            if row != col:
                factor = a[row][col]
                a[row] = [a[row][j] - factor * a[col][j] for j in range(2 * n)]

    return [row[n:] for row in a]

n = int(input("n = "))
matrix = []

for i in range(n):
    matrix.append(list(map(float, input(f"row {i + 1} = ").split()))[:n])

result = inverse_matrix(matrix)

if result is None:
    print("Not invertible")
else:
    for row in result:
        print(*[round(x, 6) for x in row])

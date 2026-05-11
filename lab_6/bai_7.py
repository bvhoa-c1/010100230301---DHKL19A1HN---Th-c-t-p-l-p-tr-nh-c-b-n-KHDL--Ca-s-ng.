m = int(input("m = "))
n = int(input("n = "))
matrix = []

for i in range(m):
    row = list(map(float, input(f"row {i + 1} = ").split()))[:n]
    matrix.append(row)

print(sum(sum(row) for row in matrix))

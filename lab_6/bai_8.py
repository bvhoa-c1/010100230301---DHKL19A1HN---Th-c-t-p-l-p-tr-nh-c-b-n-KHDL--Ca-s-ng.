m = int(input("rows A = "))
n = int(input("cols A = "))
a = []

for i in range(m):
    a.append(list(map(float, input(f"A row {i + 1} = ").split()))[:n])

p = int(input("rows B = "))
q = int(input("cols B = "))
b = []

for i in range(p):
    b.append(list(map(float, input(f"B row {i + 1} = ").split()))[:q])

if n != p:
    print("Cannot multiply")
else:
    c = [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(q)] for i in range(m)]
    for row in c:
        print(*row)

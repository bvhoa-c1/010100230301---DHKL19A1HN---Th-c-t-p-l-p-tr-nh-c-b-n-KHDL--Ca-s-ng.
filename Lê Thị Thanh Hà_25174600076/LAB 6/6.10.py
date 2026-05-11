A = []

print("Nhập ma trận 2x2")

for i in range(2):
    row = []

    for j in range(2):
        x = float(input(f"A[{i}][{j}]: "))
        row.append(x)

    A.append(row)

det = A[0][0] * A[1][1] - A[0][1] * A[1][0]

if det == 0:
    print("Ma trận không khả nghịch")
else:
    inv = [
        [A[1][1] / det, -A[0][1] / det],
        [-A[1][0] / det, A[0][0] / det]
    ]

    print("Ma trận nghịch đảo:")

    for row in inv:
        print(row)
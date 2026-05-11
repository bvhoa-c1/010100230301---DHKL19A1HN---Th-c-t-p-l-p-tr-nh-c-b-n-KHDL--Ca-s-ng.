def det2x2(m):
    return m[0][0]*m[1][1] - m[0][1]*m[1][0]
def inverse2x2(m):
    d = det2x2(m)
    if d == 0:
        return None
    return [[m[1][1]/d, -m[0][1]/d], [-m[1][0]/d, m[0][0]/d]]
n = int(input("Nhập cấp ma trận (chỉ hỗ trợ 2): "))
if n == 2:
    A = []
    for i in range(2):
        row = []
        for j in range(2):
            row.append(float(input(f"A[{i}][{j}]: ")))
        A.append(row)
    inv = inverse2x2(A)
    if inv is None:
        print("Ma trận không khả nghịch")
    else:
        print("Ma trận nghịch đảo:")
        for row in inv:
            print(row)
else:
    print("Chương trình chỉ hỗ trợ ma trận 2x2")
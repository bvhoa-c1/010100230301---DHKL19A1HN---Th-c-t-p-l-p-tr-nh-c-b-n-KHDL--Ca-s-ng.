# Nhập các phần tử của ma trận 2x2
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
d = float(input("Nhập d: "))

# Tính định thức
det = a * d - b * c

# Kiểm tra khả nghịch
if det == 0:
    print("Ma trận không khả nghịch (không có ma trận nghịch đảo)")
else:
    # Tính ma trận nghịch đảo
    A_nguoc = [
        [d / det, -b / det],
        [-c / det, a / det]
    ]

    print("Ma trận nghịch đảo là:")
    for hang in A_nguoc:
        print(hang)
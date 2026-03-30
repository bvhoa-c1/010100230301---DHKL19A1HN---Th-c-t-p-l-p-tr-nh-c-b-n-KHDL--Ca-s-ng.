n = int(input("Nhập n: "))

def tong_cs(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s

dem = 0
for i in range(1, n+1):
    if tong_cs(i) % 2 == 0:
        dem += 1

print("Số lượng:", dem)
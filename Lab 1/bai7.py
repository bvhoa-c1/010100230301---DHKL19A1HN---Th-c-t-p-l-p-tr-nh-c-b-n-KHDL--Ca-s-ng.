def tong_chu_so(x):
    return sum(int(d) for d in str(x))

n = int(input("Nhap n: "))
count = 0

for i in range(1, n + 1):
    if tong_chu_so(i) % 2 == 0:
        count += 1

print("So luong =", count)
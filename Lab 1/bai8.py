def tong_chu_so(x):
    return sum(int(d) for d in str(x))

n = int(input("Nhap n: "))
max_sum = 0
res = 1

for i in range(1, n + 1):
    s = tong_chu_so(i)
    if s > max_sum:
        max_sum = s
        res = i

print("So =", res, "voi tong chu so =", max_sum)
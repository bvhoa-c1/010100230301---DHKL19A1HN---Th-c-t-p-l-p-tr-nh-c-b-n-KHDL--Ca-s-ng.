def tong_chu_so(n):
    return sum(int(d) for d in str(n))

n = int(input("Nhập n: "))
dem = 0
for i in range(1, n + 1):
    if tong_chu_so(i) % 2 == 0:
        dem += 1
print(f"Số lượng các số thỏa mãn: {dem}")
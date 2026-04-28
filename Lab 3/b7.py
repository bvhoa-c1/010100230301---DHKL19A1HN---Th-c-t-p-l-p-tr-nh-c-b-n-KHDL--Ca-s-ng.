n = int(input("Nhập n: "))
dem = 0
for i in range(1, n+1):
    tong = sum(int(d) for d in str(i))
    if tong % 2 == 0:
        dem += 1
print("Kq:", dem)
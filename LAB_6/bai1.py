n = int(input("Nhap so phan tu: "))

a = []
for i in range(n):
    x = int(input(f"a[{i}] = "))
    a.append(x)

tong_chan = 0
tong_le = 0

for x in a:
    if x % 2 == 0:
        tong_chan += x
    else:
        tong_le += x

print("Tong so chan:", tong_chan)
print("Tong so le:", tong_le)
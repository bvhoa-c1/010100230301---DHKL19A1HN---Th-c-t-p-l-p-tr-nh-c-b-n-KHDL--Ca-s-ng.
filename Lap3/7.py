dem = 0
for i in range(1, i + 1):
    tong = sum(int(ch) for ch in str(i))
    if tong % 2 == 0:
        dem += 1
print("ket qua:", dem)
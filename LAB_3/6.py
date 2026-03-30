n = int(input())
tong = 0
if n <= 0:
    exit()
for i in range(1 , n + 1):
    tong += 1 / i
print(tong)
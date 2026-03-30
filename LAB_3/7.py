n = int(input())
if n <= 0:
    exit()
dem = 0
for i in range(1, n + 1):
    if sum(int(d) for d in str(i)) % 2 == 0:
        dem += 1
print(dem)

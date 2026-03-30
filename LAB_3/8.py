n = int(input())
if n <= 0:
    exit()
so_sum_max = 0
tong = 0

for i in range(1, n + 1):
    s = sum(int(d) for d in str(i))
    if s > tong:
        tong = s
        so_sum_max = i

print("so co tong lon nhat", so_sum_max)
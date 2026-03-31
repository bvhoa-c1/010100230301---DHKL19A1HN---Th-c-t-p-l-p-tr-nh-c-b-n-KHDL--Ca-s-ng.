# Ý A ) Tính tổng chia hết cho 7 nhưng không chia hết cho 5 trong [2000, 4000]
tong_a = 0
for i in range(2000, 4001):
    if i % 7 == 0 and i % 5 != 0:
        tong_a += i
print(f"Tổng a) = {tong_a}")

# Ý B) Tính tổng chia hết cho 4 nhưng không chia hết cho 6 trong [500, 1000]
tong_b = 0
for i in range(500, 1001):
    if i % 4 == 0 and i % 6 != 0:
        tong_b += i
print(f"Tổng b) = {tong_b}")

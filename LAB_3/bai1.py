tong_a = 0
for i in range(2000, 4001):
    if i % 7 == 0 and i % 5 != 0:
        tong_a += i
print(f"Tổng câu a: {tong_a}")


tong_b = 0
for i in range(500, 1001):
    if i % 4 == 0 and i % 6 != 0:
        tong_b += i
print(f"Tổng câu b: {tong_b}")
n = int(input("Nhập số nguyên n: "))
S1 = 0
for i in range(1, n + 1):
    S1 += 1 / i
print(f"Tổng nghịch đảo S1 = {S1}")
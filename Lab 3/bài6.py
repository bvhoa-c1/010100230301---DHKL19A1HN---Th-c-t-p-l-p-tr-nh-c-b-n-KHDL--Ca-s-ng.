n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("n phải > 0, vui lòng nhập lại: "))

S1 = 0
for i in range(1, n + 1):
    S1 += 1 / i

print("Tổng nghịch đảo S1 =", S1)
n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Nhập lại n (>0): "))
S1 = 0
for i in range(1, n + 1):
    S1 += 1 / i
print("S1 =", S1)
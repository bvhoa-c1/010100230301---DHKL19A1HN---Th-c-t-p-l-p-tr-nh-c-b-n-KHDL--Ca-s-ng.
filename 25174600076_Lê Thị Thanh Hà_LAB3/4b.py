n = 0
while n <= 0:
    n = int(input("Nhập n nguyên dương: "))
# b) S2 = 1/1 + 1/2 + ... + 1/n
s2 = sum(1/i for i in range(1, n + 1))
print(s2)
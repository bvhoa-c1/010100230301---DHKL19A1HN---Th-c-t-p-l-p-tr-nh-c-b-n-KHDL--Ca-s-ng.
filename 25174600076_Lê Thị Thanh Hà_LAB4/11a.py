n = int(input("Nhập n: "))

S1 = 0
i = 1

while True:
    term = 6 ** i
    if term > n:
        break
    S1 += term
    i += 1

print("S1 =", S1)
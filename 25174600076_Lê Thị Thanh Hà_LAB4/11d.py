S4 = 0
i = 1
n=int(input("nhập n:"))
while True:
    term = i * (i + 1) * (i + 2)
    if term > n:
        break
    S4 += term
    i += 1

print("S4 =", S4)
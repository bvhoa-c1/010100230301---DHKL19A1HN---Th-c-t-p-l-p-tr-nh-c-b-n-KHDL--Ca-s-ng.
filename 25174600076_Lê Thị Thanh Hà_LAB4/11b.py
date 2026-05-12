S2 = 0
i = 1
n=int(input("nhập n:"))
while True:
    term = 1 / (3 ** (2*i - 1))
    if term < 1/n :   # nhỏ quá thì dừng
        break
    S2 += term
    i += 1

print("S2 =", S2)
#a
n = int(input("Nhập n: "))
i = 1
s = 0
while i <= n:
    s += 6 ** i
    i += 1
print("S1 =", s)

#b
n = int(input("Nhập n: "))
i = 1
s = 0
while i <= n:
    s += 1/(3**(2**i-1))
    i += 1
print("s2 =", s)

#c
n = int(input("Nhập n: "))
i = 1
s = 0
while i <= n:
    s += ((-1) ** i)* (i**2)
    i += 1
print("S3 =", s)

#d
n = int(input("Nhập n: "))
i = 1
s = 0
while i <= n:
    s += i * (i + 1) * ( i + 2)
    i += 1
print("s4 =", s)
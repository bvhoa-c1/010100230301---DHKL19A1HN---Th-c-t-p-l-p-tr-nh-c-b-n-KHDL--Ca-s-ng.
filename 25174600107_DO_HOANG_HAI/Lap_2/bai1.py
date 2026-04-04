n = int(input("Nhập số n: "))
a = 0
b = 1
c = 0
while c < n:
    i = a + b
    a = b
    b = i
    c += 1
print(a)    
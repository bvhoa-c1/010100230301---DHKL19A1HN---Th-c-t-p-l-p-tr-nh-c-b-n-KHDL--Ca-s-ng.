n = int(input("Nhập n: "))
f= [0, 1]
for i in range(n - 2):
    s = f[-1] + f[-2]
    f.append(s)
for i in f:
    print(i, end=" ")
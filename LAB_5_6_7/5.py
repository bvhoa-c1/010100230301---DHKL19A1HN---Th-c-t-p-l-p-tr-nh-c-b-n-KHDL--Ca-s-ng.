
snt = [x for x in range(2, 100) if all(x % j != 0 for j in range(2, x))]
print(snt)
n = int(input("n = "))
a = list(map(int, input("array = ").split()))[:n]

if len(a) < 2:
    print(True)
else:
    d = a[1] - a[0]
    print(all(a[i] - a[i - 1] == d for i in range(2, len(a))))

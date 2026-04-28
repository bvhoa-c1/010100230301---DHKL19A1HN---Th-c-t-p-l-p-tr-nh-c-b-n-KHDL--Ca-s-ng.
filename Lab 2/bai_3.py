n = int(input("Nhap n: "))
i = n - 1

while i > 0:
    if n % i == 0:
        print("Uoc lon nhat (khac n):", i)
        break
    i -= 1
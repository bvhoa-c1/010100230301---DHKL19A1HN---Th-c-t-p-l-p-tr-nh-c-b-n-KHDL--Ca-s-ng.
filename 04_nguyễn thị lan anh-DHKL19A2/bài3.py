n = int(input("Nhap n: "))

i = 1
max_uoc = 1

while i < n:
    if n % i == 0:
        max_uoc = i
    i += 1

print("Uoc lon nhat =", max_uoc)
n = int(input("Nhập n: "))
uoc = 1

i = 1
while i < n:
    if n % i == 0:
        uoc = i
    i += 1

print("Ước lớn nhất:", uoc)
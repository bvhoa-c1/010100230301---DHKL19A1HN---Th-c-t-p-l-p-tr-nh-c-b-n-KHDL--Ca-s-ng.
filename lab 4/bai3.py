n = int(input("Nhập n: "))
i = 1
uoc_max = 1
while i < n:
    if n % i == 0:
        uoc_max = i
    i += 1
print("Ước lớn nhất:", uoc_max)
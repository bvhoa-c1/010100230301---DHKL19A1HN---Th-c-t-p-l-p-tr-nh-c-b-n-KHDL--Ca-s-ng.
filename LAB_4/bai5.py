n = int(input("Nhập n: "))
temp = n
dao_so = 0
while temp > 0:
    dao_so = dao_so * 10 + (temp % 10)
    temp //= 10

if n == dao_so:
    print(f"{n} là số đối xứng")
else:
    print(f"{n} không phải số đối xứng")
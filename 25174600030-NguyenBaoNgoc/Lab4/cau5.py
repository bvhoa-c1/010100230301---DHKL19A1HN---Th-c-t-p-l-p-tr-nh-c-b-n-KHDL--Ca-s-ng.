n = int(input("Nhập n: "))
temp = n
dao = 0

while temp > 0:
    digit = temp % 10
    dao = dao * 10 + digit
    temp //= 10

if dao == n:
    print(n, "là số đối xứng")
else:
    print(n, "không phải số đối xứng")
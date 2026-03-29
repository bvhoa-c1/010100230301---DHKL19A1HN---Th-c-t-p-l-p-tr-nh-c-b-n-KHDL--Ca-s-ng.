n = int(input("Nhập số: "))
temp = n
dao = 0
while temp > 0:
    digit = temp % 10
    dao = dao * 10 + digit
    temp //= 10
if dao == n:
    print("đối xứng")
else:
    print("ko đối xứng")
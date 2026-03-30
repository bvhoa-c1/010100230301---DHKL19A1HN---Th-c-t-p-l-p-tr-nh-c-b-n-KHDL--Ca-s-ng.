n = int(input("Nhập n: "))
digits = []
tmp = n
while tmp > 0:
    digits.append(tmp % 10)
    tmp //= 10
tong = sum(digits)
tich = 1
for d in digits:
    tich *= d
dao = 0
for d in digits:
    dao = dao * 10 + d
print("Tổng chữ số:", tong)
print("Tích chữ số:", tich)
print("Số đảo:", dao)

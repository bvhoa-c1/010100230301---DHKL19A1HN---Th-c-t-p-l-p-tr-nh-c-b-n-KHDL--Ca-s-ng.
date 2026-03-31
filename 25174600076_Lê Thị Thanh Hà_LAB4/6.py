n = int(input("Nhập n: "))
# số Armstrong là số mà tổng các lũy thừa của các chữ số của nó bằng chính nó, lũy thừa bậc bao nhiêu ứng với số chữ số của số đó. Ví dụ:. +Số 153 thì 1^3+5^3+3^3 = 153;.
tong = 0
temp = n
k = len(str(n))

while temp > 0:
    digit = temp % 10
    tong += digit ** k
    temp //= 10

if tong == n:
    print("Là số Armstrong")
else:
    print("Không phải")
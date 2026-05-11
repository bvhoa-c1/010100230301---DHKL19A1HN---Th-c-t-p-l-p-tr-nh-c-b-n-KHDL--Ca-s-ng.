str = input("Nhập chuỗi kí tự: ")
chuoi = ''
for i in str:
    if "0" <= i <= "9":
        chuoi += i
print("Sau khi tách:", chuoi)
n = int(chuoi)
if n < 2:
    print("Không phải số nguyên tố")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Không phải số nguyên tố")
            break
    else:
        print("Là số nguyên tố")
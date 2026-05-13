
n = int(input("Nhập một số nguyên dương: "))

if n <= 0:
    print("Vui lòng nhập một số nguyên dương!")
else:
    temp = n
    binary_manual = ""
    
    while temp > 0:
        binary_manual = str(temp % 2) + binary_manual
        temp //= 2
    
    print(f"Số {n} trong hệ nhị phân là: {binary_manual}")

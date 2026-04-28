n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("vui lòng nhập số nguyên lớn hơn 0")
else:
    print(f"các ước số của {n} là:")
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end=' ')
            
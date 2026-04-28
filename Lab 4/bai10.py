n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("n phải > 0, vui lòng nhập lại: "))

i = n
while i > 0:
    print("*" * i)
    i -= 1
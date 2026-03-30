n = int(input("Nhập số dòng: "))

i = n
while i >= 1:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i -= 1
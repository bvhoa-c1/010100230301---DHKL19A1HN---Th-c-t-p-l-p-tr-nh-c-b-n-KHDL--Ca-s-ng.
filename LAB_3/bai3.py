h = int(input("Nhập số hàng: "))
for i in range(1, h + 1):
    for j in range(1, i + 1):

        if j == 1 or j == i or i == h:
            print("*", end="")
        else:
            print(" ", end="")
    print()
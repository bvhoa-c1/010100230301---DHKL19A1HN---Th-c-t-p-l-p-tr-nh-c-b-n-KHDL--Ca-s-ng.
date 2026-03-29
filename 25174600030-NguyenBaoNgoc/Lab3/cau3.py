n = int(input("Nhập số hàng: "))

for i in range(1, n + 1):
    if i == 1:
        print("*")
    elif i == 2:
        print("**")
    elif i == n:
        print("*" * n)
    else:
        print("*", end="")
        print(" " * (i - 2), end="")
        print("*")
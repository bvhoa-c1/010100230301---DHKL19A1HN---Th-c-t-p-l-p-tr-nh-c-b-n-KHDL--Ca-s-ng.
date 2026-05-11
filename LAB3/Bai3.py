n = int(input("Nhập số hàng n: "))

for i in range(1, n + 1):
    if i == 1:
        print("*")
    elif i == n:
        print("*" * n)
    else:
        # In 1 dấu sao, sau đó là khoảng trắng, rồi 1 dấu sao chốt cuối
        print("*" + " " * (i - 2) + "*")
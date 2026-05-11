while True:
    n = int(input("Nhập n : "))
    if n > 0:
        break
    else:
        print("Nhập lại!")

# Tính tổng S1
Tong = 0
for i in range(1, n + 1):
    Tong += i

print("Tong =", Tong)
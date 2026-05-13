while True:
    n = int(input("Nhập n (n > 0): "))
    if n > 0:
        break
    else:
        print("Vui lòng nhập lại!")
S = 0
for i in range(1, n + 1):
    S += 1 / i

print(f"Tổng nghịch đảo của các số nguyên S = ", round(S,3))
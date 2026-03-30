# Bài 7: Nhập n. Đếm số lượng số trong [1, n] có tổng chữ số chẵn

def tong_chu_so(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s

def main():
    n = int(input("Nhập n: "))
    dem = 0
    for i in range(1, n + 1):
        if tong_chu_so(i) % 2 == 0:
            dem += 1
    print(f"Số lượng số có tổng chữ số chẵn trong [1, {n}]: {dem}")

if __name__ == "__main__":
    main()


# Bài 8: Nhập n. Tìm số có tổng chữ số lớn nhất trong [1, n]

def tong_chu_so(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s

def main():
    n = int(input("Nhập n: "))
    max_tong = 0
    so_max = 1
    for i in range(1, n + 1):
        t = tong_chu_so(i)
        if t > max_tong:
            max_tong = t
            so_max = i
    print(f"Số có tổng chữ số lớn nhất trong [1, {n}] là {so_max} (tổng = {max_tong})")

if __name__ == "__main__":
    main()


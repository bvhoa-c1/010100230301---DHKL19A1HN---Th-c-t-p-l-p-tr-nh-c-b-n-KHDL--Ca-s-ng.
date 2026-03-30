# Bài 9: Nhập n. Tìm số có nhiều ước nhất trong [1, n]

def dem_uoc(x):
    dem = 0
    for i in range(1, x + 1):
        if x % i == 0:
            dem += 1
    return dem

def main():
    n = int(input("Nhập n: "))
    max_uoc = 0
    so_max = 1
    for i in range(1, n + 1):
        u = dem_uoc(i)
        if u > max_uoc:
            max_uoc = u
            so_max = i
    print(f"Số có nhiều ước nhất trong [1, {n}] là {so_max} ({max_uoc} ước)")

if __name__ == "__main__":
    main()


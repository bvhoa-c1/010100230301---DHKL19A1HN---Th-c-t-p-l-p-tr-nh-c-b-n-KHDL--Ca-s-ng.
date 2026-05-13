def tong_ngich_dao(n):
    tong = 0
    for i in range(1, n + 1):
        tong += 1 / i
    return tong
print(tong_ngich_dao(5))
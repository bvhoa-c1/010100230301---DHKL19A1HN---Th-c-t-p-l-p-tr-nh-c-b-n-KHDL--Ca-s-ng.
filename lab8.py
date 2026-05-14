# bài 8.1
def la_nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

for i in range(2, 1000):
    if la_nguyen_to(i) and la_nguyen_to(i + 2):
        print((i, i + 2))
# bài 8.2
def giai_thua(n):
    gt = 1

    for i in range(1, n + 1):
        gt *= i

    return gt

n = int(input("Nhập n: "))

print("Giai thừa:", giai_thua(n))
# bài 8.3
def giai_thua(n):
    gt = 1

    for i in range(1, n + 1):
        gt *= i

    return gt


def to_hop(n, k):
    return giai_thua(n) // (giai_thua(k) * giai_thua(n - k))

n = int(input("Nhập n: "))
k = int(input("Nhập k: "))

print("Tổ hợp C(n, k) =", to_hop(n, k))
# bài 8.4
def tong_uoc(n):
    tong = 0

    for i in range(1, n + 1):
        if n % i == 0:
            tong += i

    return tong

n = int(input("Nhập n: "))

print("Tổng ước:", tong_uoc(n))
# bài 8.5
def dao_nguoc(s):
    return s[::-1]

s = input("Nhập chuỗi: ")

print(dao_nguoc(s))
# bài 8.6
def max_list(arr):
    return max(arr)

arr = list(map(int, input("Nhập dãy số: ").split()))

print("Giá trị lớn nhất:", max_list(arr))
# bài 8.7
def dem_nguyen_am(s):
    count = 0

    for c in s.lower():
        if c in "ueoai":
            count += 1

    return count

s = input("Nhập chuỗi: ")

print("Số nguyên âm:", dem_nguyen_am(s))
# bài 8.8
def dem_nguyen_am(s):
    count = 0

    for c in s.lower():
        if c in "ueoai":
            count += 1

    return count

s = input("Nhập chuỗi: ")

print("Số nguyên âm:", dem_nguyen_am(s))
# bài 8.9
def kiem_tra_doi_xung(s):
    return s == s[::-1]

s = input("Nhập chuỗi: ")

if kiem_tra_doi_xung(s):
    print("Chuỗi đối xứng")
else:
    print("Không đối xứng")
# bài 8.10
def tinh_tong(*args):
    return sum(args)

print(tinh_tong(1, 2, 3, 4, 5))
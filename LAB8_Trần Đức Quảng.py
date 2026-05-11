"""LAB 8 : XÂY DỰNG HÀM TUỲ BIẾN """
# bài 8.1 : 
def la_so_nguyen_to(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

print("Các cặp số nguyên tố sinh đôi < 1000:")
for i in range(2, 998):
    if la_so_nguyen_to(i) and la_so_nguyen_to(i + 2):
        print(f"({i}, {i+2})")


# bài  8.2: Hàm tính giai thừa
def giai_thua(n):
    kq = 1
    for i in range(1, n + 1):
        kq *= i
    return kq

# bài 8.3: Hàm tính Hoán vị (P) và Tổ hợp (C)
def hoan_vi(n, r):
    return giai_thua(n) / giai_thua(n - r)

def to_hop(n, r):
    return giai_thua(n) / (giai_thua(r) * giai_thua(n - r))

print("Hoán vị P(5,3) =", hoan_vi(5, 3))
print("Tổ hợp C(5,3) =", to_hop(5, 3))


# bài 8.4: Tính tổng lập phương các chữ số
def cubesum(n):
    tong = 0
    for chu_so in str(n):
        tong += int(chu_so)**3
    return tong

#  bài 8.5: Kiểm tra số Armstrong
def la_armstrong(n):
    return n == cubesum(n)

print("Các số Armstrong < 1000 là:")
for i in range(1, 1000):
    if la_armstrong(i):
        print(i)

# bài 8.6: Tính tổng các ước thực sự (trừ chính nó)
def sumPdivisors(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong

# bài  8.7: Kiểm tra cặp số thân thiết
def la_amicable(a, b):
    return sumPdivisors(a) == b and sumPdivisors(b) == a

num1 = 220
num2 = 284
if la_amicable(num1, num2):
    print(f"{num1} và {num2} là cặp số thân thiết!")

# bài 8.8 : 
mang = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

so_chan = list(filter(lambda x: x % 2 == 0, mang))
so_le = list(filter(lambda x: x % 2 != 0, mang))

print("Số chẵn:", so_chan)
print("Số lẻ:", so_le)

# bài 8.9 :
mang_goc = [1, 2, 3, 4, 5]
mang_moi = list(map(lambda x: x**3, mang_goc))

print("Mảng ban đầu:", mang_goc)
print("Mảng lập phương:", mang_moi)

# bài 8.10 :
mang_so = [1, 2, 3, 4, 5, 6]
so_chan_lap_phuong = list(map(lambda x: x**3, filter(lambda x: x % 2 == 0, mang_so)))
so_le_binh_phuong = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, mang_so)))
print("Mảng gốc:", mang_so)
print("Số chẵn đã lập phương:", so_chan_lap_phuong)
print("Số lẻ đã bình phương:", so_le_binh_phuong)
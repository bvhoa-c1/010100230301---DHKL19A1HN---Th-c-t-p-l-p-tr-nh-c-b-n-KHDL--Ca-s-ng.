# Bài 8.1: Xây dựng hàm kiểm tra số nguyên tố độc lập. Ứng dụng hàm này để quét, tìm kiếm
# và xuất ra toàn bộ các cặp số nguyên tố sinh đôi có giá trị nhỏ hơn 1000
def la_ngto(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print("Các cặp số nguyên tố sinh đôi có giá trị nhỏ hơn 1000:")
for i in range(1, 1000):
    if la_ngto(i) and la_ngto(i+2):
        if i+2 < 1000:
            print(f"({i}, {i+2})")
        

# Bài 8.2: Khai báo hàm xử lý toán học để tính giai thừa của một số nguyên dương, tạo tiền đề nền tảng cho các bài toán phân tích tổ hợp phức tạp.
def giai_thua(n):
    gt = 1
    for i in range(1, n + 1):
        gt *= i
    return gt

n = int(input("Nhập n: "))
if n < 0:
    print("Vui lòng nhập số nguyên dương")
else:
    print(f"{n}! =", giai_thua(n))


# Bài 8.3: Kế thừa hàm giai thừa vừa xây dựng, phát triển cấu trúc hàm tính số hoán vị của n phần tử chập r và số tổ hợp của n phần tử chập r
def giai_thua(n):
    gt = 1
    for i in range(1, n + 1):
        gt *= i
    return gt

def hoan_vi(n, r):
    return giai_thua(n) / giai_thua(n - r)

def to_hop(n, r):
    return giai_thua(n) / (giai_thua(r) * giai_thua(n - r))

n = int(input("Nhập n: "))
r = int(input("Nhập r: "))
if n < 0 or r < 0 or r > n:
    print("Dữ liệu không hợp lệ")
else:
    print("Hoán vị =", int(hoan_vi(n, r)))
    print("Tổ hợp =", int(to_hop(n, r)))


# Bài 8.4: Thiết lập hàm cubesum nhận tham số đầu vào là một số nguyên, thực hiện bóc tách và trả về tổng các lập phương từ các chữ số cấu thành số đó
def cubesum(n):
    tong = 0
    while n > 0:
        chu_so = n % 10 
        tong += chu_so ** 3 
        n //= 10         
    return tong

n = int(input("Nhập số nguyên: "))
print("Tổng lập phương các chữ số =", cubesum(n))


# Bài 8.5: Khai thác lại hàm cubesum để xây dựng hàm logic isArmstrong nhằm đánh giá tính chất Armstrong của một số, đồng thời viết thủ tục xuất danh sách các số này
def cubesum(n):
    tong = 0
    while n > 0:
        chu_so = n % 10
        tong += chu_so ** 3
        n //= 10
    return tong

def isArmstrong(n):
    return cubesum(n) == n

print("Các số Armstrong nhỏ hơn 1000 là:")
for i in range(1, 1000):
    if isArmstrong(i):
        print(i)


# Bài 8.6: Phát triển thuật toán và đóng gói thành hàm sumPdivisors chịu trách nhiệm tìm kiếm và tính tổng tất cả các ước số thực sự của một số nguyên dương đầu vào
def sumPdivisors(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong

n = int(input("Nhập n: "))
print("Tổng các ước số thực sự =", sumPdivisors(n))


# Bài 8.7: Ứng dụng hàm sumPdivisors để thiết lập hàm kiểm tra xem hai số nguyên độc lập có cấu thành một cặp số Amicable hay không theo định nghĩa toán học
def sumPdivisors(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong

def isAmicable(a, b):
    return sumPdivisors(a) == b and sumPdivisors(b) == a
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
if isAmicable(a, b):
    print(a, "và", b, "là cặp số Amicable")
else:
    print(a, "và", b, "không phải cặp số Amicable")


# Bài 8.8: Vận dụng hàm filter kết hợp cùng cú pháp lambda để phân tách một cách độc lập nhóm số chẵn và nhóm số lẻ từ một mảng dữ liệu hỗn hợp
arr = list(map(int, input("Nhập các phần tử: ").split()))
so_chan = list(filter(lambda x: x % 2 == 0, arr))
so_le = list(filter(lambda x: x % 2 != 0, arr))
print("Danh sách số chẵn:", so_chan)
print("Danh sách số lẻ:", so_le)


# Bài 8.9: Triển khai hàm map để xử lý dữ liệu hàng loạt, khởi tạo danh sách mới chứa giá trị lập phương của toàn bộ các phần tử thuộc mảng gốc
arr = list(map(int, input("Nhập các phần tử: ").split()))
lap_phuong = list(map(lambda x: x ** 3, arr))
print("Danh sách ban đầu:", arr)
print("Danh sách lập phương:", lap_phuong)


# Bài 8.10: Phối hợp đồng thời hai kỹ thuật map và filter để thiết lập một đường ống xử lý
# dữ liệu: tính lập phương riêng cho tập hợp số chẵn và bình phương riêng cho tập hợp số lẻ
arr = list(map(int, input("Nhập các phần tử: ").split()))
so_chan = list(
    map(lambda x: x ** 3,
        filter(lambda x: x % 2 == 0, arr))
)
so_le = list(
    map(lambda x: x ** 2,
        filter(lambda x: x % 2 != 0, arr))
)
print("Lập phương các số chẵn:", so_chan)
print("Bình phương các số lẻ:", so_le)
# Bài 6.1: Nhập mảng gồm n số nguyên dương. Tiến hành phân loại và tính tổng độc lập cho nhóm các số chẵn và nhóm các số lẻ
n = int(input("Nhập số lượng phần tử: "))
chan = []
le = []
tong_chan = 0
tong_le = 0

for i in range(n):
    x = int(input("Nhập phần tử: "))
    if x % 2 == 0:
        chan.append(x)
        tong_chan += x
    else:
        le.append(x)
        tong_le += x

print("Các số chẵn là:", chan)
print("Tổng chẵn là:", tong_chan)
print("Các số lẻ là:", le)
print("Tổng lẻ là:", tong_le)


# Bài 6.2: Khảo sát mảng n số nguyên dương đầu vào. Trích xuất và xuất ra màn hình toàn bộ các phần tử thỏa mãn điều kiện là số nguyên tố hoặc số hoàn hảo
def la_ngto(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def la_hhao(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    if tong == n:
        return True
    else:
        return False
    
n = int(input("Nhập số phần tử: "))
tmdk = []
for i in range(n):
    x = int(input("Nhập phần tử: "))
    if la_hhao(x) or la_ngto(x):
        tmdk.append(x)

print("Các phần tử thỏa mãn điều kiện là số hoàn hảo hoặc số nguyên tố là:", tmdk)


# Bài 6.3: Tiếp nhận một dãy số hỗn hợp gồm các số nguyên và số thực. Tìm kiếm và in ra giá trị lớn nhất cũng như giá trị nhỏ nhất tồn tại trong dãy
so = input("Nhập 1 dãy số: ")
ds = []
for x in so:
    ds.append(float(x))

so_max = ds[0]
so_min = ds[0]
for i in ds:
    if i > so_max:
        so_max = i
    if i < so_min:
        so_min = i

print("Giá trị lớn nhất là:", so_max)
print("Giá trị nhỏ nhất là:", so_min)


# Bài 6.4: Vận dụng kỹ thuật List Comprehension để khởi tạo và lưu trữ danh sách gồm n số hạng đầu tiên thuộc dãy số Fibonacci
n = int(input("Nhập n: "))
fibo = [0, 1]
[fibo.append(fibo[i-1] + fibo[i-2]) for i in range(2, n)]
print(n,"số hạng đầu tiên thuộc dãy số Fibonacci là:", fibo[:n])


# Bài 6.5: Ứng dụng cú pháp List Comprehension để thiết lập một danh sách chứa toàn bộ các số nguyên tố có giá trị nhỏ hơn 100
def la_ngto(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

ds = [i for i in range(1, 100) if la_ngto(i)]
print("Danh sách chứa toàn bộ các số nguyên tố có giá trị nhỏ hơn 100 là:", ds)


# Bài 6.6: Khảo sát một dãy số nguyên đầu vào. Thực hiện tính toán sai phân giữa các phần
# tử liên tiếp để đối chiếu và kết luận dãy số có cấu thành một cấp số cộng hay không
ds = list(map(int, input("Nhập dãy số: ").split()))
hieu = [ds[i+1] - ds[i] for i in range(len(ds)-1)]
if all(h == hieu[0] for h in hieu):
    print("Dãy số cấu thành 1 cấp số cộng")
else:
    print("Dãy số không cấu thành 1 cấp số cộng")


# Bài 6.7: Tiếp nhận dữ liệu cấu thành ma trận kích thước m × n từ người dùng. Thực hiện tính toán tổng của toàn bộ các phần tử bên trong ma trận đó
m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))
matran = []
for i in range(m):
    hang = list(map(int, input(f"Nhập hàng thứ {i+1}: ").split()))
    matran.append(hang)
tong = 0
for hang in matran:
    for phantu in hang:
        tong += phantu
print("Ma trận:")
for hang in matran:
    print(hang)
print("Tổng các phần tử trong ma trận là:", tong)


# Bài 6.8: Thiết lập cấu trúc lưu trữ cho hai ma trận riêng biệt, kiểm tra điều kiện nhân và lập trình thuật toán tính tích của hai ma trận
m = int(input("Nhập số hàng của ma trận A: "))
n = int(input("Nhập số cột của ma trận A: "))
A = []
print("Nhập ma trận A:")
for i in range(m):
    hang = list(map(int, input(f"Hàng {i+1}: ").split()))
    A.append(hang)
p = int(input("Nhập số hàng của ma trận B: "))
q = int(input("Nhập số cột của ma trận B: "))
if n != p:
    print("Không thể nhân hai ma trận")
else:
    B = []
    print("Nhập ma trận B:")
    for i in range(p):
        hang = list(map(int, input(f"Hàng {i+1}: ").split()))
        B.append(hang)
    C = []
    for i in range(m):
        hang = []
        for j in range(q):
            tong = 0
            for k in range(n):
                tong += A[i][k] * B[k][j]
            hang.append(tong)
        C.append(hang)
    print("Ma trận tích là:")
    for hang in C:
        print(hang)


# Bài 6.9: Xây dựng ma trận chuyển vị bằng cách hoán đổi hàng và cột của ma trận gốc. Ứng dụng kết quả này để kiểm tra tính đối xứng của một ma trận vuông
n = int(input("Nhập kích thước ma trận vuông n: "))
A = []
print("Nhập ma trận:")
for i in range(n):
    hang = list(map(int, input(f"Hàng {i+1}: ").split()))
    A.append(hang)
AT = []
for j in range(n):
    hang = []
    for i in range(n):
        hang.append(A[i][j])
    AT.append(hang)
print("Ma trận chuyển vị:")
for hang in AT:
    print(hang)
if A == AT:
    print("Đây là ma trận đối xứng")
else:
    print("Đây không phải ma trận đối xứng")


# Bài 6.10: Phát triển thuật toán tìm kiếm và xuất ra màn hình ma trận nghịch đảo của một ma trận vuông cấp n, với điều kiện ma trận đó khả nghịch
n = int(input("Nhập cấp ma trận: "))
A = []
print("Nhập ma trận:")
for i in range(n):
    hang = list(map(float, input(f"Hàng {i+1}: ").split()))
    A.append(hang)
if n != 2:
    print("Chương trình hiện chỉ hỗ trợ ma trận 2x2")
else:
    a = A[0][0]
    b = A[0][1]
    c = A[1][0]
    d = A[1][1]
    det = a*d - b*c
    if det == 0:
        print("Ma trận không khả nghịch")
    else:
        A_inv = [
            [d/det, -b/det],
            [-c/det, a/det]
        ]
        print("Ma trận nghịch đảo là:")
        for hang in A_inv:
            print(hang)
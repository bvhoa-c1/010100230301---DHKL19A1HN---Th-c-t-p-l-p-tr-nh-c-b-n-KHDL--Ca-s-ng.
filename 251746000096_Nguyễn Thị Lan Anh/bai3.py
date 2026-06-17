# a) Kiểm tra số nguyên tố
def so_nguyen_to():
    n = int(input("Nhập số nguyên dương n: "))
    
    if n < 2:
        print(n, "không phải số nguyên tố")
        return
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(n, "không phải số nguyên tố")
            return
    
    print(n, "là số nguyên tố")


# b) Kiểm tra số hoàn hảo
def so_hoan_hao():
    n = int(input("Nhập số nguyên dương n: "))
    
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    
    if tong == n:
        print(n, "là số hoàn hảo")
    else:
        print(n, "không phải số hoàn hảo")


# c) In số đối xứng từ 1 đến 1000
def so_doi_xung():
    dem = 0
    
    for n in range(1, 1001):
        if str(n) == str(n)[::-1]:
            print(f"{n:5}", end="")
            dem += 1
            
            if dem % 15 == 0:
                print()


# Gọi hàm
so_nguyen_to()
so_hoan_hao()
so_doi_xung()
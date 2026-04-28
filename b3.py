#a) Kiểm tra số nguyên tố
import math

def nhap_so_nguyen_duong():
    while True:
        try:
            n = int(input("Nhập vào một số nguyên dương n: "))
            if n > 0:
                return n
            else:
                print("Vui lòng nhập số lớn hơn 0!")
        except ValueError:
            print("Đầu vào không hợp lệ. Vui lòng nhập số nguyên.")

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print("--- Câu a: Kiểm tra số nguyên tố ---")
n = nhap_so_nguyen_duong()
if la_so_nguyen_to(n):
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không phải là số nguyên tố.")

#b) Kiểm tra số hoàn hảo
import math
def la_so_hoan_hao(n):
    if n < 2:
        return False
    tong_uoc = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            tong_uoc += i
            if i != n // i: 
                tong_uoc += n // i
    return tong_uoc == n
print("\n--- Câu b: Kiểm tra số hoàn hảo ---")
n = nhap_so_nguyen_duong() 
if la_so_hoan_hao(n):
    print(f"{n} là số hoàn hảo.")
else:
    print(f"{n} không phải là số hoàn hảo.")

#c) In các số đối xứng trong phạm vi 1000
def la_so_doi_xung(n):
    chuoi_so = str(n)
    return chuoi_so == chuoi_so[::-1]

def in_so_doi_xung_pham_vi(gioi_han):
    dem = 0 
    print(f"\n--- Câu c: Các số đối xứng trong phạm vi {gioi_han} ---")
    
    for i in range(1, gioi_han + 1):
        if la_so_doi_xung(i):
            print(f"{i:<5}", end="") 
            dem += 1
            if dem % 15 == 0:
                print() 
                
    print()
in_so_doi_xung_pham_vi(1000)
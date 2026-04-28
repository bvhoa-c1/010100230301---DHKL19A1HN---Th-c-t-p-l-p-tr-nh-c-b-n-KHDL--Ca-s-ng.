#a
def ktr_so_ngto():
    n = int(input("Nhập số nguyên dương n: "))
    if n < 2:
        print(f"{n} ko phải là số nguyên tố")
        return
    is_prime = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            is_prime = False
            break
        if is_prime:
            print(f"{n} là số ngto")
        else:
            print(f"{n} ko phải là số ngto")
ktr_so_ngto()

#b
def ktr_so_hoan_hao():
    n = int(input("Nhập số nguyên dương n: "))
    if n <= 0:
        print("vui lòng nhập số nguyên dương!")
        return
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    if tong == n:
        print(f"{n} là số hoàn hảo")
    else:
        print(f"{n} không phải là số hoàn hảo")
ktr_so_hoan_hao()

#c
def so_doi_xung():
    print("các số đối xứng trong phạm vi 1000:")
    dem = 0
    for n in range(1001):
        s = str(n)
        if s == s[::-1]:
            print(f"{n:5}", end=" ")
            dem += 1
            if dem % 15 == 0:
                print()
    print()
so_doi_xung()

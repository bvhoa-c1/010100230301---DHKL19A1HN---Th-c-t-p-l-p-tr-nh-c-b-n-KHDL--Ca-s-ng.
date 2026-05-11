#a)
def so_nguyen_to(n) :
    if n < 2 :
        return False
    for i in range(2,int(n**0.5)+1) :
        if n%i == 0:
            return False 
    return True
def check_snt() :
    n = int(input("Nhập số nguyên dương n :"))
    if so_nguyen_to(n) :
        print(f"{n} là số nguyên tố ")
    else :
        print(f"{n} không phải là số nguyên tố")
check_snt()

#b) 
def so_hoan_hao(n) :
    tong = 0 
    for  i in range(1,n) :
        if n%i==0 :
            tong+=i
    return tong==n
def check_shh() :
    n = int(input("Nhập số nguyên dương : "))
    if so_hoan_hao(n) :
        print(f"{n} là số hoàn hảo ")
    else :
        print(f"{n} không phải là số hoàn hảo")
check_shh()

#c)

def so_doi_xung(n):
    ban_dau = n
    thay_doi = 0
    while ban_dau > 0 :
        thay_doi = thay_doi *10 +ban_dau%10
        ban_dau=ban_dau//10
    return thay_doi == n
def check_sdx() :
    dem =0 
    for i in range(1000) :
        if so_doi_xung(i) :
            print(f"{i:5}",end = "")
            dem+=1
            if dem %15 ==0 :
                print()
check_sdx()
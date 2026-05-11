xau = input("Nhập 1 xâu : ")
ds = ""
for  i in xau :
    if i.isdigit() :
        ds+=i
print(f"Chuỗi số là : {ds}")
n = int(ds)
while True :
    if n < 2 :
        print(f"{n} không phải là số nguyên tố")
    else :
        for j in range(2,int(n**0.5)+1) :
            if n % j == 0 :
                print(f"{n} không phải là số nguyên tố")
        else:
            print(f"{n} là số nguyên tố ")
        break
    
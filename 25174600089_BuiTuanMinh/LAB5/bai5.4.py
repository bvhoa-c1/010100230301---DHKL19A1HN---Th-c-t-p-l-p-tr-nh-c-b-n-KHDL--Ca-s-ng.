chuoi = input("nhap chuoi ky tu:")
chi_so= ""
for ky_tu in chuoi:
    if ky_tu.isdigit():
        chi_so += ky_tu
print(chi_so)
if chi_so=="":
    print("ko co so nao trong chuoi")
else:
    so = int(chi_so)
    la_nguyen_to= True
    if so <2:
        la_nguyen_to = False
    else:
        for i in range (2,int(so**0.5)+1):
            if so % i ==0:
                la_nguyen_to= False
                break
    if la_nguyen_to:
        print(so,"la so nguyen to")
    else:
        print(so,"ko la so nguyen to")
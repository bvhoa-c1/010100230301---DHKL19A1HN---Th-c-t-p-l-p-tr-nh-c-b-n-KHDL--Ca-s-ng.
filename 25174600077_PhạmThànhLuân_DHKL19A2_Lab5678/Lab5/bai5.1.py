n = int(input("Nhập một số nguyên dương hệ thập phân : "))
nhi_phan = ""
while n > 0 :
    nhi_phan = str(n%2) + nhi_phan
    n = n //2
print(f"Số nhị phân : {nhi_phan} ")
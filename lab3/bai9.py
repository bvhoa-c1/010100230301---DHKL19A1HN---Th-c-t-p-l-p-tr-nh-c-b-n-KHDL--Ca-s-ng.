n = int(input("Nhập n: "))
max_uoc = 0      
so_ket_qua = 0   

for i in range(1, n + 1):
    dem = 0  
    
    for j in range(1, i + 1):
        if i % j == 0:
            dem += 1
    
    if dem > max_uoc:
        max_uoc = dem
        so_ket_qua = i

print("Số có nhiều ước nhất là:", so_ket_qua)
print("Số lượng ước là:", max_uoc)
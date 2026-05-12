# Xây dựng hàm không tham số tính lũy thừa của 1 số tự nhiên

def luy_thua():
    a = int(input("Nhập số tự nhiên: "))
    n = int(input("Nhập số mũ: "))
    
    ket_qua = a ** n
    
    print("Kết quả =", ket_qua)

# Gọi hàm
luy_thua()
# Bài 1: Xây dựng hàm không tham số tính lũy thừa một số tự nhiên

def tinh_luy_thua():
    a = int(input("Nhập cơ số: "))
    n = int(input("Nhập số mũ tự nhiên: "))
    
    ket_qua = a ** n
    
    print(f"{a}^{n} = {ket_qua}")

tinh_luy_thua()
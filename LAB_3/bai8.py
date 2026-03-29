n = int(input("Nhập n: "))
max_tong = -1
so_ket_qua = 0

for i in range(1, n + 1):
    tong_hien_tai = sum(int(chuso) for chuso in str(i))
    
    if tong_hien_tai > max_tong:
        max_tong = tong_hien_tai
        so_ket_qua = i

print(f"Số có tổng chữ số lớn nhất trong khoảng [1, {n}] là: {so_ket_qua} (Tổng = {max_tong})")
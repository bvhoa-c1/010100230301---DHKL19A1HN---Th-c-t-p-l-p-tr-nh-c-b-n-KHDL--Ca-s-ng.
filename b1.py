def tinh_luy_thua():
    try:
        co_so = int(input("Nhập cơ số (số tự nhiên): "))
        so_mu = int(input("Nhập số mũ (số tự nhiên): "))
        if co_so < 0 or so_mu < 0:
            print("Vui lòng nhập số tự nhiên (lớn hơn hoặc bằng 0).")
        else:
            ket_qua = co_so ** so_mu
            print(f"Kết quả: {co_so}^{so_mu} = {ket_qua}")
            
    except ValueError:
        print("Đầu vào không hợp lệ. Vui lòng nhập số nguyên.")

print("--- Bài 1: Tính lũy thừa ---")
tinh_luy_thua()
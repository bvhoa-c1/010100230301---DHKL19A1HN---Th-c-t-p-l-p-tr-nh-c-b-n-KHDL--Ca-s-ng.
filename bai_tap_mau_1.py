def tinh_luy_thua():
    try:
        co_so = int(input("Nhập cơ số (số tự nhiên): "))
        so_mu = int(input("Nhập số mũ (số tự nhiên): "))
        ket_qua = co_so ** so_mu
        print(f"{co_so} mũ {so_mu} là: {ket_qua}")
    except ValueError:
        print("Vui lòng nhập số tự nhiên hợp lệ.")

tinh_luy_thua()
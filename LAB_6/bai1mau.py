def tinh_luy_thua():
    """
    Hàm không tham số tính lũy thừa một số tự nhiên.
    Nhập cơ số a và số mũ n (tự nhiên) từ bàn phím,
    sau đó in và trả về kết quả a^n.
    """
    
    try:
        a = int(input("Nhập cơ số a: "))
    except ValueError:
        print("Lỗi: Cơ số a phải là một số nguyên.")
        return None
    try:
        n = int(input("Nhập số mũ n (tự nhiên, n >= 0): "))
    except ValueError:
        print("Lỗi: Số mũ n phải là một số nguyên.")
        return None

    if n < 0:
        print("Lỗi: Số mũ n phải là số tự nhiên (n >= 0).")
        return None

    if a == 0 and n == 0:
        print("Lưu ý: 0^0 là biểu thức không xác định. Kết quả trả về là 1 theo quy ước.")

    ket_qua = 1
    for i in range(n):
        ket_qua *= a

    print(f"{a}^{n} = {ket_qua}")
    return ket_qua


# Gọi hàm khi chạy file trực tiếp
if __name__ == "__main__":
    tinh_luy_thua()


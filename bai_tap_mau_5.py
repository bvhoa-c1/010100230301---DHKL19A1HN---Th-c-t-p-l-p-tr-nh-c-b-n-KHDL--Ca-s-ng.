def nhap_ky_tu():
    ky_tu = input("Nhập 1 ký tự (ESC để thoát): ")
    return ky_tu

while True:
    k = nhap_ky_tu()

    # kiểm tra nếu nhấn ESC
    if k == chr(27):   # mã ASCII của phím ESC
        print("Kết thúc chương trình.")
        break

    # chỉ lấy ký tự đầu tiên nếu nhập nhiều hơn 1 ký tự
    if len(k) > 0:
        print("Giá trị ASCII của", k[0], "là:", ord(k[0]))

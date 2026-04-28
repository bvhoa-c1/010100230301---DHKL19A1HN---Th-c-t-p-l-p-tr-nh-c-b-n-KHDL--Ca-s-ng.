def ascii_value(ch):
    return ord(ch)

while True:
    ch = input("Nhập ký tự (ESC để thoát): ")

    # Kiểm tra nếu nhập ESC (chuỗi "ESC")
    if ch == "ESC":
        break

    if len(ch) != 1:
        print("Vui lòng nhập đúng 1 ký tự!")
        continue

    print("Mã ASCII là:", ascii_value(ch))
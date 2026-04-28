def in_ascii():
    print("Nhấn ESC để thoát")

    while True:
        ky_tu = input("Nhập ký tự: ")

        # nếu người dùng không nhập gì thì bỏ qua
        if ky_tu == "":
            continue

        ky_tu = ky_tu[0]  # lấy ký tự đầu tiên

        if ord(ky_tu) == 27:  # ESC
            print("Kết thúc chương trình")
            break

        print(f"Ký tự: {ky_tu} → ASCII: {ord(ky_tu)}")

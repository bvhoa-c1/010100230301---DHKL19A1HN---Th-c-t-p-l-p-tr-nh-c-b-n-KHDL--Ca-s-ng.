def in_ascii():
    while True:
        ky_tu = input("Nhập ký tự (ESC để thoát): ")

        if ky_tu == "":
            continue
        ky_tu = ky_tu[0]

        if ord(ky_tu) == 27:
            print("Kết thúc chương trình!")
            break

        print(f"Ký tự: {ky_tu} -> ASCII: {ord(ky_tu)}")
in_ascii()
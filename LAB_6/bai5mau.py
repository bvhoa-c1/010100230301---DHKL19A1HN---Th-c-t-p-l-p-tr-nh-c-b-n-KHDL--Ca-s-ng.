while True:
    ch = input("Nhập ký tự (ESC để thoát): ")

    if ch == "":
        continue

    if ord(ch[0]) == 27:   # ESC = 27
        print("Kết thúc!")
        break

    print("Mã ASCII:", ord(ch[0]))
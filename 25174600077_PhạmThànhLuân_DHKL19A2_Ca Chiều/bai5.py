def ascii() :
    while True :
        ky_tu = input("Nhập kí tự (Nhập ESC để thoát) : ")
        if ky_tu == "ESC" :
            print("Kết thúc chương trình")
            break
        if len(ky_tu) != 1 :
            print("Vui lòng chỉ nhập 1 kí tự")
        else :
            print(f"Mã ASCII : {ord(ky_tu)}")
ascii()
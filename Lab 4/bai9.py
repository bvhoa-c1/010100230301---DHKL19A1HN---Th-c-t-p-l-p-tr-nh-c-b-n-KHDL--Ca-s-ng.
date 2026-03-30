while True:
    chon = int(input("Chọn: "))
    if chon == 0: 
        print("thoát chương trình.")
        break
 
    if chon in [1, 2, 3, 4]: 
        a = float(input("nhập a: "))
        b = float(input("nhập b: "))
        if chon == 1: 
            print("kết quả: ", a + b)
        elif chon == 2: 
            print("kết quả: ", a - b)
        elif chon == 3: 
            print("kết quả: ", a * b) 
        elif chon == 4: 
            print("kết quả: ", a / b)
        else: 
            print("k chia dc cho 0")
    else: 
        print("lựa chọn k hợp lệ.")
def in_ascii():
    while True:
        ch = input("Nhập ký tự (gõ 'esc' để thoát): ")
        
        if ch.lower() == 'esc':
            print("Kết thúc chương trình")
            break
        
        if len(ch) == 0:
            continue
        
        print("ASCII của", ch[0], "là:", ord(ch[0]))

in_ascii()
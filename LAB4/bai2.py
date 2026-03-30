# Bài 2: Nhập mật khẩu liên tục đến khi đúng "123456"
while True:
    pw = input("Nhập mật khẩu: ")
    if pw == "123456":
        print("Mật khẩu đúng!")
        break
    else:
        print("Mật khẩu sai, thử lại.")

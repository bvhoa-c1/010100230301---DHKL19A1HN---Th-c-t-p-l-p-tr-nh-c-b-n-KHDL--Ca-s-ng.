pass_correct = "123456"
password = ""
while password != pass_correct:
    password = input("Nhập mật khẩu: ")
    if password != pass_correct:
        print("Sai rồi, nhập lại nhé!")
print("Đăng nhập thành công!")
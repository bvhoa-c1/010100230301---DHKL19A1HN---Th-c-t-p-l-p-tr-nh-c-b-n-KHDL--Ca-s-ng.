
MAT_KHAU_DUNNG = "123456"
while True:
    
    nhap_vao = input("Nhập mật khẩu: ")
    
    if nhap_vao == MAT_KHAU_DUNNG:
        print("Đăng nhập thành công!")
        break  # Thoát khỏi vòng lặp khi mật khẩu đúng
    else:
        print("Sai mật khẩu rồi, vui lòng nhập lại.")
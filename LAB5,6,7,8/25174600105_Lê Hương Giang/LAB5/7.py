str = input("Nhập chuỗi kí tự: ")
in_thuong = 0
in_hoa = 0 
chu_so = 0
ky_tu_db = 0
for i in str:

    if "a" <= i <= "z":
        in_thuong += 1

    elif "A" <= i <= "Z":
        in_hoa += 1

    elif "0" <= i <= "9":
        chu_so += 1

    else:
        ky_tu_db += 1
print("Chữ thường:", in_thuong)
print("Chữ hoa:", in_hoa)
print("Chữ số:", chu_so)
print("Ký tự đặc biệt:", ky_tu_db)

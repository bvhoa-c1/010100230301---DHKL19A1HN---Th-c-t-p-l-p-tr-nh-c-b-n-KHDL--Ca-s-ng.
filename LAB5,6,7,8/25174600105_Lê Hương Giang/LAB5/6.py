str = input("Nhập chuỗi kí tự: ")
chuoi = ""
for i in str:
    if not (("a" <= i <= "z") or ("A" <= i <= "Z") or ("0" <= i <= "9")) and i not in chuoi :
        dem = str.count(i)
        percent = dem / len(str) * 100 
        print(f"{i} xuất hiện {dem} lần")
        print("Tỷ lệ: ",percent,"%")
        chuoi += i
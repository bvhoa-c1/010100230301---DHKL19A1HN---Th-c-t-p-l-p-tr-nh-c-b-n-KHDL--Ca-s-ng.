text = input("Nhập chuỗi văn bản: ")
keyword = input("Nhập từ khóa: ")

count = text.count(keyword)

if keyword in text:
    print("Vị trí đầu tiên:", text.find(keyword))
else:
    print("Không tìm thấy")

print("Số lần xuất hiện:", count)

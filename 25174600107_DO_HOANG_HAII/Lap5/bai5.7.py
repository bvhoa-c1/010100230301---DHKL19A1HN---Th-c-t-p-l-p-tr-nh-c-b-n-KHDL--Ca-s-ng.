s = input("Nhập xâu ký tự: ")

lowercase = sum(1 for c in s if c.islower())
uppercase = sum(1 for c in s if c.isupper())
digits = sum(1 for c in s if c.isdigit())
special = sum(1 for c in s if not c.isalnum())

total = len(s)

print("Thống kê chi tiết xâu ký tự:")
print(f"{'Loại ký tự':<20} {'Số lượng':<15} {'Tỷ lệ %':<15}")
print("-" * 50)

if total > 0:
    print(f"{'Chữ cái in thường':<20} {lowercase:<15} {(lowercase/total)*100:.2f}%")
    print(f"{'Chữ cái in hoa':<20} {uppercase:<15} {(uppercase/total)*100:.2f}%")
    print(f"{'Chữ số':<20} {digits:<15} {(digits/total)*100:.2f}%")
    print(f"{'Ký tự đặc biệt':<20} {special:<15} {(special/total)*100:.2f}%")
    print("-" * 50)
    print(f"{'Tổng cộng':<20} {total:<15} 100.00%")
else:
    print("Xâu rỗng!")

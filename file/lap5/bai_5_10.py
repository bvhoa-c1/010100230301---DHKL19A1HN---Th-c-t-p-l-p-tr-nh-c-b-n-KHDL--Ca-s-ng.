# Bài 5.10: Loại bỏ toàn bộ ký tự khoảng trắng

text = input("Nhập xâu: ")

# Loại bỏ tất cả ký tự khoảng trắng
result = text.replace(" ", "").replace("\t", "").replace("\n", "")

print(f"Xâu ban đầu: '{text}'")
print(f"Xâu sau khi loại bỏ khoảng trắng: '{result}'")

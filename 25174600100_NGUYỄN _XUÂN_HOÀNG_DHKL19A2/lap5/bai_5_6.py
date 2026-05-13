# Bài 5.6: Đếm ký tự đặc biệt và tính tỷ lệ phần trăm

text = input("Nhập xâu: ")

special_chars = {}
total_length = len(text)

for char in text:
    if not char.isalnum() and not char.isspace():
        special_chars[char] = special_chars.get(char, 0) + 1

if special_chars:
    print("Ký tự đặc biệt và tần suất:")
    for char, count in sorted(special_chars.items()):
        percentage = (count / total_length) * 100
        print(f"'{char}': {count} lần ({percentage:.2f}%)")
else:
    print("Không có ký tự đặc biệt nào!")

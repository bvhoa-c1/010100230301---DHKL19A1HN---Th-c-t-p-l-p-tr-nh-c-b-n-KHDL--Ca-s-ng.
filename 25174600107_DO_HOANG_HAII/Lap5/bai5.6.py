s = input("Nhập xâu ký tự: ")

special_chars = {}
for char in s:
    if not char.isalnum():
        special_chars[char] = special_chars.get(char, 0) + 1

if not special_chars:
    print("Xâu không chứa ký tự đặc biệt nào!")
else:
    print("Thống kê ký tự đặc biệt:")
    print(f"{'Ký tự':<10} {'Số lần':<10} {'Tỷ lệ %':<10}")
    print("-" * 30)
    
    for char, count in sorted(special_chars.items()):
        percentage = (count / len(s)) * 100
        print(f"'{char}'<{10-len(char)} {count:<10} {percentage:.2f}%")

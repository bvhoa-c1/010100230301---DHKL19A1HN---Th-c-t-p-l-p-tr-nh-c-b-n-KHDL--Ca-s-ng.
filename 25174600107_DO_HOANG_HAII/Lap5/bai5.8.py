s = input("Nhập xâu ký tự: ")

if len(s) <= 10:
    print("Xâu phải có độ dài lớn hơn 10 ký tự!")
else:
    print(f"Xâu gốc: {s}")
    print(f"Độ dài: {len(s)}")
    print()
    
    substring1 = s[2:9]
    print(f"Xâu con từ vị trí 2 đến 8: {substring1}")
    
    substring2 = s[5:10]
    print(f"5 ký tự từ vị trí 5: {substring2}")
    
    last3 = s[-3:]
    print(f"3 ký tự cuối cùng: {last3}")
    
    uppercase = s.upper()
    print(f"Chuyển sang chữ hoa: {uppercase}")
    
    lowercase = s.lower()
    print(f"Chuyển sang chữ thường: {lowercase}")
    
    reversed_str = s[::-1]
    print(f"Đảo ngược xâu: {reversed_str}")

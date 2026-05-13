# Bài 5.8: Các thao tác trên xâu có độ dài > 10

text = input("Nhập xâu (độ dài > 10): ")

if len(text) <= 10:
    print("Xâu phải có độ dài lớn hơn 10!")
else:
    # Trích xuất từ vị trí 2 đến 8
    substring1 = text[1:8]  # Python dùng chỉ số 0, nên vị trí 2 = index 1
    print(f"Xâu con từ vị trí 2 đến 8: '{substring1}'")
    
    # Trích xuất 5 ký tự từ vị trí 5
    substring2 = text[4:9]  # vị trí 5 = index 4
    print(f"5 ký tự từ vị trí 5: '{substring2}'")
    
    # Lấy 3 ký tự cuối cùng
    last_3 = text[-3:]
    print(f"3 ký tự cuối cùng: '{last_3}'")
    
    # Chuyển đổi sang chữ hoa
    uppercase = text.upper()
    print(f"Chữ hoa: {uppercase}")
    
    # Chuyển đổi sang chữ thường
    lowercase = text.lower()
    print(f"Chữ thường: {lowercase}")
    
    # Đảo ngược xâu
    reversed_text = text[::-1]
    print(f"Đảo ngược: {reversed_text}")

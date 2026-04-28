# Khởi tạo biến cho bảng cửu chương bắt đầu từ 2
i = 2

while i <= 9:
    print(f"--- Bảng cửu chương {i} ---")
    
    # Khởi tạo biến nhân tử bắt đầu từ 1 cho mỗi bảng
    j = 1
    while j <= 10:
        result = i * j
        print(f"{i} x {j:2} = {result:2}")
        j += 1 # Tăng nhân tử lên 1
    
    print()
    i += 1 # Chuyển sang bảng tiếp theo

def find_shortest_common_substring(str1, str2):
    """
    Tìm chuỗi ký tự con chung có độ dài ngắn nhất giữa hai chuỗi
    """
    if len(str1) > len(str2):
        str1, str2 = str2, str1
    
    common_substrings = set()
    
    # Duyệt qua tất cả các độ dài chuỗi con
    for length in range(1, len(str1) + 1):
        for i in range(len(str1) - length + 1):
            substring = str1[i:i + length]
            if substring in str2:
                common_substrings.add(substring)
    
    if not common_substrings:
        return None
    
    # Tìm chuỗi con ngắn nhất
    shortest = min(common_substrings, key=len)
    return shortest

# Nhập dữ liệu
str1 = input("Nhập chuỗi ký tự thứ nhất: ")
str2 = input("Nhập chuỗi ký tự thứ hai: ")

# Kiểm tra dữ liệu nhập
if not str1 or not str2:
    print("Vui lòng nhập hai chuỗi ký tự không rỗng!")
else:
    result = find_shortest_common_substring(str1, str2)
    
    if result:
        print(f"\nChuỗi ký tự con chung ngắn nhất: '{result}'")
        print(f"Độ dài: {len(result)}")
    else:
        print("\nKhông có chuỗi ký tự con chung nào giữa hai chuỗi!")

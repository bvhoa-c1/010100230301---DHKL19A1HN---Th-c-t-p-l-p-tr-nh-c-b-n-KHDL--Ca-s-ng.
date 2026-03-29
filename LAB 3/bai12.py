def char_to_num(c):
    if c.isdigit():
        return int(c)
    else:
        return ord(c) - ord('A') + 10

def check_digit(container):
    total = 0
    
    for i in range(len(container)):
        value = char_to_num(container[i])
        weight = 2 ** i
        total += value * weight
    
    result = total % 11
    if result == 10:
        result = 0
    
    return result

container = input("Nhập mã container (10 ký tự): ")

print("Số kiểm tra là:", check_digit(container))
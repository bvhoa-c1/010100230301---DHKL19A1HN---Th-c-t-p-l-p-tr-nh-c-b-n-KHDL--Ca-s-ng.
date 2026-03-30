for i in range(10):
    char = container[i]
    if char.isalpha():
        value = char_to_number[char]
    else:
        value = int(char)
    weight = value * (2 ** i)
    total += weight
check_digit = total % 11
if check_digit == 10:
    check_digit = 0
print(f"Số kiểm tra của container {container} là: {check_digit}")
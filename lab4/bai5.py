n = input("Nhập số n: ")

# Đảo ngược chuỗi n và so sánh với chính nó
if n == n[::-1]:
    print(f"{n} là số đối xứng (đúng)")
else:
    print(f"{n} không phải số đối xứng (sai)")
n = input("Nhập số n: ")
if n == n[::-1]:
    print(f"{n} là số đối xứng (palindrome).")
else:
    print(f"{n} không phải số đối xứng.")
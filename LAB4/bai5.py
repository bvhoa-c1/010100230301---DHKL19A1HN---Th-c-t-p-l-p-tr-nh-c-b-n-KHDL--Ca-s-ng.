# Bài 5: Kiểm tra số đối xứng (palindrome)
n = input("Nhập n: ")  # as string to check digits
if n == n[::-1]:
    print("Là số đối xứng")
else:
    print("Không phải số đối xứng")

s = input("Nhập chuỗi: ")

num_str = ""

for ch in s:
    if ch.isdigit():
        num_str += ch

if num_str == "":
    print("Không có chữ số")
else:
    n = int(num_str)

    prime = True
    if n < 2:
        prime = False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                prime = False
                break

    print("Số sau khi xử lý:", n)

    if prime:
        print("Là số nguyên tố")
    else:
        print("Không phải số nguyên tố")

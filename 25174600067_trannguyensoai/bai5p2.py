def uoc_so(n):
    ds = []
    for i in range(1, n + 1):
        if n % i == 0:
            ds.append(i)
    return ds

# Nhập dữ liệu
n = int(input("Nhập số nguyên dương n: "))

# Gọi hàm
ket_qua = uoc_so(n)

# In kết quả
print("Các ước của", n, "là:", ket_qua)
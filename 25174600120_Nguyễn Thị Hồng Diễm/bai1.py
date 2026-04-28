def tinh_luy_thua():
    try:
        a = int(input("Nhập cơ số (số tự nhiên): ").strip())
        n = int(input("Nhập số mũ (số nguyên không âm): ").strip())
    except ValueError:
        print("Lỗi: vui lòng nhập số nguyên hợp lệ.")
        return

    if n < 0:
        print("Lỗi: số mũ phải là số nguyên không âm.")
        return

    result = 1
    for _ in range(n):
        result *= a

    print(f"{a}^{n} = {result}")

if __name__ == "__main__":
    tinh_luy_thua()

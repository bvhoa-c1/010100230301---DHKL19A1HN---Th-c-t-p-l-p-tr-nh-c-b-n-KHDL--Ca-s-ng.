#a
def product_odds(n: int) -> int:
    """Hàm lõi: trả về tích 1*3*...*(2n+1)."""
    if n < 0:
        raise ValueError("n phải >= 0")
    result = 1
    for k in range(n + 1):
        result *= (2 * k + 1)
    return result

def product_odds_input():
    """Hàm không tham số: đọc n từ bàn phím và in kết quả."""
    try:
        n = int(input("Nhập n (n >= 0) cho P(n)=1*3*...*(2n+1): ").strip())
    except ValueError:
        print("Giá trị không hợp lệ")
        return
    try:
        print(f"P({n}) = {product_odds(n)}")
    except ValueError as e:
        print(e)
#b
def alternating_sum_core(n: int) -> int:
    """Hàm lõi: trả về tổng xen kẽ 1-2+3-4+..."""
    if n < 0:
        raise ValueError("n phải >= 0")
    total = 0
    for k in range(1, n + 1):
        total += k if (k % 2 == 1) else -k
    return total

def alternating_sum_input():
    """Hàm không tham số: đọc n và in S(n)."""
    try:
        n = int(input("Nhập n (n >= 0) cho S(n)=1-2+3-4+...: ").strip())
    except ValueError:
        print("Giá trị không hợp lệ")
        return
    try:
        print(f"S({n}) = {alternating_sum_core(n)}")
    except ValueError as e:
        print(e)
#c
def sum_of_prefixes_core(n: int) -> int:
    """Hàm lõi: trả về S(n)=1 + (1+2) + ... + (1+...+n)."""
    if n < 0:
        raise ValueError("n phải >= 0")
    # Dùng công thức nhanh: n*(n+1)*(n+2)/6
    return n * (n + 1) * (n + 2) // 6

def sum_of_prefixes_input():
    """Hàm không tham số: đọc n và in S(n)."""
    try:
        n = int(input("Nhập n (n >= 0) cho S(n)=sum_{k=1..n} (1+...+k): ").strip())
    except ValueError:
        print("Giá trị không hợp lệ")
        return
    try:
        print(f"S({n}) = {sum_of_prefixes_core(n)}")
    except ValueError as e:
        print(e)
#d
def power_core(x: float, y: int) -> float:
    """Hàm lõi: tính x^y, y là số nguyên."""
    if not isinstance(y, int):
        raise ValueError("y phải là số nguyên")
    return x ** y

def power_input():
    """Hàm không tham số: đọc x và y rồi in x^y."""
    try:
        x = float(input("Nhập x (số thực): ").strip())
        y = int(input("Nhập y (số nguyên): ").strip())
    except ValueError:
        print("Giá trị không hợp lệ")
        return
    try:
        print(f"{x}^{y} = {power_core(x, y)}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    product_odds_input()
    alternating_sum_input()
    sum_of_prefixes_input()
    power_input()

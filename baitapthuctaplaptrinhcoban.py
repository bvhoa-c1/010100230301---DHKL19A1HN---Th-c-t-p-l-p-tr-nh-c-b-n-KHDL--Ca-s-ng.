#Bài 5.1
n = int(input("Nhập số nguyên dương: "))
print(f"{n} -> nhị phân: {bin(n)[2:]}")
# Bài 5.2: Chuỗi con chung có độ dài ngắn nhất
def bai_5_2():
    str1 = input("Nhập str1: ")
    str2 = input("Nhập str2: ")
    min_len = min(len(str1), len(str2))
    common = ""
    for length in range(min_len, 0, -1):
        for i in range(len(str1) - length + 1):
            sub = str1[i:i+length]
            if sub in str2:
                if len(sub) < len(common) or common == "":
                    common = sub
        if common:
            break
    # Tìm chuỗi con chung ngắn nhất (length=1 trở lên)
    # Tìm tất cả chuỗi con chung rồi lấy ngắn nhất
    all_common = set()
    for length in range(1, min_len + 1):
        for i in range(len(str1) - length + 1):
            sub = str1[i:i+length]
            if sub in str2:
                all_common.add(sub)
    if all_common:
        shortest = min(all_common, key=len)
        print(f"Chuỗi con chung ngắn nhất: '{shortest}'")
    else:
        print("Không có chuỗi con chung.")
# Bài 5.3: Tìm kiếm và thống kê tần suất
def bai_5_3():
    text = input("Nhập chuỗi văn bản: ")
    key = input("Nhập từ khóa: ")
    words = text.lower().split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    pos = []
    idx = 0
    while True:
        idx = text.lower().find(key.lower(), idx)
        if idx == -1:
            break
        pos.append(idx)
        idx += 1
    print(f"Vị trí xuất hiện của '{key}': {pos}")
    max_word = max(freq, key=freq.get)
    print(f"Từ xuất hiện nhiều nhất: '{max_word}' ({freq[max_word]} lần)")
# Bài 5.4: Loại ký tự không phải chữ số, kiểm tra nguyên tố
def bai_5_4():
    s = input("Nhập chuỗi: ")
    digits = ''.join(c for c in s if c.isdigit())
    n = int(digits) if digits else 0
    def is_prime(x):
        if x < 2: return False
        for i in range(2, int(x**0.5)+1):
            if x % i == 0: return False
        return True
    print(f"Số sau khi loại ký tự: {n}")
    print(f"Là số nguyên tố: {is_prime(n)}")
# Bài 5.5: Trộn hai chuỗi ký tự
def bai_5_5():
    s1 = input("Nhập chuỗi 1: ")
    s2 = input("Nhập chuỗi 2: ")
    result = '-'.join(a + b for a, b in zip(s1, s2))
    # Xử lý phần dư
    min_len = min(len(s1), len(s2))
    extra = s1[min_len:] + s2[min_len:]
    if extra:
        result = result + '-' + '-'.join(extra) if result else '-'.join(extra)
    print(f"Chuỗi sau khi trộn: {result}")
# Bài 5.6: Đếm ký tự đặc biệt
def bai_5_6():
    s = input("Nhập chuỗi: ")
    special_count = {}
    total = 0
    for c in s:
        if not c.isalpha() and not c.isdigit():
            special_count[c] = special_count.get(c, 0) + 1
            total += 1
    for c, cnt in special_count.items():
        print(f"'{c}': {cnt} lần, tỉ lệ: {cnt/len(s)*100:.2f}%")
    print(f"Tổng ký tự đặc biệt: {total}")
# Bài 5.7: Thống kê chi tiết chuỗi
def bai_5_7():
    s = input("Nhập chuỗi: ")
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    digits = sum(1 for c in s if c.isdigit())
    special = sum(1 for c in s if not c.isalnum())
    print(f"Chữ hoa: {upper}, Chữ thường: {lower}, Chữ số: {digits}, Đặc biệt: {special}")
# Bài 5.8: Xử lý chuỗi dài hơn 10 ký tự
def bai_5_8():
    s = input("Nhập chuỗi: ")
    if len(s) > 10:
        sub1 = s[1:8]        # vị trí 2 đến 8 (index 1..7)
        sub2 = s[-3:]         # 3 ký tự cuối
        swapped = s.swapcase()
        reversed_s = s[::-1]
        print(f"Chuỗi con vị trí 2-8: {sub1}")
        print(f"3 ký tự cuối: {sub2}")
        print(f"Đổi hoa/thường: {swapped}")
        print(f"Đảo ngược: {reversed_s}")
    else:
        print("Chuỗi không đủ dài (cần > 10 ký tự).")
# Bài 5.9: Chuyển đổi chuỗi thành mục tiêu bằng thêm/xóa/thay thế
def bai_5_9():
    s = input("Nhập chuỗi ban đầu: ")
    target = input("Nhập chuỗi mục tiêu: ")
    # Đếm số thao tác tối thiểu (edit distance - Levenshtein)
    m, n = len(s), len(target)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1): dp[i][0] = i
    for j in range(n+1): dp[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == target[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    print(f"Số thao tác tối thiểu để chuyển '{s}' thành '{target}': {dp[m][n]}")
# Bài 5.10: Xóa khoảng trắng trong chuỗi
def bai_5_10():
    s = input("Nhập chuỗi: ")
    result = s.replace(" ", "")
    print(f"Chuỗi sau khi xóa khoảng trắng: '{result}'")
# LAB 6: DANH SÁCH VÀ BỘ (LIST & TUPLE)
# Bài 6.1: Phân loại số chẵn/lẻ và tính tổng
def bai_6_1():
    n = int(input("Nhập n: "))
    arr = list(map(int, input("Nhập mảng: ").split()))
    even = [x for x in arr if x % 2 == 0]
    odd  = [x for x in arr if x % 2 != 0]
    print(f"Số chẵn: {even}, tổng = {sum(even)}")
    print(f"Số lẻ:  {odd}, tổng = {sum(odd)}")
# Bài 6.2: Lọc số nguyên tố và số hoàn hảo
def bai_6_2():
    arr = list(map(int, input("Nhập mảng: ").split()))
    def is_prime(x):
        if x < 2: return False
        for i in range(2, int(x**0.5)+1):
            if x % i == 0: return False
        return True
    def is_perfect(x):
        return x > 1 and sum(i for i in range(1, x) if x % i == 0) == x
    result = [x for x in arr if is_prime(x) or is_perfect(x)]
    print(f"Số nguyên tố hoặc hoàn hảo: {result}")
# Bài 6.3: Tìm max và min trong dãy hỗn hợp
def bai_6_3():
    data = input("Nhập dãy số (cách nhau bởi dấu cách): ").split()
    nums = [float(x) for x in data]
    print(f"Lớn nhất: {max(nums)}, Nhỏ nhất: {min(nums)}")
# Bài 6.4: n số hạng đầu dãy Fibonacci bằng List Comprehension
def bai_6_4():
    n = int(input("Nhập n: "))
    fib = [0, 1]
    [fib.append(fib[-1] + fib[-2]) for _ in range(n - 2)]
    print(f"Fibonacci: {fib[:n]}")
# Bài 6.5: Số nguyên tố < 100 bằng List Comprehension
def bai_6_5():
    def is_prime(x):
        if x < 2: return False
        return all(x % i != 0 for i in range(2, int(x**0.5)+1))
    primes = [x for x in range(2, 100) if is_prime(x)]
    print(f"Số nguyên tố < 100: {primes}")
# Bài 6.6: Kiểm tra cấp số cộng
def bai_6_6():
    arr = list(map(int, input("Nhập dãy số: ").split()))
    diffs = [arr[i+1] - arr[i] for i in range(len(arr)-1)]
    is_ap = len(set(diffs)) == 1
    print(f"Là cấp số cộng: {is_ap}")
# Bài 6.7: Ma trận m×n và tổng các phần tử bên trong (không viền)
def bai_6_7():
    m = int(input("Nhập m: "))
    n = int(input("Nhập n: "))
    matrix = []
    for i in range(m):
        row = list(map(int, input(f"Nhập hàng {i+1}: ").split()))
        matrix.append(row)
    inner_sum = sum(matrix[i][j] for i in range(1, m-1) for j in range(1, n-1))
    print(f"Tổng phần tử bên trong ma trận: {inner_sum}")
# Bài 6.8: Kiểm tra điều kiện nhân và tích hai ma trận
def bai_6_8():
    def input_matrix(name):
        r = int(input(f"Số hàng ma trận {name}: "))
        c = int(input(f"Số cột ma trận {name}: "))
        mat = [list(map(int, input(f"Hàng {i+1}: ").split())) for i in range(r)]
        return mat, r, c
    A, rA, cA = input_matrix("A")
    B, rB, cB = input_matrix("B")
    if cA != rB:
        print("Không thể nhân: số cột A phải bằng số hàng B.")
    else:
        C = [[sum(A[i][k]*B[k][j] for k in range(cA)) for j in range(cB)] for i in range(rA)]
        print("Tích hai ma trận:")
        for row in C: print(row)
# Bài 6.9: Ma trận chuyển vị và kiểm tra đối xứng
def bai_6_9():
    n = int(input("Nhập n: "))
    matrix = [list(map(int, input(f"Hàng {i+1}: ").split())) for i in range(n)]
    transpose = [[matrix[j][i] for j in range(n)] for i in range(n)]
    is_symmetric = all(matrix[i][j] == matrix[j][i] for i in range(n) for j in range(n))
    print("Ma trận chuyển vị:")
    for row in transpose: print(row)
    print(f"Ma trận đối xứng: {is_symmetric}")
# Bài 6.10: Ma trận nghịch đảo (n×n, dùng Gauss-Jordan)
def bai_6_10():
    n = int(input("Nhập n: "))
    matrix = [list(map(float, input(f"Hàng {i+1}: ").split())) for i in range(n)]
    # Tạo ma trận tăng cường [A | I]
    aug = [matrix[i] + [1 if i==j else 0 for j in range(n)] for i in range(n)]
    for col in range(n):
        # Tìm pivot
        max_row = max(range(col, n), key=lambda r: abs(aug[r][col]))
        aug[col], aug[max_row] = aug[max_row], aug[col]
        pivot = aug[col][col]
        if abs(pivot) < 1e-9:
            print("Ma trận không khả nghịch!")
            return
        aug[col] = [x / pivot for x in aug[col]]
        for row in range(n):
            if row != col:
                factor = aug[row][col]
                aug[row] = [aug[row][k] - factor * aug[col][k] for k in range(2*n)]
    inverse = [aug[i][n:] for i in range(n)]
    print("Ma trận nghịch đảo:")
    for row in inverse: print([round(x, 4) for x in row])
# LAB 7: TẬP HỢP VÀ TỪ ĐIỂN (SET & DICTIONARY)
# Bài 7.1: Từ điển kích thước N, khóa x, giá trị x^3
def bai_7_1():
    N = int(input("Nhập N: "))
    d = {x: x**3 for x in range(1, N+1)}
    print(d)
# Bài 7.2: Từ điển sinh viên, xếp loại học lực
def bai_7_2():
    n = int(input("Nhập số sinh viên: "))
    students = {}
    for _ in range(n):
        name = input("Tên: ")
        score = float(input("Điểm: "))
        students[name] = score
    def rank(s):
        if s >= 9: return 'A'
        elif s >= 8: return 'B'
        elif s >= 7: return 'C'
        elif s >= 5: return 'D'
        else: return 'F'
    for name, score in students.items():
        print(f"{name}: {score} -> {rank(score)}")
# Bài 7.3: Từ điển đếm tần suất sinh viên theo mức học lực
def bai_7_3():
    n = int(input("Nhập số sinh viên: "))
    freq = {'A':0,'B':0,'C':0,'D':0,'F':0}
    for _ in range(n):
        score = float(input("Điểm: "))
        if score >= 9: freq['A'] += 1
        elif score >= 8: freq['B'] += 1
        elif score >= 7: freq['C'] += 1
        elif score >= 5: freq['D'] += 1
        else: freq['F'] += 1
    for k, v in freq.items():
        print(f"Loại {k}: {v} sinh viên")
# Bài 7.4: Tần suất từ trong đoạn văn bản
def bai_7_4():
    text = input("Nhập đoạn văn: ")
    import re
    words = re.findall(r'\b\w+\b', text.lower())
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    for word, count in sorted(freq.items()):
        print(f"'{word}': {count}")
# Bài 7.5: Tìm từ có tần suất cao nhất và thấp nhất
def bai_7_5():
    text = input("Nhập văn bản: ")
    import re
    words = re.findall(r'\b\w+\b', text.lower())
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    max_word = max(freq, key=freq.get)
    min_word = min(freq, key=freq.get)
    print(f"Từ xuất hiện nhiều nhất: '{max_word}' ({freq[max_word]} lần)")
    print(f"Từ xuất hiện ít nhất: '{min_word}' ({freq[min_word]} lần)")
# Bài 7.6: Từ điển hành trang, thêm 'pocket' và cập nhật 'gold'
def bai_7_6():
    inventory = {
        'backpack': ['sword', 'shield'],
        'gold': 100
    }
    inventory['pocket'] = ['map', 'compass']
    inventory['gold'] += 50
    print(inventory)
# Bài 7.7: Hiển thị vật phẩm trong 'backpack', loại bỏ một vật phẩm
def bai_7_7():
    inventory = {
        'backpack': ['sword', 'shield', 'potion'],
        'pocket': ['map'],
        'gold': 150
    }
    print("Vật phẩm trong backpack:", inventory['backpack'])
    item = input("Nhập vật phẩm cần loại bỏ: ")
    if item in inventory['backpack']:
        inventory['backpack'].remove(item)
        print(f"Đã loại bỏ '{item}'.")
    else:
        print(f"'{item}' không có trong backpack.")
    print("Backpack sau khi cập nhật:", inventory['backpack'])
# Bài 7.8: Hóa đơn từ hai từ điển (số lượng tồn kho + đơn giá)
def bai_7_8():
    stock    = {'apple': 10, 'banana': 5, 'cherry': 20}
    price    = {'apple': 3000, 'banana': 2000, 'cherry': 5000}
    print(f"{'Mặt hàng':<12} {'SL':>5} {'Đơn giá':>10} {'Thành tiền':>12}")
    print("-" * 42)
    total = 0
    for item in stock:
        cost = stock[item] * price[item]
        total += cost
        print(f"{item:<12} {stock[item]:>5} {price[item]:>10,} {cost:>12,}")
    print(f"{'Tổng cộng':>30}: {total:>12,} VND")
# Bài 7.9: Phát triển thủ tục xuất kho và báo cáo tồn kho
def bai_7_9():
    stock = {'apple': 10, 'banana': 5, 'cherry': 20}
    item = input("Nhập mặt hàng cần xuất: ")
    qty = int(input("Số lượng xuất: "))
    if item not in stock:
        print("Mặt hàng không tồn tại.")
    elif stock[item] < qty:
        print(f"Không đủ hàng. Tồn kho: {stock[item]}")
    else:
        stock[item] -= qty
        print(f"Xuất thành công {qty} {item}.")
    print("Tình trạng tồn kho:")
    for k, v in stock.items():
        print(f"  {k}: {v}")
# Bài 7.10: Set để biểu diễn danh mục và trích xuất hàng chưa bán
def bai_7_10():
    catalog  = {'apple', 'banana', 'cherry', 'date', 'elderberry'}
    sold     = {'apple', 'cherry'}
    unsold   = catalog - sold
    print(f"Hàng trong kho nhưng chưa bán: {unsold}")
# LAB 8: XÂY DỰNG HÀM TÙY BIẾN
# Bài 8.1: Hàm kiểm tra số nguyên tố, tìm tất cả cặp sinh đôi < 1000
def bai_8_1():
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0: return False
        return True
    twin_primes = [(p, p+2) for p in range(2, 999) if is_prime(p) and is_prime(p+2)]
    print(f"Các cặp số nguyên tố sinh đôi < 1000: {twin_primes}")
# Bài 8.2: Hàm tính giai thừa
def bai_8_2():
    def factorial(n):
        if n == 0: return 1
        return n * factorial(n - 1)
    n = int(input("Nhập n: "))
    print(f"{n}! = {factorial(n)}")
# Bài 8.3: Hàm tính số hoán vị C(n,r) và tổ hợp C(n,r)
def bai_8_3():
    def factorial(n):
        if n == 0: return 1
        return n * factorial(n-1)
    def permutation(n, r):
        return factorial(n) // factorial(n - r)
    def combination(n, r):
        return factorial(n) // (factorial(r) * factorial(n - r))
    n = int(input("Nhập n: "))
    r = int(input("Nhập r: "))
    print(f"P({n},{r}) = {permutation(n,r)}")
    print(f"C({n},{r}) = {combination(n,r)}")
# Bài 8.4: Hàm cubesum nhận số nguyên, bóc tách chữ số, tổng lập phương
def bai_8_4():
    def cubesum(n):
        return sum(int(d)**3 for d in str(abs(n)))
    n = int(input("Nhập số nguyên: "))
    print(f"cubesum({n}) = {cubesum(n)}")
# Bài 8.5: Hàm isArmstrong dùng cubesum
def bai_8_5():
    def cubesum(n):
        digits = str(abs(n))
        k = len(digits)
        return sum(int(d)**k for d in digits)
    def isArmstrong(n):
        return cubesum(n) == n
    print("Các số Armstrong từ 1 đến 9999:")
    print([n for n in range(1, 10000) if isArmstrong(n)])
# Bài 8.6: Hàm sumPdivisors – tổng ước số thực sự
def bai_8_6():
    def sumPdivisors(n):
        return sum(i for i in range(1, n) if n % i == 0)
    n = int(input("Nhập số nguyên dương: "))
    print(f"Tổng ước thực sự của {n} = {sumPdivisors(n)}")
# Bài 8.7: Kiểm tra cặp số Amicable
def bai_8_7():
    def sumPdivisors(n):
        return sum(i for i in range(1, n) if n % i == 0)
    def isAmicable(a, b):
        return a != b and sumPdivisors(a) == b and sumPdivisors(b) == a
    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))
    print(f"({a}, {b}) là cặp Amicable: {isAmicable(a, b)}")
# Bài 8.8: Dùng filter và lambda tách số chẵn/lẻ
def bai_8_8():
    arr = list(map(int, input("Nhập mảng: ").split()))
    evens = list(filter(lambda x: x % 2 == 0, arr))
    odds  = list(filter(lambda x: x % 2 != 0, arr))
    print(f"Số chẵn: {evens}")
    print(f"Số lẻ:  {odds}")
# Bài 8.9: Dùng map tạo danh sách lập phương
def bai_8_9():
    arr = list(map(int, input("Nhập mảng: ").split()))
    cubes = list(map(lambda x: x**2, arr))
    print(f"Lập phương: {cubes}")
# Bài 8.10: Kết hợp map và filter – lập phương số chẵn, bình phương số lẻ
def bai_8_10():
    arr = list(map(int, input("Nhập mảng: ").split()))
    evens_sq  = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, arr)))
    odds_sq   = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, arr)))
    print(f"Lập phương số chẵn: {evens_sq}")
    print(f"Bình phương số lẻ:  {odds_sq}")
    # MENU CHẠY THỬ
if __name__ == "__main__":
    labs = {
        "5.2": bai_5_2,  "5.3": bai_5_3,  "5.4": bai_5_4,
        "5.5": bai_5_5,  "5.6": bai_5_6,  "5.7": bai_5_7,  "5.8": bai_5_8,
        "5.9": bai_5_9,  "5.10": bai_5_10,
        "6.1": bai_6_1,  "6.2": bai_6_2,  "6.3": bai_6_3,  "6.4": bai_6_4,
        "6.5": bai_6_5,  "6.6": bai_6_6,  "6.7": bai_6_7,  "6.8": bai_6_8,
        "6.9": bai_6_9,  "6.10": bai_6_10,
        "7.1": bai_7_1,  "7.2": bai_7_2,  "7.3": bai_7_3,  "7.4": bai_7_4,
        "7.5": bai_7_5,  "7.6": bai_7_6,  "7.7": bai_7_7,  "7.8": bai_7_8,
        "7.9": bai_7_9,  "7.10": bai_7_10,
        "8.1": bai_8_1,  "8.2": bai_8_2,  "8.3": bai_8_3,  "8.4": bai_8_4,
        "8.5": bai_8_5,  "8.6": bai_8_6,  "8.7": bai_8_7,  "8.8": bai_8_8,
        "8.9": bai_8_9,  "8.10": bai_8_10,
    }
    print("=== DANH SÁCH BÀI ===")
    print("Lab 5: 5.2 → 5.10 | Lab 6: 6.1 → 6.10")
    print("Lab 7: 7.1 → 7.10 | Lab 8: 8.1 → 8.10")
    choice = input("\nChạy bài nào? (vd: 5.1): ").strip()
    if choice in labs:
        print(f"\n--- Bài {choice} ---")
        labs[choice]()
    else:
        print("Bài không tồn tại. Vui lòng nhập đúng định dạng (vd: 5.1, 7.10).")
 
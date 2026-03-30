# Bài 1: Tính tổng các số thỏa mãn điều kiện
# a) Chia hết cho 7 nhưng không chia hết cho 5 trong [2000, 4000]
# b) Chia hết cho 4 nhưng không chia hết cho 6 trong [500, 1000]

def main():
    # Phần a
    tong_a = 0
    for i in range(2000, 4001):
        if i % 7 == 0 and i % 5 != 0:
            tong_a += i
    print(f"Tổng a (2000-4000, chia hết 7 không 5): {tong_a}")

    # Phần b
    tong_b = 0
    for i in range(500, 1001):
        if i % 4 == 0 and i % 6 != 0:
            tong_b += i
    print(f"Tổng b (500-1000, chia hết 4 không 6): {tong_b}")

if __name__ == "__main__":
    main()


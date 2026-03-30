# Bài 5: Tìm và in các số chính phương từ 1 đến 1000 sử dụng vòng lặp for

import math

def main():
    print("Các số chính phương từ 1 đến 1000:")
    for i in range(1, 1001):
        sqrt_i = math.sqrt(i)
        if sqrt_i == int(sqrt_i):
            print(i, end=" ")
    print()

if __name__ == "__main__":
    main()


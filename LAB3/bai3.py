# Bài 3: Nhập số hàng n, vẽ tam giác vuông rỗng

def main():
    n = int(input("Nhập số hàng n: "))
    
    for i in range(1, n + 1):
        if i == 1 or i == n:
            print("*" * i)
        else:
            print("*" + " " * (i * 2 - 3) + "*")

if __name__ == "__main__":
    main()


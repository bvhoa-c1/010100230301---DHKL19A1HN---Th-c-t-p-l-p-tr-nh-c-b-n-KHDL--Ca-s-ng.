# Bài 2: In bảng cửu chương 1-9 dạng bảng 2 chiều

def main():
    print("Bảng cửu chương từ 1 đến 9:")
    print(" " * 4, end="")
    for i in range(1, 10):
        print(f"{i:4}", end="")
    print()
    
    for i in range(1, 10):
        print(f"{i:2} ", end="")
        for j in range(1, 10):
            print(f"{i*j:4}", end="")
        print()

if __name__ == "__main__":
    main()


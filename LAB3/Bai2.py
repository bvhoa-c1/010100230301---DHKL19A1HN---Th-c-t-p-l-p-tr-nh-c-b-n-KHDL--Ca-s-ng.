for i in range(1, 10):
    for j in range(1, 10):
        # In theo định dạng: số x số = kết quả, end="\t" để tạo khoảng cách ngang
        print(f"{j} x {i} = {i*j}", end="\t")
    print() # Xuống dòng khi hết 1 hàng
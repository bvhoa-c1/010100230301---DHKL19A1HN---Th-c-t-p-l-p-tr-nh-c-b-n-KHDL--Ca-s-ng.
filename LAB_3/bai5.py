print("Các số chính phương từ 1 đến 1000 là:")

# Sử dụng vòng lặp for để bình phương từng số nguyên i
# range(1, 32) sẽ chạy i từ 1 đến 31
for i in range(1, 32):
    so_chinh_phuong = i ** 2
    if so_chinh_phuong <= 1000:
        print(so_chinh_phuong, end=" ")
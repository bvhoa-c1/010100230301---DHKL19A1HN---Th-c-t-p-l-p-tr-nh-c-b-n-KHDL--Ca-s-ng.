chuoi_goc = input("Nhập chuỗi ban đầu: ")
chuoi_muc_tieu = input("Nhập chuỗi mục tiêu: ")
do_dai_ngan_nhat = min(len(chuoi_goc), len(chuoi_muc_tieu))
so_thao_tac = 0
for i in range(do_dai_ngan_nhat):
    if chuoi_goc[i] != chuoi_muc_tieu[i]:
        so_thao_tac += 1
so_thao_tac += abs(len(chuoi_goc) - len(chuoi_muc_tieu))
print("Cần", so_thao_tac, "thao tác(thêm/xóa/thay thế) để chuyển", chuoi_goc,"sang", chuoi_muc_tieu)


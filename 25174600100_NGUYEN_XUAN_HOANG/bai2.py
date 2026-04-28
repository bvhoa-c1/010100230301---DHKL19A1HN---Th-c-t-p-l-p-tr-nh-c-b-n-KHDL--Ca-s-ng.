def giai_phuong_trinh_bac_nhat(a, b):
    """
    Giải phương trình bậc nhất có dạng ax + b = 0.

    Args:
        a (float): Hệ số của x.
        b (float): Hằng số.
    """
    if a == 0:
        if b == 0:
            print("Phương trình có vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        nghiem_x = -b / a
        print(f"Phương trình có nghiệm duy nhất x = {nghiem_x}")
giai_phuong_trinh_bac_nhat(-3, 9)
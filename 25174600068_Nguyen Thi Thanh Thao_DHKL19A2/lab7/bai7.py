hanh_trang = {
    "backpack": ["rope", "torch", "apple", "dagger"]
}

hanh_trang["backpack"].sort()

print("Sau khi sap xep:")
print(hanh_trang["backpack"])

vat_pham = input("Nhap vat pham can xoa: ")

if vat_pham in hanh_trang["backpack"]:
    hanh_trang["backpack"].remove(vat_pham)

print("Danh sach sau khi xoa:")
print(hanh_trang["backpack"])
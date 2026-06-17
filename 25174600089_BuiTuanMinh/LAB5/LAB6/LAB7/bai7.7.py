inventory = {
    "backpack": ["sword", "potion", "map", "torch", "bread"],
    "gold":     100,
}

print("Backpack ban đầu:", inventory["backpack"])
inventory["backpack"].sort()
print("Backpack sau khi sắp xếp:", inventory["backpack"])

xoa = input("Nhập tên vật phẩm muốn xóa: ").strip()

if xoa in inventory["backpack"]:
    inventory["backpack"].remove(xoa)
    print(f"Đã xóa '{xoa}'. Backpack còn lại:", inventory["backpack"])
else:
    print(f"Không tìm thấy '{xoa}' trong backpack.")
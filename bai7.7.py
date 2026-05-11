# Từ điển inventory
inventory = {
    "gold": 500,
    "pouch": ["flint", "twine", "gemstone"],
    "backpack": ["xylophone", "dagger", "bedroll", "bread loaf"]
}

# Hiển thị backpack ban đầu
print("Backpack ban đầu:")
print(inventory["backpack"])

# Sắp xếp theo thứ tự từ điển
inventory["backpack"].sort()

# Xóa một vật phẩm cụ thể
inventory["backpack"].remove("dagger")

# Hiển thị backpack sau khi cập nhật
print("\nBackpack sau khi sắp xếp và xóa vật phẩm:")
print(inventory["backpack"])
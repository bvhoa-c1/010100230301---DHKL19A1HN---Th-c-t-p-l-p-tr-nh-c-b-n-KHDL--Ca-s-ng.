inventory = {
    'backpack': ['rope', 'torch', 'gold coin', 'sword', 'shield'],
    'gold': 750
}

print("Hành trang ban đầu:")
print(f"Backpack: {inventory['backpack']}")

backpack_sorted = sorted(inventory['backpack'])

print(f"\nBackpack sau sắp xếp: {backpack_sorted}")

item_to_remove = input("\nNhập tên vật phẩm cần loại bỏ: ")

if item_to_remove in backpack_sorted:
    backpack_sorted.remove(item_to_remove)
    inventory['backpack'] = backpack_sorted
    print(f"Đã loại bỏ '{item_to_remove}'")
else:
    print(f"Không tìm thấy '{item_to_remove}' trong backpack")

print(f"\nBackpack cuối cùng: {inventory['backpack']}")

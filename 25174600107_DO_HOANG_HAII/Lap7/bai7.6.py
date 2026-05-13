inventory = {
    'backpack': ['rope', 'torch', 'gold coin'],
    'gold': 500
}

print("Hành trang ban đầu:")
print(f"Backpack: {inventory['backpack']}")
print(f"Vàng: {inventory['gold']}")

inventory['pocket'] = ['key', 'knife', 'map']

inventory['gold'] = 750

print("\nHành trang sau cập nhật:")
print(f"Backpack: {inventory['backpack']}")
print(f"Vàng: {inventory['gold']}")
print(f"Túi: {inventory['pocket']}")
print(f"\nToàn bộ hành trang: {inventory}")

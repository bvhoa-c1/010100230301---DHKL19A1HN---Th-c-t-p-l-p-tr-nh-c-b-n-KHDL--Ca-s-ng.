warehouse_inventory = {'apple', 'banana', 'orange', 'grape', 'mango', 'lemon', 'kiwi', 'peach'}

print("Sản phẩm trong kho:")
print(warehouse_inventory)

customer_selected = set()
n = int(input("\nNhập số lượng sản phẩm khách hàng chọn mua: "))

for i in range(n):
    product = input(f"Nhập sản phẩm thứ {i+1}: ").lower()
    customer_selected.add(product)

print(f"\nSản phẩm khách hàng chọn: {customer_selected}")

not_selected = warehouse_inventory - customer_selected

print(f"\nSản phẩm trong kho nhưng chưa được khách hàng chọn mua:")
print(sorted(not_selected))

print(f"\nTổng số sản phẩm trong kho: {len(warehouse_inventory)}")
print(f"Số sản phẩm khách hàng chọn: {len(customer_selected)}")
print(f"Số sản phẩm chưa được chọn: {len(not_selected)}")

# Bài 7.10: Sử dụng Set để tìm mặt hàng trong kho nhưng chưa được chọn

# Danh mục sản phẩm trong kho (Set)
warehouse_products = {'apple', 'banana', 'orange', 'mango', 'grape', 'kiwi', 'peach'}

# Danh sách sản phẩm đã được khách hàng chọn mua (Set)
purchased_products = {'apple', 'orange', 'kiwi'}

print("Sản phẩm trong kho:")
print(warehouse_products)

print("\nSản phẩm khách hàng đã chọn mua:")
print(purchased_products)

# Tìm sản phẩm có trong kho nhưng chưa được chọn mua
# Sử dụng phép toán tập hợp: hiệu tập hợp (difference)
not_purchased = warehouse_products - purchased_products

print("\nSản phẩm trong kho nhưng chưa được chọn mua:")
print(not_purchased)

# Các phép toán tập hợp khác
print("\n" + "=" * 50)
print("CÁC PHÉP TOÁN TẬP HỢP:")
print("=" * 50)

# Hợp (union): tất cả sản phẩm
all_products = warehouse_products | purchased_products
print(f"Hợp (tất cả sản phẩm): {all_products}")

# Giao (intersection): sản phẩm vừa trong kho vừa được chọn
common_products = warehouse_products & purchased_products
print(f"Giao (trong kho và đã chọn): {common_products}")

# Sản phẩm chỉ khách hàng chọn nhưng không có trong kho
only_purchased = purchased_products - warehouse_products
print(f"Chỉ chọn mua (không có trong kho): {only_purchased}")

# Sản phẩm khác nhau giữa hai tập hợp
different = warehouse_products ^ purchased_products
print(f"Khác nhau (symmetric difference): {different}")

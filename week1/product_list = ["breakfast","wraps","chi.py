product_list = ["breakfast","wraps","chips", "pastries", ]
for i in enumerate(product_list):
    print(i)
idx_product = int(input("Product index that needs to be changed"))
upd_product = input("Put in updated product")
product_list[idx_product] = upd_product
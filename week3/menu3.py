print(" |Cafe Generation| " )
main_menu = int(input(" '0' To Exit App \n '1' To View Menu \n '2' To Create New Product \n '3' To Update Product \n '4' To Delete Product \n '5' To Access Product menu "))

drink_list = ["coffee","tea","hot chocolate"]

product_list = ["breakfast", "wraps", "chips", "pastries", ]

while main_menu != 0:
    if main_menu == 1:

        menu2 = int(input("1 for drinks, 2 for food: "))
        if menu2 == 1:
            print(drink_list)
        else:
            print(product_list)

    elif main_menu == 2:
        menu2 = int(input("1 to create new drink, 2 for new food: "))
        if menu2 == 1:
            new_drink = input("Add New Drink: ")
            drink_list.append(new_drink)
            print(drink_list)
        else:
            new_product = input("add new product: ")
            product_list.append(new_product)
            print(product_list)

    elif main_menu == 3:
        for i in enumerate(product_list):
            print(i)
        idx_product = int(input("Product index that needs to be changed: "))
        upd_product = input("Put in updated product")
        product_list[idx_product] = upd_product
        print(product_list)
    elif main_menu == 4:
        for i in enumerate(product_list):
            print(i)
        index_p = int(input( " choose index that needs to be deleted: "))
        del product_list[index_p]
        print(product_list)
    ans = input("would you like to continue or exit: ")
    if ans == "exit":
        exit()
    else:
        main_menu = int(input(" '0' To Exit App \n '1' To Access Menu \n '2' To Create New Product \n '3' To Update Product \n '4' To Delete Product: "))
    
            


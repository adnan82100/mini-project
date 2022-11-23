import Functions as func
shopping_basket = {}
order_status = 'preparing'
orders_list = []
func.products_order()
func.courier_order()
print(" |Cafe Generation| " )
main_menu = int(input(" '0' To Exit App \n '1' For Product Menu \n '2' For Order Menu \n '3' For Courier Menu \n >>>"))
while main_menu != 0:
    if main_menu == 1:

        Product_menu = int(input(" '0' To Exit App \n '1' To View Menu \n '2' To Create New Product \n '3' To Update Product \n '4' To Delete Product \n >>> "))
        
        while Product_menu != 0:
            if Product_menu == 1:
                print(func.product_list)
                Product_menu = int(input(" '0' To Exit App \n '1' To View Menu \n '2' To Create New Product \n '3' To Update Product \n '4' To Delete Product \n >>> "))
            elif Product_menu == 2:
                func.create_product()
                Product_menu = int(input(" '0' To Exit App \n '1' To View Menu \n '2' To Create New Product \n '3' To Update Product \n '4' To Delete Product \n >>> "))               
            elif Product_menu == 3:
               func.update_product()
               Product_menu = int(input(" '0' To Exit App \n '1' To View Menu \n '2' To Create New Product \n '3' To Update Product \n '4' To Delete Product \n >>> "))
            elif Product_menu == 4:
                func.delete_product()
                Product_menu = int(input(" '0' To Exit App \n '1' To View Menu \n '2' To Create New Product \n '3' To Update Product \n '4' To Delete Product \n >>> "))
        main_menu = int(input(" '0' To Exit App \n '1' For Product Menu \n '2' For Order Menu \n '3' For Courier Menu \n >>>"))


    elif main_menu == 2: #TODO: make a while loop to keep asking to add things to basket

        order_menu = int(input("""
        0 To Return to Main Menu
        1 To View Orders
        2 Add customer information
        3 to update existing order status
        4 to update order
        5 to delete order """))
        while order_menu != 0:
            if order_menu == 1:
                print(orders_list)
            elif order_menu == 2:
                customer_name = input("What is your name?: ")
                customer_address = input('what is your address?: ')
                customer_number = input('what is your number?:')
                shopping_basket['Customer Name: '] = customer_name
                shopping_basket['Customer Address: '] = customer_address
                shopping_basket['Customer Number'] = customer_number
                shopping_basket['order_status'] = order_status
                print(shopping_basket)
                orders_list.append(shopping_basket)
            elif order_menu == 3:
                update_status = input('what would you like to change Order Status too?')
                shopping_basket['order_status'] = update_status
                print(shopping_basket)
            elif order_menu == 4:
                for i in enumerate(orders_list):
                    print(i)
                    Change_o = int(input("which order would you like to change"))
                    print(orders_list[Change_o])
                    new_name = input("What is your name?: ")
                    new_address = input('what is your address?: ')
                    new_number = input('what is your number?:')
                    new_status = input('what is the status')
                    Dictionary2 = {'Customer Name:': new_name,'Customer Address:': new_address,'Customer Number:': new_number,'Order Status': new_status,}
                    orders_list[Change_o] = Dictionary2
                    print(orders_list)
            elif order_menu == 5:
                shopping_basket.clear()
                print(shopping_basket)
            order_menu = int(input(""" 0 To Return to Main Menu
                    1 To print Order 
                    2 Customer information
                    3 to update existing order status
                    4 to update order
                    5 to delete order
                    """))
        main_menu = int(input(" '0' To Exit App \n '1' For Product Menu \n '2' For Order Menu \n '3' For Courier Menu \n >>>"))
        
    if main_menu == 3:


        Courier_menu = int(input(" '0' To Exit To MainMenu \n '1' To View Courier \n '2' To Create New Courier \n '3' To Change Courier \n '4' To Delete Courier\n >>>"))
        # couriers menu ELSE IF user input is 2:
        while Courier_menu != 0:
            if Courier_menu == 1:
                print(func.Courier_list)
                Courier_menu = int(input(" '0' To Exit To MainMenu \n '1' To View Courier \n '2' To Create New Courier \n '3' To Change Courier \n '4' To Delete Courier\n >>>"))
                 #view courier
            elif Courier_menu == 2:
                func.create_courier()
                Courier_menu = int(input(" '0' To Exit To MainMenu \n '1' To View Courier \n '2' To Create New Courier \n '3' To Change Courier \n '4' To Delete Courier\n >>>"))
                 # create new courier
            elif Courier_menu == 3:
                func.update_courier()
                Courier_menu = int(input(" '0' To Exit To MainMenu \n '1' To View Courier \n '2' To Create New Courier \n '3' To Change Courier \n '4' To Delete Courier\n >>>"))
                #change courier
            elif Courier_menu == 4:
                func.delete_courier
                Courier_menu = int(input(" '0' To Exit To MainMenu \n '1' To View Courier \n '2' To Create New Courier \n '3' To Change Courier \n '4' To Delete Courier\n >>>"))
                #delete #courier
        main_menu = int(input(" '0' To Exit App \n '1' For Product Menu \n '2' For Order Menu \n '3' For Courier Menu \n >>>"))
else:
    ans = input("would you like to continue or exit: ")
    if ans == "exit":
        #save and quit
        func.close_save_people()
        func.close_save_product()
        exit()

            
                


    #     #courier Menu
    #     pass     
    # ans = input("would you like to continue or exit: ")
    # if ans == "exit":
    #     # SAVE products list to products.txt 
    #     # SAVE couriers list to couriers.txt
    # #save everything
    #     exit()
    
            


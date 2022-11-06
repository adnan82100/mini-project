# with open('products.txt', 'r') as f:
    # for line in f:
    #     print(line, end = "")
    
    # f_contents = f.read()
    # print(f_contents)
# with open('products.txt', 'a') as f:
def view():
    with open('products123.txt', 'r') as f:
        for line in f.readlines():
            print(line.rstrip())

def change():
    with open('products123.txt', 'r' ) as f:
        lines = f.readlines()
        new_list = []
        for line in lines:
            new_list.append(line.strip())
        print(new_list)

    with open('products123.txt','w') as f:
        f.write(new_list)
        product_index = int(input('Product index that you would like to change: '))
        new_product = input('what would you like to change it to: ')
        new_list[product_index - 1] = new_product



def add():
    with open('products123.txt', 'r+') as f:
        lines = f.readlines()
        print(lines)
        products = input("add product: ")
        f.write(products + "\n")

def delete():
    with open('products.txt', 'r+') as f:
        pass
change()

# .strip("\n")

# f = open('products.txt', 'r')

# print(f.name)

# f.close()
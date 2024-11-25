from .supplier_screen import supplier_data_base
from .suit import Suit

input_text = '''1. Add product
2. Remove product
3. View product list
4. Return'''

product_data_base = []


def Product_menu():
    while True:
        print(input_text)

        action_input = input('Please select an option: ')

        option = None

        try:
            option = int(action_input)
        except ValueError:
            print("Invalid Option, ending execution")
            break

        if option == 4:
            break
        elif option == 1:
            code = input("Please insert product code: ")
            description = input("Please insert a description of the product: ")
            size = input("Please insert product size: ")
            supplier = input("Please insert supplier's name: ")
            purchase_price = input("Please insert the product's purchase price: ")
            selling_price = input("Please insert the product's selling price: ")
            for i in range(len(supplier_data_base)):
                check_supplier = supplier_data_base[i]
                if supplier == check_supplier.name:
                    product_data_base.append(Suit(code, description, int(size), supplier, float(purchase_price), float(selling_price)))
                    break
                else:
                    print("This supplier is not on the supplier database, please include this supplier on the database before registering this product")

        elif option == 2:
            code = input('Please insert the code of the product you wish to remove: ')
            removed_product = None
            for d in range(len(product_data_base)):
                suit = product_data_base[d]
                if suit.code == code:
                    removed_product = product_data_base.pop(d)
                    break
            if removed_product == None:
                print("This product is not on the database")

        elif option == 3:
            print("Products in the database: ")

            for c in product_data_base:
                data = '''Code: {code}
    Description: {description}
    Size: {size}
    Supplier: {supplier}
    Purchase price: {purchase_price}
    Selling price: {selling_price}'''.format(code = c.code, description = c.description, size = c.size, supplier = c.supplier, purchase_price = c.purchase_price, selling_price = c.selling_price)
                print(data)

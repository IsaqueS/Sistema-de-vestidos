import client_screen
import rental_screen
import supplier_screen
import product_screen

input_text = '''1. Clients
2. Suppliers
3. Products
4. Rentals
5. Exit'''


while True:
    print(input_text)


    action_input = input("Please select an option: ")

    option = None

    try:
        option = int(action_input)
    except ValueError:
        print("Invalid Option, ending execution")
        break
    if option == 5:
        print('Goodbye!')
        break
    elif option == 1:
        client_screen.Client_menu()
    elif option == 2:
        supplier_screen.Supplier_menu()
    elif option == 3:
        product_screen.Product_menu()
    elif option == 4:
        rental_screen.Rental_menu()




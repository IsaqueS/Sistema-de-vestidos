from DataBackend.Controls import client_control
from DataBackend.Controls import rental_control
from DataBackend.Controls import supplier_control
from DataBackend.Controls import suit_control

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
        client_control.ClientControl()
    elif option == 2:
        supplier_control.SupplierControl()
    elif option == 3:
        suit_control.SuitControl()
    elif option == 4:
        rental_control.RentalControl()

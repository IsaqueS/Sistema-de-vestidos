from DataBackend.Controls.client_control import ClientControl
from DataBackend.Controls.rental_control import RentalControl
from DataBackend.Controls.suit_control import SuitControl
from DataBackend.Controls.supplier_control import SupplierControl

input_text = '''Select an option: 
1. Clients
2. Suppliers
3. Products
4. Rentals
5. Exit'''

if __name__ == "__main__":

    suit_control: SuitControl = SuitControl()
    client_control: ClientControl = ClientControl()
    supplier_control: SupplierControl = SupplierControl()
    rental_control: RentalControl = RentalControl()

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
            client_control.start_client_screen()
        elif option == 2:
            supplier_control.start_supplier_screen()
        elif option == 3:
            suit_control.start_product_screen()
        elif option == 4:
            rental_control.start_rental_screen()

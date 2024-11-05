import datetime
from rental import Rental
from client_screen import data_base
from product_screen import product_data_base

input_text = '''1. Rent product
2. Return product
3. View rental list
4. Return'''

rental_data_base = []


def Rental_menu():
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
            date = datetime.datetime.now()
            wait_time = datetime.datetime(int(input("Year of return: ")), int(input("Month of return: ")), int(input("Day of return: ")))
            products = []
            client = input("Please insert the client's name: ")

            for i in range(len(data_base)):
                check_client = data_base[i]
                if client == check_client.name:
                    rental_data_base.append(Rental(date, wait_time, products, client))
                    break
                else:
                    print("Client not in database, please register client before renting")


        elif option == 2:
            codigo_removido = input('Insert code of rental undone')
            for c in range(len(rental_data_base)):
                if codigo_removido == rental_data_base[c].rent_code:
                    rental_data_base.pop(c)
                    break
                else:
                    print("There is no rental with this code")
                    break

        elif option == 3:
            print("Active rentals in database: ")

            for d in rental_data_base:
                data = '''Code: {rent_code}
    Date: {date}
    Wait_time: {wait_time}
    Products: {products}
    Client: {client}'''.format(rent_code = d.rent_code, date = d.date, wait_time = d.wait_time, products = d.products, client = d.client)
                print(data)

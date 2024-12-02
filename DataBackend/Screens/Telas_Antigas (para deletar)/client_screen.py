import datetime
from .Controladores import client_control


input_text = '''1. Add client
2. Remove client
3. View client list
4. Return'''

data_base = []

def Client_menu():
    while True:
        print(input_text)
        action_input = input("Select you action: ")
        option = None
        try:
            option = int(action_input)
        except ValueError:
            print("Invalid Option, ending execution")
            break
        if option == 4:
            break
        elif option == 1:
            name = input("please enter the client's name: ")
            number = input("please enter the client's number: ")
            email = input("please enter the client's email: ")
            instagram = input("please enter the client's instagram (leave empty it does not have it): ")
            cpf = input("please enter the client's cpf: ")
            birth_date = datetime.datetime(int(input("year of birth: ")),int(input("month of birth: ")),int(input("day of birth: ")))
            data_base.append(Client(name,int(number),email,instagram,int(cpf),birth_date))
        elif option == 2:
            name = input("please input the client name you want to remove: ")
            removed_client = None
            for i in range(len(data_base)):
                client = data_base[i]
                if client.name == name:
                    removed_client = data_base.pop(i)
                    break
            if removed_client == None:
                print("This name does not exist on the data base")
        elif option == 3:
            print("Clients on the data base: ")
            for c in data_base:
                data = '''Name: {name}
        Number: {number}
        Email: {email}
        Instagram: {instagram}
        CPF: {cpf}
        Birth Date: {birth_date}
        Registration Date: {registration_date}
    
                '''.format(name = c.name,number = c.number, email = c.email, instagram = c.instagram, cpf = c.cpf, birth_date = c.birth_date, registration_date = c.registration_date)
                print(data)
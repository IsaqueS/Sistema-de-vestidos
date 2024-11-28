from Classes.supplier import Supplier

imput_text = '''1. Add supplier
2. Remove supplier
3. View supplier list
4. Return'''

supplier_data_base = []

def Supplier_menu():
    while True:
        print(imput_text)
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
            name = input("Please insert the supplier's name: ")
            number = input("Please insert the supplier's number: ")
            email = input("Please insert the supplier's e-mail: ")
            contact = input("Please insert the supplier's contact information: ")
            cnpj = input("Please insert the supplier's cnpj: ")
            address = input("Please insert the supplier's address: ")
            website = input("Please insert the supplier's website: ")
            supplier_data_base.append(Supplier(name, int(number), email, contact, int(cnpj), address, website))
        elif option == 2:
            name = input('Please insert the name of the supplier you wish to remove: ')
            removed_supplier = None
            for i in range(len(supplier_data_base)):
                supplier = supplier_data_base[i]
                if supplier.name == name:
                    removed_supplier = supplier_data_base.pop(i)
                    break
            if removed_supplier == None:
                print("This supplier is not on the database")
        elif option == 3:
            print("Suppliers in the database: ")
            for c in supplier_data_base:
                data = '''Name: {name}
    Number: {number}
    E-mail: {email}
    Contact: {contact}
    CNPJ: {cnpj}
    Address: {address}
    Website: {website}'''.format(name = c.name,number = c.number, email = c.email, contact = c.contact, cnpj = c.cnpj, address = c.address, website = c.website)
                print(data)
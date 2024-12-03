import json


database = "module_5\project\contact_management_system\database\contact_data.json"

def load_contact():
    try:
        with open(database, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print('File not found')


def save_contact(contact):
    with open(database,'w') as file:
        json.dump(contact,file,indent=4)

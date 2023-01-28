import json
data = {
    'Frodo': '12345678',
    'Sam': '87654321',
    'Mari': '18273645',

}

with open(r'file', 'w+') as file:
    data = json.dumps(data)
    file.write(data)
    print('Open file')
with open(r'file', 'r+') as file:
    file_dict = file.read()
    file_dict = json.loads(file_dict)

while True:
    contacts = input('Enter your contact:')
    if contacts == 'list':
        print(file_dict)
    elif contacts == 'stats':
        print(f'You have {len(file_dict)} contacts.')
    elif contacts == 'add':
        new_contacts = input('Enter new contact: ')
        key = new_contacts
        with open(r'file', 'r+') as file:
            file_dict = file.read()
            file_dict = json.loads(file_dict)
        if key in file_dict:
            print(f'This contact already exist.')
        else:
            number = input('Enter number: ')
            num = int(number)
            file_dict[key] = num
            with open(r'file', 'w+') as file:
                file_dict = json.dumps(file_dict)
                file.write(file_dict)
                file_dict = json.loads(file_dict)
            print(f'Add new contact: {key} {num}')
    elif contacts == 'delete':
        del_con = input('Enter the name of the contact you want to delete: ')
        with open(r'file', 'r+') as file:
            file_dict = file.read()
            file_dict = json.loads(file_dict)
        if del_con in file_dict:
            del file_dict[del_con]
            with open(r'file', 'w+') as file:
                file_dict = json.dumps(file_dict)
                file.write(file_dict)
                file_dict = json.loads(file_dict)
            print(f'Contact delete.')
        else:
            print('This contact does not exist')
    elif contacts == 'show':
        show = input('Name contact:')
        if show in file_dict:
            print(f'Name: {show} \nNumber: {file_dict[show]}')
        else:
            print('This contact does not exist.')

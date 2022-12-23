new_dic = {
    'Frodo': '+12345678',
    'Sam': '+87654321',
    'Mari': '+18273645',
}

while True:
    contacts = input('Enter contact: ')
    con = contacts.split()

    if contacts == 'list':
        print(list(new_dic))
    elif contacts == 'stats':
        print('You have ' + str(len(new_dic)) + ' contacts.')
    elif contacts == 'add':
        new_contacts = input('Enter new contacts: ')
        key = new_contacts.split()
        if key[0] in new_dic:
            print('This contact already exists.')
        else:
            new_dic[key[0]] = key[1]
            print('Contact ' + key[0] + ' saved.')
    elif con[0] == 'delete':
        if con[1] in new_dic:
            del new_dic[con[1]]
            print(con[1] + ' delete.')
        else:
            print('Non-existent contact.')
    elif con[0] == 'show':
        print('Name contacts: ' + con[1] + '\nNumber contacts: ' + new_dic[con[1]])
    else:
        print('Contact don`t exist.')
    print(new_dic)

while True:
    contacts = input('Enter contact: ')
    con = contacts.split()

    new_dic = {
        'Frodo': '+12345678',
        'Sam': '+87654321',
        'Mari': '+18273645',
    }

    if contacts == 'list':
        print(list(new_dic))

    elif contacts == 'stats':
        print('You have ' + str(len(new_dic)) + ' contacts.')
    elif contacts == 'add':
        new_contacts = input('Enter new contacts: ')
        con_split = new_contacts.split()
        name = con_split[0]
        number = con_split[1]
        new_dic[name] = number
    elif con[0] == 'delete':
        con_del = con[1]
        del new_dic[con[1]]
        print('Contact delete.')
    elif con[0] == 'show':
        print('Name contacts: ' + con[1] + '\nNumber contacts: ' + new_dic[con[1]])
    else:
        print('Contact don`t exist.')
    print(new_dic)
text = input('Enter your text: ')
for item in text:
    print(item)
    if item.isdigit():
        print('This is digit.')
        if int(item) % 2 == 0:
            print('This is even.')
        else:
            print('This is add.')
    elif item.isalnum():
        print('This is letter.')
        if item.istitle():
            print('Big letter.')
        else:
            print('Small letter.')
    else:
        print('Symbol.')
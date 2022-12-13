text = input('Enter your text: ')
if text.isdigit():
    text = int(text)
    print(str(text)+' it`s numeric.')
    print(type(text))
    if text % 2 == 0:
        print(str(text) + ' it`s even.')
    else:
        print(str(text) + ' it`s add.')
else:
    print(str(text)+' it`s word.')
    print(type(text))
    print(str(len(text))+' letters.')

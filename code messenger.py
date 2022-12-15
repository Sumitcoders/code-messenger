import random


print('Welcome to the Coder and Decoder')
c = int(input('press 1 to turn your message into code \npress 2 to decode a code into the message: '))


def coding(message,passcode = ''):
    if passcode == '':
        for i in range(5):
            passcode = passcode + str(random.randint(1,9))
    
    l = [passcode[0],passcode[1],passcode[2],passcode[3],passcode[4]]
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
    turn = 0
    f_message = ''
    for i in range(len(message)):

        
        c_letter = message[i]
        if c_letter != ' ':
            pos = alphabets.index(c_letter) + int(l[turn])

            if pos > len(alphabets) - 1:
                pos = pos - (len(alphabets))


            
            f_letter = alphabets[pos]
            f_message = f_message + str(f_letter)
        else:
            f_message = f_message + ' '
        turn += 1
        if turn > 4:
            turn = 0
    print('Here is the coded message')
    print(f'"{f_message}"')
    print(f'Passcode = {passcode}')







def decoding(passcode,message):
    passcode = str(passcode)
    if len(passcode) != 5:
        print('Invalid passcode')
        return
    l = [passcode[0],passcode[1],passcode[2],passcode[3],passcode[4]]

    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
    turn = 0
    f_message = ''
    for i in range(len(message)):

        
        c_letter = message[i]
        if c_letter != ' ':
            pos = alphabets.index(c_letter) - int(l[turn])

            if pos < 0:
                pos = (len(alphabets)) + pos

            f_letter = alphabets[pos]
            f_message = f_message + str(f_letter)
        else:
            f_message = f_message + ' '
        turn += 1
        if turn > 4:
            turn = 0
    return print(f_message)

if c == 1:
    print('Enter your message below (a-z only)')
    message = input('')
    i = str(input('do you want any custom passcode? (yes/no): '))
    if i == 'yes':
        pasc = int(input('Enter your custom numeric passcode: '))
        pasc = str(pasc)
        coding(message = message,passcode= pasc)
    else:
        coding(message = message)
elif c == 2:
    print('Enter the code of your message below(a-z only)')
    code = input('')
    passcode = input('Enter the passcode: ')
    decoding(passcode= passcode, message= code)






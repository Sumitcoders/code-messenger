import random

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
    return f_message,passcode








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
    return f_message




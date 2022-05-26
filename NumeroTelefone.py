def isPhoneNumber(text):    
    if len(text) != 9:
        return False
    for i in range(0, 4):
        if not text[i].isdecimal():
            return False
        if text[4] != '-':
            return False
    for i in range(5, 9):
        if not text[i].isdecimal():
            return False
    return True
def isCellNumber(text):
    if len(text) != 10:
        return False
    for i in range(0, 5):
        if not text[i].isdecimal():
            return False
        if text[5] != '-':
            return False
    for i in range(6, 10):
        if not text[i].isdecimal():
            return False
    return True
def cellORphone(number):
    print(number[0])
    if number[0]!=9:
        print(number, ' é um número de telefone:')
        print(isPhoneNumber(number))   
    elif number[0] == 9:
        print(number, ' é um número de celular:')
        print(isCellNumber(number))
number = input('Digite o número de telefone: ')
cellORphone(number)



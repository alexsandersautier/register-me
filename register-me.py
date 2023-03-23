from datetime import datetime
import random

def is_register(choice):
    if choice =='y':
        return True
    else:
        return False

def message(user,date_register,card):
    print(f'''
    Olá {user}, seu registro foi concluído com sucesso no dia {date_register.strftime('%d/%m/%Y')}.
    Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de {card}
    ''')

what = ['y','n']

option = random.choice(what) #input('Do want create new user? (y/n)')

options = is_register(option)

#test automatic
names = ['alexsander','jhonatan','micael']
ages = [25,29,24]
birthdays = ['24/10/1997', '25/11/1998', '15/09/1994']
cards = ['R$50,00','R$250,00','R$120,00']
birth = True

while options:
    user = random.choice(names) # user = capitalize(input('Type new user: '))
    age = random.choice(ages) # age = int(input('Type age of user'))
    date_register = datetime.now()
    card = random.choice(cards)
    birthday = random.choice(birthdays)

    '''
    while True:
        try:
            birthday = datetime.strptime(input('Type your birthday in format DD/MM/YYYY: '), '%d/%m/%Y')
            break
        except:
            print('Date in format incorrect')
            continue
    '''        


    message(user, date_register, card)

    option = random.choice(what) #input('Do want create new user? (y/n)')

    options = is_register(option)
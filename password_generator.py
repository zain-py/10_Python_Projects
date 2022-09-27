import string
import random

characters = list(string.ascii_letters + string.digits + "!$&~@#()^*%")

def generate_password():
    
    password_length = int(input("How long would you like the password to be? "))
    
    random.shuffle(characters)
    
    password = []
    
    for i in range(password_length):
        password.append(random.choice(characters))
        
    random.shuffle(password)
    
    password = ''.join(password)
    
    print()
    return print(password)


option = input('Do you want to generate password?[y/n]: ')

if option.lower() == 'y':
    print()
    generate_password()
elif option.lower() == 'n':
    print('\nProgram Terminated!')
    quit()
else:
    print('\nInvalid Input!')
    quit()

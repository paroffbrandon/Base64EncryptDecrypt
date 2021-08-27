import base64_e
import base64_d
from os import system, name

def clear_screen():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

while True:
    clear_screen()

    print("Welcome to my Base64 Encrypter / Decrypter!\n")

    ansBa = input("What Operation would you like to do? \n1. Encrypting \n2. Decrypting\n")
    if (ansBa == "1"):
        base64_e.base64E()
    elif (ansBa == "2"):
        base64_d.base64D()

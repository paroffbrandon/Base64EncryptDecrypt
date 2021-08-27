import base64
import pyperclip
from os import system, name

def clear_screen():
    if name == 'nt':
        system('cls')
    else:
        system('clear')
def base64D():
    while True:
        clear_screen()

        print("Welcome to my Base64 Decrypter! This is very basic and just to test if I can do it.\n")

        base64_message = input("What message do you want to decrypt?\n")
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')

        print(message)
        pyperclip.copy(message)
        answer = input('\nPress enter to continue, type exit to go back\n')
        if (answer == "exit"):
            break
        elif (answer != "exit"):
            print('ok')

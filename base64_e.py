import base64
import pyperclip
from os import system, name

def clear_screen():
    if name == 'nt':
        system('cls')
    else:
        system('clear')
def base64E():
    while True:
        clear_screen()

        print("Welcome to my Base64 Encrypter! This is very basic and just to test if I can do it.\n")

        message = input("What message do you want to encrypt?\n")
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')

        print(base64_message)
        pyperclip.copy(base64_message)
        answer = input('\nPress enter to continue, type exit to go back\n')
        if (answer == "exit"):
            break
        elif (answer != "exit"):
            print('ok')

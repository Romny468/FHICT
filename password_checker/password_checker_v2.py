# import defenition from other file
from passwdCheck_v1 import passwdCheck

# program beginning
passwd = input("Give me your password and I will check it for toughness: ")
while True: 
    if (passwdCheck(passwd)): 
        print("\npassword it secure enough, for now")
        break
    else: 
        passwd = input("\npassword not secure, try again: ")

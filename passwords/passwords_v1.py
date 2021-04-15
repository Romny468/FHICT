#this is a password checker and a password generator
#this program will ask the user whether the user wants to generate or check a password

# this function is used to generate passwords
def passwordGenerate():
    try:
        import string, random
        print("This is a password generator","\nYou can create a random password with this program")
        # ask how long the password should be with some checks
        while True:
            characters = input("\nhow many characters should the password be? ")
            if characters.isdigit():
                if int(characters) > 100:
                    check("\nare you sure you want a password bigger than 100 characters?")
                    pass_length = int(characters)
                    break
                else:
                    pass_length = int(characters)
                    break
            elif characters == "":
                pass_length = 10
                break
            else: print("\nyou must type a number, try again.")

        # ask if the user wants numbers and special characters in the password with a self-made check function
        numbers = check("\ndo you wish to have numbers in the password?")
        characters = check("\ndo you wish to have special characters in the password?")

        #the password will be gererated here based on the user answers
        if numbers == True and characters == True:
            char = string.ascii_letters + string.punctuation + string.digits
            password = "".join(random.choice(char) for i in range(pass_length))
            print("The generated password is: " + password)
        elif numbers == True and characters == False:
            char = string.ascii_letters + string.digits
            password = "".join(random.choice(char) for i in range(pass_length))
            print("The generated password is: " + password)
        elif numbers == False and characters == True:
            char = string.ascii_letters + string.punctuation
            password = "".join(random.choice(char) for i in range(pass_length))
            print("The generated password is: " + password)
        else:
            char = string.ascii_letters
            password = "".join(random.choice(char) for i in range(pass_length))
            print("\nThe generated password is: " + password)
    except:
        print("an error occured while loading one or more libraries!")
        pass

# check function to make sure the user answers a question with "y" or "n" ("y" is preselected)
def check(question):
    while True:
        check1 = input(question + " ([y]/n): ")
        if check1 == "y":
            return True
        elif check1 == "n":
            return False
        elif check1 == "":
            return True
        else:
            print('\nthe question must be answered with "y" or "n"')

# this function is used to check the password security on length, lower case, upper case, digits and special chars
def passwdCheck(passwd):
    try:
        import string
        passworderror = "Your password is missing the following:"
        if len(passwd) < 8: passworderror = passworderror + "\n - at least 8 characters"
        if not any(char.islower() for char in passwd): passworderror = passworderror + "\n - one lower case character"
        if not any(char.isupper() for char in passwd): passworderror = passworderror + "\n - one upper case character"
        if not any(char.isdigit() for char in passwd): passworderror = passworderror + "\n - one digit"
        if not any(char in string.punctuation for char in passwd): passworderror = passworderror + "\n - one special character"
        if passworderror == "Your password is missing the following:": return True
        else: print("\n", passworderror,sep="")
    except: pass

# passwword check setup and final.
def passwordChecker():
    passwd = input("Give me your password and I will check it for toughness: ")
    while True: 
        if (passwdCheck(passwd)): 
            print("\npassword it secure enough, for now")
            break
        else:
            answer1 = check("\npassword not secure, would you want to try another password?")
            if answer1 == True: passwd = input("\nGive me another password and I will check it for toughness: ")
            elif answer1 == False: break

# main function to ask what the user wants to do
def main():
    print("What would you like me to do?", "\n\n 1: Check \n 2: generate")
    answer = input("Choose an option: ")
    while True:
        if answer in ("1", "check", "Check"):
            print("\nYou chose option 1: password check.")
            passwordChecker()
            break
        elif answer in ("2", "generate", "Generate"):
            print("\nYou chose option 2: generate password.")
            passwordGenerate()
            break
        else: answer = input("I did not understand your wish, answer again: ")

    while True:
        answer2 = check("\nWould you like me to do something else?")
        if answer2 == True: main()
        else:
            print("\nGoodbye!")
            exit()

print("Hello, I am able to check and generate passwords.")
main()

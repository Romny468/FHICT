try:
    import string
    import random
except:
    print("an error occured while loading one or more libraries!")
    print("exiting...")
    exit()

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

print("This is a password generator","\nYou can create a random password with this program")
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

numbers = check("\ndo you wish to have numbers in the password?")
characters = check("\ndo you wish to have special characters in the password?")

#the password will be gererated here
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
    print("The generated password is: " + password)

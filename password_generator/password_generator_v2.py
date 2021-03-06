import string
import random

print("This is a password generator","\nYou can create a random password with this program")
while True:
    characters = input("\nhow many characters should the password be? ")
    if characters.isdigit():
        pass_length = int(characters)
        break
    elif characters == "":
        pass_length = 10
        break
    else: print("\nyou must type a number. try again")
#to check for digits i found this on the internet:
    #string.isdigit()
    #Parameters:
    #isdigit() does not take any parameters
    #Returns :
    #1.True- If all characters in the string are digits.
    #2.False- If the string contains 1 or more non-digits.
#URL: https://www.geeksforgeeks.org/python-string-isdigit-application/

def check(string1, string2):
    while True:
        if string1 == "y":
            break
        elif string1 == "n":
            break
        elif string1 == "":
            string1 = "y"
            print(string1)
            break
        else:
            print('\nthe question must be answered with "y" or "n"')
            string1 = input("do you wish to have " + string2 + " in the password? ([y]/n): ")
            check(string1, string2)
            break

numbers = input("\ndo you wish to have numbers in the password? ([y]/n): ")
check(numbers, "numbers")
print(numbers)
characters = input("\ndo you wish to have special characters in the password? ([y]/n): ")
check(characters, "special characters")
print(characters)

print(numbers, characters)

#to generate password i found this
    #import random
    #import string
    #def get_random_string(length):
        ## choose from all lowercase letter
        #letters = string.ascii_lowercase
        #result_str = ''.join(random.choice(letters) for i in range(length))
        #print("Random string of length", length, "is:", result_str)
#URL: https://pynative.com/python-generate-random-string/
#the following part of the script has been made from found URL
#the password will be gererated here
if numbers == "y" and characters == "y":
    char = string.ascii_letters + string.punctuation + string.digits
    password = "".join(random.choice(char) for i in range(pass_length))
    print("The generated password is: " + password)
elif numbers == "y" and characters == "n":
    char = string.ascii_letters + string.digits
    password = "".join(random.choice(char) for i in range(pass_length))
    print("The generated password is: " + password)
elif numbers == "n" and characters == "y":
    char = string.ascii_letters + string.punctuation
    password = "".join(random.choice(char) for i in range(pass_length))
    print("The generated password is: " + password)
else:
    char = string.ascii_letters
    password = "".join(random.choice(char) for i in range(pass_length))
    print("The generated password is: " + password)

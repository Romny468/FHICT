secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
#initialise
number = 0

#read the number
number = int(input("Type in a number:"))


while number != 0:
    if number == secret_number:
        print("Well done, muggle! You are free now.")
        exit()
    else:
        print("Ha ha! You're stuck in my loop!")
        number = int(input("Try a new number:"))
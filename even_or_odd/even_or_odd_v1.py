# this program will determine whether the given number is even or odd
print("this program will determine whether the given number is even or odd")

loop = True
#ask number
number = input("give me a number to check: ")

while loop:
    #checks
    if number == "q":
        #this will exit the loop
        loop = False
        print("\nBye!")
        break
    else:
        #this checks if the input is an integer
        try:
            int(number)
            number = int(number)
            check = True
        except ValueError:
            print(number, "is not a number, you stoopid.")
            check = False
            number = input("\ngive me a number or type q to quit: ")

    #maths
    if check == True:
        if number % 2 == 0:
            print(number, "is an even number")
            number = input("\ngive me another number or type q to quit: ")
        else:
            print(number, "is an odd number")
            number = input("\ngive me another number or type q to quit: ")

#this program will generate validated BSN
import random

#generate the bsn numbers
def bsnGen():
    while True:
        chars = random.sample(range(0, 9), 9)
        a, b, c, d, e, f, g, h, i = 9*chars[0], 8*chars[1], 7*chars[2], 6*chars[3], 5*chars[4], 4*chars[5], 3*chars[6], 2*chars[7], -1*chars[8]
        som = a + b + c + d + e + f + g + h + i
        check = som % 11

        if check == 0:
            print(chars[0], chars[1], chars[2], chars[3], chars[4], chars[5], chars[6], chars[7], chars[8], sep="")
            break
        else: continue

#ask question and check for right answer
def check(question):
    while True:
        check1 = input(question + " (y/[n]): ")
        if check1 == "y": return True
        elif check1 == "n": return False
        elif check1 == "": return False
        else: print('\nthe question must be answered with "y" or "n"!')

#program beginning
#ask how many bsn numbers the user wants and check
print("my purpose in life is to generate bsn numbers")
while True:
    many = input("how many bsn numbers would you like? ")
    if many.isdigit():
        many = int(many)
        break
    else: print("\nyou must type a number, try again.")

#print as many numbers as user wanted
print("\nthe generated bsn numbers are:")
for x in range(many):
    bsnGen()

#ask if user wants more bsn numbers
while True:
    new = check("\ndo you want some more BSN numbers?")
    if new is True:
        many = int(input("how many bsn numbers would you like? "))
        print("\nthe generated bsn numbers are:")
        for x in range(many):
            bsnGen()
    else:
        print("it was nice doing business with you.")
        break

#this program will generate validated BSN
import random

def bsnGen():
    while True:
        chars = random.sample(range(0, 9), 9)
        a = 9*chars[0]
        b = 8*chars[1]
        c = 7*chars[2]
        d = 6*chars[3]
        e = 5*chars[4]
        f = 4*chars[5]
        g = 3*chars[6]
        h = 2*chars[7]
        i = -1*chars[8]
        som = a + b + c + d + e + f + g + h + i
        check = som % 11

        if check == 0:
            print(chars[0], chars[1], chars[2], chars[3], chars[4], chars[5], chars[6], chars[7], chars[8], sep="")
            break
        else:
            continue

def check(question):
    while True:
        check1 = input(question + " (y/[n]): ")
        if check1 == "y":
            return True
        elif check1 == "n":
            return False
        elif check1 == "":
            return False
        else:
            print('\nthe question must be answered with "y" or "n"!')

print("my purpose in life is to generate bsn numbers")
many = int(input("how many bsn numbers would you like? "))
print("\nthe generated bsn numbers are:")
for x in range(many):
    bsnGen()

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

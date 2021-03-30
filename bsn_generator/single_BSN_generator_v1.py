#this program will generate validated BSN
import random

def bsnGen():
    while True:
        chars = []
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
            print("the generated BSN is: ", chars[0], chars[1], chars[2], chars[3], chars[4], chars[5], chars[6], chars[7], chars[8], sep="")
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

print("this is bsn generator")
bsnGen()

while True:
    next = check("\ndo you want another BSN number?")
    if next is True: bsnGen()
    else:
        print("it was nice doing business with you.")
        break

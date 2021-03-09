
word = input("enter a word: ")
while word != 0:
    if word == "chupacabra":
        print("You've successfully left the loop.")
        break
    else:
        print("Ha! You're in a loop till you find the secret word")
        word = input("\ntry again, enter another word: ")
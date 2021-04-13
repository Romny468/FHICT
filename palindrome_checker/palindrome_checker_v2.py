#This is a palindrome checker
def palindromeCheck():
    string = input("enter a word: ")
    for i in range(0, int(len(string)/2)):
        if string[i] != string[len(string)-i-1]: return False
    return True

#program beginning
print("i am a programmed to check if a word is a palindrome")
ans = palindromeCheck()
if ans: print("your input is a palindrome!")
else: print("your input is not a palindrome")

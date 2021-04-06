import string

# check password security
def passwdCheck(passwd):
    passworderror = "Your password is missing the following:"
    if len(passwd) < 8: passworderror = passworderror + "\n + at least 8 characters"
    if not any(char.islower() for char in passwd): passworderror = passworderror + "\n + at least one lower case character"
    if not any(char.isupper() for char in passwd): passworderror = passworderror + "\n + at least one upper case character"
    if not any(char.isdigit() for char in passwd): passworderror = passworderror + "\n + at least one digit"
    if not any(char in string.punctuation for char in passwd): passworderror = passworderror + "\n + at least one special character"
    if passworderror == "Your password is missing the following:": return True
    else: print("\n", passworderror,sep="")

# program beginning
passwd = input("Give me your password and I will check it for toughness: ")
while True: 
    if (passwdCheck(passwd)): 
        print("\npassword it secure enough, for now")
        break
    else: 
        passwd = input("\npassword not secure, try again: ")

import string

def passwdCheck(passwd):
    passwd = input("Give me your password and I will check it for toughness: ")
    passworderror = "Your password is missing the following:"
    if len(passwd) < 8: passworderror = passworderror + "\n + at least 8 characters"
    if not any(char.islower() for char in passwd): passworderror = passworderror + "\n + at least one lower case character"
    if not any(char.isupper() for char in passwd): passworderror = passworderror + "\n + at least one upper case character"
    if not any(char.isdigit() for char in passwd): passworderror = passworderror + "\n + at least one digit"
    if not any(char in string.punctuation for char in passwd): passworderror = passworderror + "\n + at least one special character"
    if passworderror == "Your password is missing the following:": return True
    else: print("\n", passworderror,sep="")

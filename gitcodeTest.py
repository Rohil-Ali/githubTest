print("Welcome to my test website\nPlease sign in")

while True:
    user_name = input("Username: ")
    if user_name[0].isupper() == False:
        print("Username is invalid, Uppercase character is needed at the beginning.")
    else:
        break


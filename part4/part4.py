def Registration():
    print("== Registration ==")
    Username = input("Username: ")
    Password= input("Password: ")
    Repeat_password = input("Repeat_password: ")
    while Password != Repeat_password:
        print("Passwords not match. Please input again.")
        Repeat_password= input ("Repeat_password: ")

    Email = input("Email: ")
    print("Registered successfully.")

Registration()
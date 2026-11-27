while True:
    password = input("Enter password (stop to exit): ")

    if password == "stop":
        print("Program stopped")
        break

    upper = any(ch.isupper() for ch in password)
    lower = any(ch.islower() for ch in password)
    digit = any(ch.isdigit() for ch in password)

    if len(password) >= 8 and upper and lower and digit:
        print("Strong Password")
    else:
        print("Weak Password")
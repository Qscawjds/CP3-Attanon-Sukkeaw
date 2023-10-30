username = input("Username : ")
password = input("Password : ")
if username == "Beta01" and password == "225547" :
    print("Welcome to restaurant !")
    print("This is the menu you can order.")
    print("1.Khaopadkrapao 50 THB")
    print("2.Khaomankai    55 THB")
    print("3.Khaopadtalea  60 THB")
    print("4.Water         10 THB")
    SelectMenu = int(input("Please select menu. >> "))
    Amount = int(input("How many do you want? >> "))
    if SelectMenu == 1:
        print("Total Payment : ",50*Amount,"THB")
    elif SelectMenu == 2:
        print("Total Payment : ",55*Amount,"THB")
    elif SelectMenu == 3:
        print("Total Payment : ",60*Amount,"THB")
    elif SelectMenu == 4:
        print("Total Payment : ",10*Amount,"THB")
    else:
        print("Invalid number of menu.")
    print("Thank you for using the service.")
else:
    print("Invaild Username or Password.")


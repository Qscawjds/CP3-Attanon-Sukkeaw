def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "Beta01" and passwordInput == "225547":
        return showMenu()
    else:
        print("Invaild Username or Password.")
        return login()

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()

def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        return vatCalculator(totalPrice = int(input("Total Price : ")))
    elif userSelected == 2:
        return priceCalculator()
    else:
        print("Invalid number of menu.")
        return menuSelect()
    
def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

print(login())


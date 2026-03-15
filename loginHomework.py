def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        exit()

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()

def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        return vatCalculator(int(input("Total Price : ")))
    if userSelected == 2:
        return priceCalculator()

def vatCalculator(totalPrice):
    result = totalPrice*1.07
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    print("Total =",price1 + price2)
    return vatCalculator(price1 + price2)

print(login())
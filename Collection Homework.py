def showBill():
    print("---- MY FOOD ----")
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
        print("Total =",sum(priceList))
    exit()

menuList = []
priceList = []
while True:
    menuName = input("Enter your menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()
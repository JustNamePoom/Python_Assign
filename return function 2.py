def vatcalculate(totalPrice):
    result = (totalPrice*1.07)
    return result
print("----- Vat Calculator-----")
print(vatcalculate(int(input("Insert Total Price : "))))
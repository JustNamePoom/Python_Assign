"""
ในการเข้าใช้งานโปรแกรมให้ผู้ล็อคอินโดยใช้ Username และ Password(ผู้เรียนกำหนดเอง)
โปรแกรมจะขึ้นหน้าต้อนรับและแสดงรายการสินค้าพร้อมราคา (ผู้เรียนกำหนดเอง)
โปรแกรมจะถามจำนวนที่ต้องการซื้อ
โปรแกรมจะทำการแสดงสรุปราคารวมของรายการสั่งซื้อทั้งหมด
"""

'''
Input Login Menu
Define username and password to login
'''

username = "admin"
password = "6969"
if username == input("Username : "):
    print("Hello", username.upper())
    if password == input("Password : "):
        print("Login Successful")
        '''Program Menu'''
        print("Loading...")
        item = { "deck" : 1500,
        "wheel" : 1000,
        "Truck" : 2500,}
        print("---Welcome to Skate Shop---")
        print("Which item do you want?")
        print("Deck  1500 THB")
        print("Wheel 1000 THB")
        print("Truck 2500 THB")
        choice = input().lower()
        if choice in item:
            amount = int(input("Amount : "))
            total = item[choice] * amount
            print("Total :", total, "THB")
        else: print("I don't know this item")
        exit()
    else: print("Wrong Password")
    exit()
else: print("Wrong Username")
exit()



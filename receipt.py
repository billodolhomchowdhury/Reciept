# print("Harshadeep KI Dukaan")
print("█   █  ███  ████   ████ █   █  ███  ████  █████ █████ ████     █   █ ███    ████  █   █ █   █  ███   ███  █   █")
print("█   █ █   █ █   █ █     █   █ █   █ █   █ █     █     █   █    █  █   █     █   █ █   █ █  █  █   █ █   █ ██  █") 
print("█████ █████ ████   ███  █████ █████ █   █ ████  ████  ████     ███    █     █   █ █   █ ███   █████ █████ █ █ █")
print("█   █ █   █ █  █      █ █   █ █   █ █   █ █     █     █        █  █   █     █   █ █   █ █  █  █   █ █   █ █  ██")
print("█   █ █   █ █   █ ████  █   █ █   █ ████  █████ █████ █        █   █ ███    ████   ███  █   █ █   █ █   █ █   █")
print("Welcome Customer!!!")
Food = {"Potato": 20, "Tomato": 30, "Banana": 50, "Mango": 100, "Marie Gold Biscuits": 40, "Milk Bikis":30}
HouseHoldGoods = {"Harpic": 200, "Lux":40, "Cetaphil": 749}
Cart = {}
stillshopping = True
while stillshopping:
    # print("Options:  ")
    print("Food -------------------------->      1")
    print("HouseHoldGoods ---------------->      2")
    print("Checkout ---------------------->      0")
    cat = int(input("Category: "))
    if cat == 0:
        name = input("Please Enter Your Name: ")
        contact = input("Enter Your Contact No: ")
        print()
        print()
        print()
        print()
        print()
        print()
        print("Harshadeep Ki Dukaan")
        print("Adress: Ambicapatty, Silchar, India")
        print("Tel. +91 9583895430")
        print()
        print("***********************************************")
        print("CASH RECIEPT")
        print("***********************************************")
        print("Product                    Quantity                  Price")
        global total 
        total = 0
        for i in Cart:
            if i in Food:
                print(i, (30-len(i))*" " ,Cart.get(i),(20-len(str(Cart.get(i))))*" ",Cart.get(i)*Food.get(i))
                total = total + Cart.get(i)*Food.get(i)
            if i in HouseHoldGoods:
                            print(i, (30-len(i))*" " ,Cart.get(i),(20-len(str(Cart.get(i))))*" ",Cart.get(i)*HouseHoldGoods.get(i))
                            total = total + Cart.get(i)*HouseHoldGoods.get(i)
        print("***********************************************")
        Tax = (total/100)*18
        total = total + (total/100)*18
        print("GST + CGST (18%): ", Tax)
        print("TOTAL --------->  ", total)
        print()
        print("**** THANK YOU !!!!****")
        break
    elif cat == 1:
        print(Food)
        print("Enter 0 to go to Categories")
        while 1>0:
            selected = input("Please enter the name of the product: ")
            if selected.isnumeric():
                if int(selected)==0:
                    break
            qty = int(input("Enter Quantity: "))
            if selected in Food:
                Cart[selected] = qty
                print(qty," ",selected," Added")
            else:
                pass
        continue
            
    elif cat == 2:
        print(HouseHoldGoods)
        print("Enter 0 to go to Categories")
        while 1>0:
            selected = input("Please enter the name of the product: ")
            if selected.isnumeric():
                if int(selected)==0:
                    break
            qty = int(input("Enter Quantity: "))
            if selected in HouseHoldGoods:
                Cart[selected] = qty
                print(qty," ",selected," Added")
            else:
                pass
        continue
    else:
        print("Invalid please try again")
        continue
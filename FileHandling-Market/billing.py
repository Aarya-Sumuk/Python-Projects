#This function calculates the final amount the customer should pay
def purchase_items(List):
    L = List  
    cust_name = input("Please enter your name: ")
    print("\nHello " + cust_name + "! Welcome to our Market.\nPlease select items as per your choice.")
    q = {}  
    flag = "Y"
    while flag.upper() == "Y":  
        product = input("\nWhat do you want to buy? ")
        product_name = product.upper() 

        if product_name == L[0][0].upper() \
                or product_name == L[1][0].upper() \
                or product_name == L[2][0].upper():  
            p = True
            while p == True:
                try:
                    p_quantity = int(input("How many " + product + " do you want to buy: "))
                    p = False
                except:  
                    print("\t\tError!!!\nPlease enter integer value!! ")
            if product_name == L[0][0].upper() and p_quantity <= int(L[0][2]):
                q[product_name] = p_quantity
            elif product_name == L[1][0].upper() and p_quantity <= int(L[1][2]):
                q[product_name] = p_quantity
            elif product_name == L[2][0].upper() and p_quantity <= int(L[2][2]):
                q[product_name] = p_quantity
            else:
                print(
                    "\nSorry!! " + cust_name + "!, " + product + " is out of stock.\nWe will add stock of " + product + " later. \nLets hope, you will get this item after next shopping.\n")

            flag = (input(cust_name + " do you want buy more items?(Y/N)"))
        else:
            print("sorry!! " + product + " is not available in our store.")
            print("\nChoose from following items please!")
            print("--------------------------------------------")
            print("ITEM\t\tPRICE/kg\t\tQUANTITY/kg")
            print("--------------------------------------------")
            for i in range(len(L)):
                print(L[i][0], "\t\t", L[i][1], "\t\t",
                      L[i][2])  
            print("--------------------------------------------")

    print("\nYou Choosed Items and it's Quantity respectively:\n", q, "\n")
    
    f_amount = 0  # final amount
    for keys in q.keys():
        if keys == L[0][0].upper():  
            t_price = int(L[0][1])
            t_num = int(q[keys])
            t_amount = (t_price * t_num)
            f_amount += (t_price * t_num)
            print("\nTotal cost for tomato: ", t_amount)
        elif keys == L[1][0].upper():  
            p_price = int(L[1][1])
            p_num = int(q[keys])
            p_amount = (p_price * p_num)
            f_amount += (p_price * p_num)
            print("Total cost for potato: ", p_amount)
        else:  
            o_price = int(L[2][1])
            o_num = int(q[keys])
            o_amount = (o_price * o_num)
            f_amount += (o_price * o_num)
            print("Total cost for onions: ", o_amount)
    print("\nYour total amount is: ", f_amount)

#Generating an invoice
    import datetime  # import system date and time for create a unique invoive name.
    uniqueid = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(
        datetime.datetime.now().day) + "-" + str(datetime.datetime.now().hour) + "-" + str(
        datetime.datetime.now().minute) + "-" + str(datetime.datetime.now().second)
    invoice = str(uniqueid)  # unique invoice

    file = open(invoice + " (" + cust_name + ").txt", "w")  
    file.write("=============================================================")
    file.write("\nMARKET\t\t\t\tINVOICE")
    file.write("\n\nInvoice: " + invoice + "")
    file.write("\nName of Customer: " + str(cust_name) + "")
    file.write("\n=============================================================")
    file.write("\nPARTICULAR\tQUANTITY\tUNIT PRICE\tTOTAL")
    file.write("\n-------------------------------------------------------------")

    for keys in q.keys():  # In this loop, write in a file only those product which is purchase by user.
        if keys == "TOMATO":
            file.write(
                str("\n" + str(keys) + " \t\t " + str(q['TOMATO']) + " \t\t " + str(L[0][1]) + " \t\t " + str(t_amount)))
        elif keys == "POTATO":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['POTATO']) + " \t\t " + str(L[1][1]) + " \t\t " + str(p_amount)))
        else:
            file.write(
                str("\n" + str(keys) + " \t\t " + str(q['ONION']) + " \t\t " + str(L[2][1]) + " \t\t " + str(o_amount)))

    file.write("\n\t\t\t Your payable amount is: " + str(f_amount))
    file.write("\n-------------------------------------------------------------")
    file.write("\n\n\tThank You " + cust_name + " for your shopping.\n\t\tSee you again!")
    file.write("\n=============================================================")
    file.close()
    return q

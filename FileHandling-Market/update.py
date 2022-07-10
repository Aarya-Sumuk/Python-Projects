#This function updates the number of items left in the market after the purchase
def overwrite(List, Dictionary):   
    L = List    
    d = Dictionary    
    
    for keys in d.keys():
        if keys == "TOMATO":
            L[0][2] = str(int(L[0][2])-d['TOMATO'])
        elif keys == "POTATO":
            L[1][2] = str(int(L[1][2])-d['POTATO'])
        else:
            L[2][2] = str(int(L[2][2])-d['ONION'])
    print("\nRemaining Stock Items:\n",L)
        
    files = open("items.txt", "w")  
    for each in L:
        files.write(str(",".join(each)))
        files.write("\n")         
    files.close()
    return

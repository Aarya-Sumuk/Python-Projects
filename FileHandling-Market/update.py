def overwrite(List, Dictionary):   # an overwrite function
    L = List    # assign list with variable name 'L'
    d = Dictionary    # assign Dictionary with variable name 'd'
    """
    Update quantity of product after customer purchased some quantity of any product.
    And print remaining stock products.
    """
    for keys in d.keys():
        if keys == "TOMATO":
            L[0][2] = str(int(L[0][2])-d['TOMATO'])
        elif keys == "POTATO":
            L[1][2] = str(int(L[1][2])-d['POTATO'])
        else:
            L[2][2] = str(int(L[2][2])-d['ONION'])
    print("\nRemaining Stock Items:\n",L)
        
    files = open("items.txt", "w")  # opens stock file (products.txt) file in write mode.
    for each in L:
        files.write(str(",".join(each)))
        files.write("\n")         
    files.close()
    return

import items
import billing
import update

again = "Y"
while again.upper() == "Y":
    a = items.read_items()
    b = billing.purchase_items(a)
    update.overwrite(a, b)
    again = input("\nNew guests arrived? ")
print("\nThank you !!")
print("\nFind your invoice by searching your name as a text file")

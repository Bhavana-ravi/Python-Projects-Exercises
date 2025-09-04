#Shopping cart exercise

item = input("Enter the item you would like to buy: ")
quantity = int(input("Enter the quantity of the item: "))
price = float(input("Enter the price of the item : "))
total = quantity * price

print(f"You are wishing to purchase {quantity} {item}/s")
print(f"Total price of the {item} is : Rs.{round(total,2)}")


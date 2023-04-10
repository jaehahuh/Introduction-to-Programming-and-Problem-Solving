first_item = float(input("Enter price of first item: "))
second_item = float(input("Enter price of second item: "))
card = input("Does customer have a club card?(Y/N): ")
tax_rate = float(input("Enter tax rate, e.g.5.5 for 5.5% tax: "))

base_price = first_item + second_item

if (first_item > second_item):
    promotion = first_item + (second_item/2)
elif (first_item < second_item):
    promotion = (first_item/2) + second_item
elif (first_item == second_item):
    promotion = (first_item/2) + second_item

if (card == "Y" or card == "y"):
    total_discount = promotion*0.9
else:
    total_discount = promotion

total_price = round(total_discount + (total_discount*tax_rate/100),2)

print("Base price =", base_price)
print("Price after discounts =", total_discount)
print("Total_price =", total_price)

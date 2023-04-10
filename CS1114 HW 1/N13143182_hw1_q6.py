print("Please enter your amount in the format of dollars and cents in two separate lines:")
dollars = int(input())
cents = int(input())

total_cents = (dollars * 100) + cents

quarters = total_cents//25
r_quarters = total_cents%25
dimes = r_quarters//10
r_dimes = r_quarters%10
nickels = r_dimes//5
r_nickels = r_dimes%5
pennies = r_nickels


print(dollars, "dollars and", cents, "cents are:")
print(quarters,"quarters,", dimes, "dimes,", nickels, "nickels and", pennies, "pennies.")

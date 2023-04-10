print("Please enter number of coins:")

quarters = int(input("# of quarters: "))
dimes = int(input("# of dimes: "))
nickels  = int(input("# of nickels: "))
pennies = int (input("# of pennies: "))

q_cents = quarters * 25
d_cents = dimes * 10
n_cents = nickels * 5
p_cents = pennies

total_cents = q_cents + d_cents + n_cents + p_cents

dollars = total_cents//100
cents = total_cents%100

print("The total is", dollars, "dollars and", cents, "cents")

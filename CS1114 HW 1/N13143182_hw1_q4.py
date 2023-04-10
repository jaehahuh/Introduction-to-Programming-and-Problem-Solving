print ("Current U.S. population is 307,357,870.")
year = int(input("Please enter the year : "))

current_population = 307357870

day = year * 365
hour = day * 24
minute = hour * 60
second = minute * 60

birth = second/7
death = second/13
immigrant = second/35


future_population = current_population + birth - death + immigrant

print("The estimated population after" ,year, "years from current year :",int(future_population))

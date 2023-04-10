john_days = int(input("Please enter the number of days John has worked: "))
john_hours = int(input("Please enter the number of hours John has worked: "))
john_minutes = int(input("Please enter the number of minutes John has worked: "))

bill_days = int(input("Please enter the number of days Bill has worked: "))
bill_hours = int(input("Please enter the number of hours Bill has worked: "))
bill_minutes = int(input("Please enter the number of minutes Bill has worked: "))

sum_john =  (john_days*24*60) + (john_hours*60) + john_minutes
sum_bill = (bill_days*24*60) + (bill_hours*60) + bill_minutes

total_time = sum_john + sum_bill

total_day = total_time//(24*60)
rest_time = total_time%(24*60)
total_hour = rest_time//(60)
total_minute = rest_time%60


print ("The total time both of them worked together is: ",  total_day, "days,", total_hour, "hours and", total_minute, "minutes.")

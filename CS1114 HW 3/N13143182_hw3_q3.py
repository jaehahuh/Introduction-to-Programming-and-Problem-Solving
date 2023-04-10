start_day = input("Enter the day the call started at: ")
start_time = int(input("Enter the time the call started at (hhmm): "))
duration_time = int(input("Enter the duration of the call (in minutes): "))

if (start_day == 'Mon' or start_day == 'Tue' or start_day == 'Wed' or start_day == 'Thr' or start_day == 'Fri'):
    if (start_time >= 800 and start_time <= 1800):
        cost = duration_time*0.4
    else:
        cost = duration_time*0.25
else:
    cost = duration_time*15
    
print("This call will cost $", cost)

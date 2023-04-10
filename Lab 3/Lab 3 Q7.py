s =  input("Please enter time in 24hr format: ")

num = int(s)

hour = num//100
minute = num%100

if(minute < 10):
    mod_minute = "0" + str(minute)
else:
    mod_minute = minute
    
if(hour == 12):
    print (hour,":",minute, "in 12 hr format is:", hour, ":", mod_minute, "pm")
elif (hour == 0):
    print (hour,":",minute, "in 12 hr format is:", hour +12, ":", mod_minute, "am")

elif (hour >= 13):
    print (hour,":",minute, "in 12 hr format is:", hour - 12, ":", mod_minute, "pm")
else:
    print (hour,":",minute, "in 12 hr format is:", hour, ":" ,mod_minute, "am")

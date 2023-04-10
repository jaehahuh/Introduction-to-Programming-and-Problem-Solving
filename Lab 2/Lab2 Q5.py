birthDate = int(input("Please enter a date of birth:"))

todayDate = int(input("Please enter a today's date: "))


byear = birthDate//10000
r_byear = birthDate%10000
bmonth = r_byear//100
bday = r_byear%100

tyear = todayDate//10000
r_tyear = todayDate%10000
tmonth = r_tyear//100
tday = r_tyear%100

print ("Date of birth is " ,bmonth,"/",bday,"/", byear)
print ("Today's date is ", tmonth,"/",tday,"/", tyear)

total_bdays = byear * 365 + bmonth * 30 + bday
total_tdays = tyear * 365 + tmonth *30 + tday

total_days = total_tdays - total_bdays

diff_year = total_days//365
r_year = total_days%365

diff_month = r_year//30
diff_day = r_year%30


print ("You have been alive for ", diff_year, "years ", diff_month, "months ", diff_day, "days")

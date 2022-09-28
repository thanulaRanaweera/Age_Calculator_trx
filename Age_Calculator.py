###########trx####################
print("********Current date******")

t_date=int(input("ENTER TODAYS DATE:"))
t_mon=int(input("ENTER TODAYS MONTH:"))
t_yr=int(input("ENTER TODAYS YEAR:"))
print(" ")
print("-----------------------------------------")
print("********Birth date******")

print(" ")
b_date=int(input("ENTER BIRTH DATE:"))
b_mon=int(input("ENTER BIRTH MONTH:"))
b_yr=int(input("ENTER BIRTH YEAR:"))
print(" ")
print("-----------------------------------------")
print(" ")
#there are few other ways to do the calculations without this array
mon=[30, 30, 30, 30, 30, 30, 30, 30, 30, 30,30, 30]
#this calculation is the core
#It can be done in a different way too.
#this is what we do, when we calculate the age manualy
if (b_date>t_date):
    t_mon=t_mon-1
    t_date=t_date+mon[b_mon-1]
if (b_mon>t_mon):
    t_yr=t_yr-1;
    t_mon=t_mon+12;
    days=abs(int((t_date-b_date)))
mon=abs(int((b_mon-t_mon)))
yr=abs(int((t_yr-b_yr)))
print("********AGE Calculator ******")
print("Years: ",yr," Months: ",mon," Days: ",days)
#bye

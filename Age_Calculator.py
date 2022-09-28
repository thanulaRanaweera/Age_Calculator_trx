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
#Hi! Nethmi Madam, Thank You.....
mon=[30, 30, 30, 30, 30, 30, 30, 30, 30, 30,30, 30]
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
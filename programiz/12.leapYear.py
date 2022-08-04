year=int(input("enter a year"))
if(year%400==0):
    print("leap year")
elif(year%100==0):
    print("not a leap year")
elif(year%4==0):
    print("leap year")
else:
    print("not a leap year")
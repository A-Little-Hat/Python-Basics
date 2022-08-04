side1=int(input("enter a side"))
side2=int(input("enter a side"))
side3=int(input("enter a side"))
s=(side1+side2+side3)/2
print("area is : ", ((s*(s-side1)*(s-side2)*(s-side3)) ** .5))
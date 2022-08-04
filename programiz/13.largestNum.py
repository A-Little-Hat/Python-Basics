a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
if(a>b and b>c):
    print(a,"is the largest number.")
elif(b>a and b>c):
    print(b,"is the largest number.")
else:
    print(c,"is the largest number.")
n=int(input("enter a number "))
backup=n
num=0
while(n>0):
    x=n%10
    n=n//10
    x=x**3
    num+=x
if(num==backup):
    print(num,"is a armstrong number")
else:
    print(backup,"is not a armstrong number")
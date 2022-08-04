s=int(input("enter start "))
e=int(input("enter a end "))
for n in range(s,e+1):
    order=len(str(n))
    num=0
    backup=n
    while(n>0):
        x=n%10
        num+=x**order
        n=n//10
    if(num==backup):
        print(num,"\t",end='')
n=int(input("enter the no of terms "))
a=0
b=1
for i in range(0,n):
    if(i==0): 
        print(0,"\t" ,end='')
    elif(i==1): 
        print(1,"\t" ,end='')
    else:
        c=a+b
        print(c,"\t" ,end='')
        a=b
        b=c
print()

start=int(input("enter starting number "))
end=int(input("enter ending number "))

for n in range(start,end+1):
    flag=0
    for i in range(2,n):
        if(n%i==0):
            flag+=1
            continue
    if(flag==0):
        print(n,"is a prime number")
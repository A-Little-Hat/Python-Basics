num=int(input("enter a number : "))
rev=0
while num!=0:
    temp=num%10
    rev=rev*10+temp
    num=int(num/10)
    print(len(str(num)))
print(rev)
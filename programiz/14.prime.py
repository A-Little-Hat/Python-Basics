n=int(input("enter a number "))
for i in range(2,n):
    if(n%i==0):
        print(n,"is not a prime number.")
        exit()
print(n,"is a prime number")

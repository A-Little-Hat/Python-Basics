def sortInWave(arr, n): 
    a.sort() 
    for i in range(0,n-1,2): 
        a[i], a[i+1] = a[i+1], a[i]
a=[]
n=int((input("enter the size : ")),10)
for i in range(0,n):
    e=int((input("enter a element : ")),10)
    a.append(e)
sortInWave(a, len(a)) 
for i in range(0,len(a)): 
    print (a[i]) 
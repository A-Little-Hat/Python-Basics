import array as arr
a=arr.array('i',[])
n=int((input("enter the size : ")),10)
for i in range(0,n):
    e=int((input("enter a element : ")),10)
    a.append(e)
print(a)
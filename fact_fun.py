f=open("a.txt","w")
list=["apple\n","dfdf\n","fggggg\n"]
f.write("apple\ndfdf\nfggggg\n")
f.close()
f=open("a.txt","r")
print(f.read())
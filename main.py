import fun_module
print("file __name__ is set to: {}" .format(__name__))

if __name__ == "__main__":
   print("main.py executed when ran directly")
else:
   print("main.py executed when imported")
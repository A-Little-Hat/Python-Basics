print("File __name__ is set to: {}" .format(__name__))

if __name__ == "__main__":
   print("Fun_module executed when ran directly")
else:
   print("Fun_module executed when imported")
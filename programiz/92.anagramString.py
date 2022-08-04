from ctypes.wintypes import PINT


str1=input("enter the first string : ")
str2=input("enter the second string : ")
if sorted(str1.lower()) == sorted(str2.lower()):
    print("\naragram String.")
else:
    print("\nnot anagram String")
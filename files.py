

# chapter 4 :file operation in python

# step:1 create the folder in desktop like python 


# create null file in python 

# location,mode name:x=empty
# f=open("C:\\Users\\ASUS\\Desktop\\pythin\C.txt","x"); 

# print("text file crated successfully")

# write in this file 
# f=open("C:\\Users\\ASUS\\Desktop\\pythin\C.txt","w"); 
# f.write("welcome to my python tutorial...")
# f.write("hello |  good morning ")
# print("text file is content included successfully")


# read file and how many character you read and enter their size 
f=open("C:\\Users\\ASUS\\Desktop\\pythin\C.txt","r"); 
# f.read()
# read=f.read(20)
read=f.read(2)
print(read)

# read lines
# show all content in one lines
read=f.readlines()
print(read)


# exception handling in pyhon 

# like we have not file of perticular name and we read that file than show the error
try:
   f=open("C:\\Users\\ASUS\\Desktop\\pythin\rni.txt","r"); 
   print(f.readlines())
except:
   print("file not available...plz create first")   

#    if file read than closed the file than show close...
else:
   f.close()   
   print("file closed successfully")


# correct file name:than show closed successfully
try:
   f=open("C:\\Users\\ASUS\\Desktop\\pythin\rni.txt","r"); 
   print(f.readlines())
except:
   print("file not available...plz create first")   

#    if file read than closed the file than show close...
else:
   f.close()   
   print("file closed successfully")


# copy file 
try:
   with open("C:\\Users\\ASUS\\Desktop\\pythin\C.txt") as f2:
    with open("C:\\Users\\ASUS\\Desktop\\pythin\B.txt","w") as f3:
     for i in f2:
      f3.write(i)
except:
   print("file not available...plz create first")   

#    if file read than closed the file than show close...
else:
   f2.close()   
   print("file closed successfully")   


# delete file

import os
if os.path.exists("C:\\Users\\ASUS\\Desktop\\pythin\D.txt"):
   os.remove("C:\\Users\\ASUS\\Desktop\\pythin\A.txt")
else:
   print("file not available..")

print("file delete successfully")   
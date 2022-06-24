# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 09:15:13 2022

@author: Lenovo
"""

def my_function(p, l):
    "Function untuk mengitung luas"
    print(p * l)
my_function(2,4)


# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return;

# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")

# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print("Values outside the function: ", mylist)

# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4]; # This would assig new reference in mylist
   print("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print("Values outside the function: ", mylist)

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return;

# Now you can call printme function
printme(str = "Hacktiv8")
printme(str = "123")

# Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print("Name: ", name)
   print("Age: ", age)
   return;

# Now you can call printinfo function
printinfo( age=4, name="a" )

# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 10:06:49 2022

@author: SulisSandiwarno
"""

# Function definition is here
def printinfo( name, nilai1,nilai2,nilai3,nilai4, nakhir):
   "This prints a passed info into this function"
   
   nakhir = (nilai1*0.1)+(nilai2*0.2)+(nilai3*0.3)+(nilai4*0.4)
   
   print("Name: ", name)
   print("nilai 1: ", nilai1)
   print("nilai 2: ", nilai2)
   print("nilai 3: ", nilai3)
   print("nilai 4: ", nilai4)
   print("nilai akhir: ", nakhir)

   return;

# Now you can call printinfo function
printinfo( name='a', nilai1=100, nilai2=80, nilai3=75, nilai4=88, nakhir=0)

# Function definition is here
def printinfo( name, age = 26 ):
   "This prints a passed info into this function"
   print("Name: ", name)
   print("Age: ", age)
   return;

# Now you can call printinfo function
printinfo( age=50, name="hacktiv8" )
printinfo( name="hacktiv" )


# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print("Output is: ")
   print(arg1)
   for var in vartuple:
      print(var)
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50, "a" )

# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print("Output is: ")
   print(arg1)
   for var in vartuple:
      print(var)
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50, "a" )


# Function definition is here
sum = lambda arg1, arg2, arg3, arg4, arg5 : arg1 + arg2 + arg3 + arg4 + arg5

#def sum(arg1, arg2):
    #arg1 + arg2
    
# Now you can call sum as a function
#print("nilai absen : ", sum( 10, 20 ))
#print("nilai tugas : ", sum( 20, 20 ))
#print("nilai uts: ", sum( 20, 20 ))
#print("nilai uas: ", sum( 20, 20 ))

print("nilai akhir : ", sum( 10, 20, 30, 40, 0 ))

jumlahKucing = 20

def jumlahHewan():
    jumlahAnjing = 30
    return jumlahKucing + jumlahAnjing

def jumlahKelinci():
    return jumlahKucing + jumlahKucing

jumlahHewan()
jumlahKelinci()
print(jumlahHewan(), jumlahKelinci())


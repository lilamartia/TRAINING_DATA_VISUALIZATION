# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 12:52:59 2022

@author: Lenovo
"""

x = 0
y = 5

if x < y:                            # Truthy
    print('yes')

if y < x:                            # Falsy
    print('yes')

if x:                                # Falsy
    print('yes')

if y:                                # Truthy
    print('yes')

if 'aul' in 'grault':                # Truthy
    print('yes')

if 'quux' in ['foo', 'bar', 'baz']:  # Falsy
    print('yes')
    
if 'foo' in ['bar', 'baz', 'qux']:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')
    
print('After conditional')

if 'foo' in ['foo', 'bar', 'baz']:        #  x
    print('Outer condition is true')      #  x

    if 10 > 20:                           #  x
        print('Inner condition 1')        #        x

    print('Between inner conditions')     #  x

    if 10 < 20:                           #  x
        print('Inner condition 2')        #  x

    print('End of outer condition')       #  x
print('After outer condition')            #  x

x = 20

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')
    
x = 120

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')
    
hargaBuku = 20000
hargaMajalah = 5000
uang = 2000

if uang > hargaBuku:
    print("beli buku")
else:
    print("uang tidak cukup")

x = 2

if x == 1: print('foo'); print('bar'); print('baz')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')

buku = 2000
jumlahbeli = 3
totalbelanja = 6000
uang = 10000

if uang > totalbelanja:
    print("beli buku dapat mangkuk")
elif uang < totalbelanja:
    print("tidak beli buku")
else:
    print("tidak jadi beli buku")
    
nilai_absen = int(input("masukkan nilai absen :"))
nilai_absen = nilai_absen * 0.1

nilai_tugas = int(input("masukkan nilai tugas :"))
nilai_tugas = nilai_tugas * 0.2

nilai_uts = int(input("masukkan nilai uts :"))
nilai_uts = nilai_uts * 0.3

nilai_uas = int(input("masukkan nilai uas :"))
nilai_uas = nilai_uas * 0.4

nilai_total = nilai_absen+nilai_tugas+nilai_uts+nilai_uas
print(nilai_total)

if nilai_total >= 80:
    print("A")
elif nilai_total < 80 and nilai_total >= 70:
    print("B")
elif nilai_total < 70 and nilai_total >= 60:
    print("C")
elif nilai_total < 60 and nilai_total >= 50:
    print("D")
else:
    print("E")
        
n = 5
while n > 0:
    n -= 1
    print(n)

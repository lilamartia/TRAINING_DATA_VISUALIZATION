# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 13:00:41 2022

@author: Lenovo
"""
import numpy as np
a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
a = np.array([1, 2, 3])

print(np.zeros(6))

print(np.arange(4))
print(np.arange(0,10,2)) # (start, stop, step)

print(np.arange(2,29,5))
print(np.arange(3,10,5))

import numpy as np
#array untuk append
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
np.append(arr, [1,2])

print (np.append(arr, [1,2]))

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
np.append(arr, [1,2])
print(np.append(arr, [1,2]))

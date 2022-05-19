# -*- coding: utf-8 -*-
"""
Created on Thu May 19 16:57:25 2022

@author: PRIYA
"""

"""
    *
   **
  ***  
"""    

m=4
for i in  range (1,m):
    for j in range(m,1,-i):
        print(' ',end='')
    for k in range(1,i+1):
        print('*',end='')
    print()
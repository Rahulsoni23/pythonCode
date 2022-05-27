# -*- coding: utf-8 -*-
"""
Created on Fri May 27 17:16:01 2022

@author: PRIYA
"""

"""

*
**
***
****
*****
****
***
**
*
"""

for i in range(1,6):
    for j in range(1,i):
        print("*",end='')
    print() 
    
for i in range(6,0,-1):
    for j in range(1,i):
        print('*',end='')
    print()
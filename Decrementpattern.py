# -*- coding: utf-8 -*-
"""
Created on Thu May 19 16:57:25 2022

@author: RAHUL
"""
"""
 ***
  **
   *
"""

#decpattern
n=4
for i in range(1,4):
    for j in range(1,i):
        print(' ',end='')
    for k in range(n,i,-1):
        print('*',end='')
    print()
    

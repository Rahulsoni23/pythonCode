# -*- coding: utf-8 -*-
"""
Created on Thu May 26 15:20:33 2022

@author: PRIYA
"""

# trianglepattern 
"""
   *
  * *
 * * *
"""  
num=5  
for a in range(1,num):
    for b in range(num,a,-1):
        print(' ',end='')
    for c in range(1,a+1):
        print(' * ',end='')
    print()    

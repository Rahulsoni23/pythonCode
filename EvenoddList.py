# -*- coding: utf-8 -*-
"""
Created on Fri May 20 11:19:17 2022

@author: RAHUL
"""

list=[1,2,3,4,5,6,7,8,9,10]
new_list1=[]
new_list=[]
for i in list:
    if(i%2==0):
        new_list1.append(i)
    elif(i%2==1):
            new_list.append(i)
print("It is even  number :",new_list1)
print("It is odd   number :",new_list)

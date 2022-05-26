# -*- coding: utf-8 -*-
"""
Created on Thu May 26 11:52:31 2022

@author: PRIYA
"""

" CALCULATOR "
num1=int(input("enter a number1 :"))
num2=int(input("enter a number2 :"))
print("enter number to performe a operation:")
cond=input(" '1' Addition: '2' Substraction: '3' Division: '4' Multiplication: '5' Modulus: ")

if cond=="1":
 def add(num1,num2):
    c=num1+num2
    print("addition of number :",c) 
    add(num1,num2)
elif cond=="2":
  def sub(num1,num2):
    d=num1-num2
    print("Substraction of number :",d)
  sub(num1,num2)
elif cond=="3":
   def divi( num1,num2):
      e=num1/num2
      print("Division :",e)
   divi(num1, num2)
elif cond=="4":
    def multi(num1,num2):
        f=num1*num2
        print("Multiplication :",f)
    multi(num1,num2)
elif cond=="5":
    def mod (num1,num2):
        s=num1%num2
        print("Modulus :",s)
    mod(num1, num2)
else:
    print("enter a correct value for your operation")

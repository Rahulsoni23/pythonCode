# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 20:40:27 2022

@author: PRIYA
"""

try:
     num1=int(input("enter a number1 :"))
except:
    print("valid integer number1:")
    num1=int(input("enter a number1 :"))
 
try:
    if num1<1:
      raise Exception("sorry...do not enter zero number ")
except Exception:
    print("enter a valid number:")
    num1=int(input("enter a number :"))
  
try :
    if num1>1000:
        raise MemoryError("Sorry...do not enter above 1000")
except MemoryError :
        print("enter a valid number:")
        num1=int(input("enter a number :"))
                      
     
try:
   num2=int(input("enter a number2 :"))
except:
    print("valid integer number2:")
    num2=int(input("enter a number2 :"))
    
    
try:
    if num2<1:
      raise Exception("sorry...do not enter zero number ")
except Exception:
    print("enter a valid number:")
    num2=int(input("enter a number :"))
        
try :
    if num2>1000:
        raise MemoryError("Sorry...do not enter above 1000")
except MemoryError :
        print("enter a valid number:")
        num1=int(input("enter a number :"))
        
        

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

            
        
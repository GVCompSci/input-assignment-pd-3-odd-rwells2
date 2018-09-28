'''
Created on Sep 26, 2018

@author: rwells22
'''
print("Welcome to FakeAmazon!")  

name = input("What is your name? ")  

phoneNumber = input("Please enter your telephone number: ")  

productName = input("What is the product that you want? ")  

price = float(input("How much does it cost? "))  

quantity = int(input("How many are you buying? "))  

subtotal = float(price*quantity) 

tax = float(subtotal*0.06) 

total = float(subtotal+tax) 

print() 

#Now show purchase data

print("Purchase Information:")  

print("Name: " ,name)  

print("Phone number: " ,phoneNumber)  

print("Product: " ,productName) 

print("Quantity: " ,quantity) 

print("Price: " ,price)  

print("Subtotal = " ,subtotal) 

print("Tax = " ,tax) 

print("Total = " ,total)
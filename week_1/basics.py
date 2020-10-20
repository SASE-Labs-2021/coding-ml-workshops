#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 17:54:25 2020

@author: kevinmenglin
"""

##Variables
#exactly like math variables
toy='Buzz Lightyear'
price=29.99
budget=90
inBudget=price<=budget #this is a boolean


##Input, Printing, Types, and Operators
#try writing a script where you prompt yourself to type something in and then print it out
print('Hello World') #this is a function...notice the f(x) like structure...has input and output
input() #input asks you to type something in, doesn't need an 'x' term
amount=input() #you can save what you typed into a variable as a string
amount=input("How many toys do you want?") #include a prompt
type(amount) #notice that amount is a string

amount=int(amount) #change amount to an integer

price*amount
total_price=amount*price
inBudget=price*amount<=budget #basic operator example

print("Total Price Is "+str(total_price)+" for "+str(amount)+" toys")


##Conditionals; walk through, read it as if its english, then try and predict what will happen
#this allows you to run the indented code only when certain conditions are grou
if amount>0 or False:
    print("I want some toys")
elif amount==4 and inBudget:
    print('I want four toys')
elif amount>4 :
    print("That's a lot of toys")
elif not amount<0:
    print("You can't have negative toys dummy")
else:
    print("I want less than four toys")
    
#Arrays    
receipt=[toy,price,amount,total_price] #here we make our own array
print(receipt)
print(len(receipt))

#Loops
#go through and write out how follow what's happening at each step
thing=[1,8.4,'g',['3',22,"Hi"]]
thingThree=[] #make an empty list which we will fill using the for loop

#for each entry in a supplied list, run the indented code blocks
for entry in thing:
    print(entry)
    thingThree.append(entry*3)
    print(thingThree)
    
print('a'+thingThree)

#string is a list, and you can index it like a list
'hello'[3] #4th letter
'hello'[0:4] #first 3 letters

dna='' #build a DNA strand using a while loop 
#can you figure out a way to do this with for loops?
length=int(input("How long is your strand?"))

#while a statement is true, it will run the code blocks
while(len(dna)<length):
    print(len(dna))
    print(len(dna)<length)
    dna+=input("Enter Base Letter:")
print("Your DNA strand "+dna)


##Functions: run this and then try to figure out what the function is doing under the hood
#the function is waiting for you to tell it what value is assigned to strand
#kind of like input
#useful for wrapping several lines of re-usable code into a simple piece of code
def basePairing(strand):
    opposite=''
    for i in range(len(strand)):
        base=strand[i]
        if base=='A':
            opposite+='T'
        elif base == 'T':
            opposite+='A'
        elif base == 'G':
            opposite+='C'
        else:
            opposite+='G'
    return(opposite)


paired=basePairing(dna)










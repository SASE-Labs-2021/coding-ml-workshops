#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 17:54:25 2020

@author: kevinmenglin
"""

##Variables
toy='Buzz Lightyear'
price=29.99
budget=90
inBudget=price<=budget


##Input, Printing, Types, and Operators
input() #input asks you to type something in
amount=input() #you can save what you typed into a variable as a string
amount=input("How many toys do you want?") #include a prompt
type(amount) #notice that amount is a string

amount=int(amount) #change amount to an integer

price*amount
inBudget=price*amount<=budget #basic operator example

print(int(inBudget))

total_price=amount*price
print("Total Price Is "+str(total_price)+" for "+str(amount)+" toys")


##Conditionals; predict what will happen for your value of inBudget
if amount>0:
    print("I want some toys")
if amount==4 and price==29.99:  
    print("I want four toys")
elif amount>4:
    print("That's a lot of toys")
elif not amount>0 or budget<=0:
    print("You can't have negative toys dummy")
else:
    print("I want less than four toys")
    
#Arrays    
receipt=[toy,price,amount,total_price] #here we make our own array
print(receipt)
print(len(receipt))

#Loops
thing=[1,8.4,'g',['3',22,"Hi"]]
thingThree=[]
for entry in thing:
    print(entry)
    thingThree.append(entry*3)
    print(thingThree)
print(thingThree)

dna=''
length=int(input("How long is your strand?"))

while(len(dna)<length):
    print(len(dna))
    print(len(dna)<length)
    dna+=input("Enter Base Letter:")
print("Your DNA strand "+dna)


##Functions: run this and then try to figure out what the function is doing under the hood
#the function is waiting for you to tell it what value is assigned to strand
#kind of like input
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










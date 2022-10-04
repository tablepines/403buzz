#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 18:29:31 2022

@author: vivianlaibui
"""
#Conditional exercises

response = input('Enter your response here: ')
if response == "1" or response == "2":
    print("OK")
    if response == "1":
        print("Correct!")
    if response == "2":
        print("Incorrect!")
elif response == "":
    print("Subject did not respond")
else:
    print("Subject pressed the wrong key")
    
#For loop exercises
#Question 1 and 2
my_name = 'Vivian'
n = 1
for letters in my_name:
    print (letters, n)
    n += 1

#Question 3 and 4
names = ['Amy', 'Rory', 'River']
for name in names:
    print(name)
    counter = 0
    for letter in name:
        counter += 1
        print(letter, counter)

#While loop exercises 
#Question 1
img_counter = 0
while img_counter < 20:
    if img_counter <10:
        print("%i, image1.png" %img_counter)
    elif img_counter < 20:
        print("%i, image2.png" %img_counter)
    img_counter = img_counter + 1
    
#Question 2
import random
response2 = " "
looping = True
failsafe = 0
while looping:
    response2 = random.randint(0,10)
    print(response2)
    print("This is an image")
    failsafe = failsafe + 1
    if response2 == 1 or response2 == 2 or failsafe == 5:
        looping = False 

        


    

        

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 09:00:36 2022

@author: vivianlaibui
"""
#Variable Operations Exercises
#Question 1
sub_code = "sub"
subnr_int = 2
subnr_str = "2"

#Question 2
print(sub_code + subnr_str)
print((sub_code + " ")+ subnr_str)
print(sub_code + (subnr_str * 3))
print((sub_code + subnr_str) * 3)
print((sub_code * 3) + (subnr_str * 3))

#List Operations Exercises
#Question 1
numlist = [1,2,3]
print(numlist * 2)

#Question 2
import numpy as np
numarr = np.array(numlist) 
print(numarr)
print(numarr * 2)

#Question 3
strlist = ["do", "re", "mi", "fa"]
#['dodo','rere','mimi','fafa']
print(strlist[0]*2, strlist[1]*2, strlist[2]*2, strlist[3]*2)

#['do','re','mi','fa','do','re','mi','fa']
print(strlist * 2)

#['do','do','re','re','mi','mi','fa','fa']
print([strlist[0], strlist[0], 
       strlist[1], strlist[1],
       strlist[2], strlist[2],
       strlist[3], strlist[3]])

#[['do','do'],['re','re'],['mi','mi'],['fa','fa']]
print([ [strlist[0], strlist[0]], 
        [strlist[1], strlist[1]],
        [strlist[2], strlist[2]],
        [strlist[3], strlist[3]]])

#Zipping Exercises
import numpy as np

first_item = []
second_item = []
imgs_F = ['face1.png'] * 5 +['face2.png'] * 5 +['face3.png'] * 5 + ['face4.png'] * 5 + ['face5.png'] * 5
imgs_H = ['house1.png'] *5 + ['house2.png'] *5 + ['house3.png'] * 5 + ['house4.png'] * 5 + ['house5.png'] * 5

first_item.extend(imgs_F)
first_item.extend(imgs_H)
first_item.extend(imgs_F)
first_item.extend(imgs_H)
print(first_item)
print(len(first_item))

imgs_FS = ['face1.png','face2.png', 'face3.png', 'face4.png', 'face5.png'] * 5
imgs_HS = ['house1.png','house2.png','house3.png','house4.png','house5.png'] * 5

second_item.extend(imgs_HS)
second_item.extend(imgs_FS)
second_item.extend(imgs_HS)
second_item.extend(imgs_FS)
print(second_item)
print(len(second_item))

cues = ['cue1'] * 50 + ['cue2'] * 50
catimgs = list(zip(first_item, second_item, cues))
print(catimgs)

#To randomize:
np.random.shuffle(catimgs)
print(catimgs)

#Indexing Exercises
#Question 1
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

#Question 2
print(colors[4])

#Question 3
print(colors[4][2])
print(colors[4][3])

#Question 4
del colors[5]
colors.append('indigo')
colors.append('violet')
print(colors)

#Slicing Exercises
#Question 1
list100 = list(range(0,101))
print(list100)

#Question 2
print(list100[:10])

#Question 3
print(list100[99:0:-2])

#Question 4
print(list100[100:96:-1])

#Question 5
print(list100[40:44])
print(list100[40])
print(list100[39:44] == [39, 40, 41, 42, 43])


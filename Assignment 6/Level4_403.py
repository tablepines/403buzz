#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 09:45:47 2022

@author: vivianlaibui
"""

from psychopy import gui
from psychopy import core
from psychipy import visual, monitors, event
from datetime import datetime
import os
import numpy as np

#Dialogue Box Exercises 
#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, handedness
#get date and time

exp_info = {'subject_nr':0, 'age':0, 'handedness':('right','left','ambi'), 
            'gender':'', 'session':1}
print(exp_info)
print('All variables have been created! Now ready to show the dialogue box!')

my_dlg = gui.DlgFromDict(dictionary=exp_info,
                         title ='subject info',
                         fixed=['session'],
                         order=['session', 'subject_nr', 'age','gender', 'handedness' ])


date=datetime.now()
exp_info['date']= str(date.hour) + '-' + str(date.day) + '-' + str(date.month) + '-' + str(date.year) + '-'                
print(exp_info['date'])

#-create a unique filename for the data
filenme = str(exp_info['subject_nr']) + '_' + exp_info['date'] +'.csv'


main_dir = os.getcwd()
sub_dir = os.path.join(main_dir, 'sub_info', filename)


#Monitor and window exercises
#=====================
#CREATION OF WINDOW AND STIMULI / question 3
#=====================
#-define the monitor settings using psychopy functions
#-define the window (size, color, units, fullscreen mode) using psychopy functions

mon = monitors.Monitor('myMonitor', width=30.41, distance=60 )
mon.setSizePix([1440,900])
mon.save()
thisSize = mon.getSizePix()
thisWidth = thisSize[0]
thisHeight = thisSize[1]
print(thisSize)

#For this exercise and the Stimulus exercise question 2
win = visual.Window(monitor=mon, fullscr=True, color=[-1, -1, -1])


#Stimulus exercises questions 1-3
fix_text = visual.TextStim(win, text= '+')
my_image = visual.ImageStim(win, size=400,400)
nTrials = 4
image_dir = os.path.join(main_dir, 'images')

horizMult = [-1, 1, 1, -1]
vertMult = [1, 1, -1, -1]
correctResponse = [True, True, True, True]
for trials in range(nTrials):
    my_image.image = os.path.join(image, dir, stims[trials])
    
    my_image.pos = (horizMult[trial] * thisWidth/4, vertMult[trial] * thisHeight/4)    my_image.pos = (thisWidth/4, thisHeight/4)
    my_image.draw()
    fix_text.draw() #fixation cross, question 3
    win.flip()
    key = event.waitKeys()
    
    print(key) #print on screen, wait for keyboard press
    if key[0]== 'left'
        if horizMult[trial] == -1:
            CorrectResponse[trial] = True
        else:
            CorrectResponse[trial] = False
    if key[0] == 'right'
        if horizMult[trial] == 1:
            CorrectResponse[trial] = True
        else 
            CorrectResponse[trial] = False 

win.close()
    

#Stimulus exercises question 4: filling in psuedocode
#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define experiment start text unsing psychopy functions
#-define block (start)/end text using psychopy functions
#-define stimuli using psychopy functions (images, fixation cross)

start_Text = visual.TextStim(win, text=start_msg)
block_text = visual.TextStim(win, text=block_msg)
endtr_text = visual.TextStim(win, text=endtr_msg)
#=====================
#START EXPERIMENT
#=====================
#-present start message text
#-allow participant to begin experiment with button press
start_msg ='Welcome to my experiment!'
event.waitKeys() #wait for keypress

block_msg = 'Press any key to continue to the next block.'
endtr_msg = 'End of trial'
 
stims = ['face01.jpg', 'face02.jpg', 'face03.jpg']

nBlocks = 2
nTrials = 3
my_image = visual.ImageStim(win, size=400,400)
fix_text = visual.TextStim(win, text= '+')
my_text = visual.TextStim
#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks
    #-present block start message
    #-randomize order of trials here
    
    for block in range(nBlocks):
        my_text.text = block_msg
        my_text.draw()
        win.flip()
        event.waitKeys()
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials
        #-set stimuli and stimulus properties for the current trial
        

        #=====================
        #START TRIAL
        #=====================  
        #-draw fixation
        #-flip window
        #-wait time (stimulus duration)
        
        #-draw image
        #-flip window
        #-wait time (stimulus duration)
        
        #-draw end trial text
        #-flip window
        #-wait time (stimulus duration)
        
        for trial in range(nTrials):
            
            fix_text.draw() #fixation cross, question 3
            win.flip()
            event.waitKeys()
            
            my_image.draw()
            win.flip()
            event.waitKeys()
            
            my_text.text = endtr_msg + str(trial)
            my_text.draw()
            win.flip()
            event.waitKeys()
            
        np.random.shuffle(trials) #shuffle order of stimulus 


    win.close()
                
#======================
# END OF EXPERIMENT
#======================        
#-close window
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 22:24:15 2022

@author: vivianlaibui
"""
from psychopy import visual, monitors, event, core

# Wait Exercises
        #=====================
        #START TRIAL
        #===================== 
        #-draw fixation
        #-flip window
        #-wait time (stimulus duration)
        fix_text.draw() #draw
        win.flip() #show  
        core.wait(.5) 

        
        #-draw image
        #-flip window
        #-wait time (stimulus duration)
        my_image.draw()
        win.flip()
        core.wait(.5)
        
        #-draw end trial text
        #-flip window
        #-wait time (stimulus duration)
        my_text.draw()
        win.flip()
        core.wait(.5)
        
# Clock exercises 
wait_timer = core.Clock() # meta timer for my stimuli


#Question 4
#=====================
#START EXPERIMENT
#=====================
#-present start message text
#-allow participant to begin experiment with button press
blockTimer = core.Clock()
trialTimer = core.Clock()
stimTimer = core.Clock()
respTimer = core.Clock()

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks
for block in range(nBlocks):
    blockTimer.reset()
    blockStart = blockTimer.getTime()
    #-present block start message
    #-randomize order of trials here
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    
    for trial in range(nTrials):
        trialTimer.reset()
        trialStart = trialTimer.getTime()
    #-for loop for nTrials
        #-set stimuli and stimulus properties for the current trial
        
        #=====================
        #START TRIAL
        #===================== 
        stimTimer.reset()
        while stimTimer <= 1
        #-draw fixation
        #-flip window
        
        stimTimer.reset()
        resp.Timer.reset()
        while stimTimer <= .5        
        #-draw image
        #-flip window
        
        while stimTimer <= 1:
            
        event.waitKeys() #wait for keypress
        RTresp.Timer.getTime()
        
        #-collect subject responde for that trial
        #-collect subject response time for that trial
        #-collect subject accuracy for that trial
        
        trialEnd = trialTimer.getTime() 
        
    blockEnd =  blockTimer.getTime()


#======================
# END OF EXPERIMENT
#======================        
#-close window

# Frame-based timing exercises
#Questions 1 and 2 

#define the monitor parameters
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1600,900])
win = visual.Window(monitor=mon) #define a window

#set durations
fix_dur = 0.2
image_dur = 0.1
text_dur = 0.2

refresh = 1.0/60.0

#set frame counts
fix_frames

import os
#stuff you only have to define once at the top of your script
main_dir = os.getcwd() 
image_dir = os.path.join(main_dir,'images')

fix_text = visual.TextStim(win, text= '+')
my_image = visual.ImageStim(win)

stims = ['face01.jpg','face02.jpg','face03.jpg'] #create a list if images to show
nTrials=3 #create a number of trials for your images
#stimTimer = core.Clock()
fixTime = .5
stimTime = 1.0

refresh = 1.0/60.0

fixFrames = 2
stimFrames = 1
totalFrames = stimFrames + fixFrames

wait_timer = core.Clock() # meta timer for my stimuli

# Question 2
press_timer = core.CountdownTimer()


#for trial in range(nTrials): #loop through trials
    
#    my_image.image = os.path.join(image_dir,stims[trial])
    
#    press_timer.reset()
#    press.timer.addTime(3)
    
#    while press_timer.getTime() > 0:
#        my_image.draw() #draw
#       win.flip() #show
#        core.wait(.5) #wait .5 seconds, then:
    
    
win.close() #close the window after trials have looped 

#Question 3

for trial in range(nTrials): #loop through trials
    
    my_image.image = os.path.join(image_dir,stims[trial])
    
    for nFrames in range(totalIntervals):
        if 0 <= nFrames <= fixFrames:
            fix_text.draw()
            win.flip()
    
        
        if fixFrames < nFrames <= fixFrames + stimFrames:
            if nFrames == fixFrames + 1:
                imgStartTime = wait_timer.getTime()
            my_image.draw()
            win.flip() #show
        
    #core.wait(.5) #wait .5 seconds, then:
        
    fix_text.draw() #draw
   # imgEndTime = wait_timer.getTime()
   
       if fixFrames + stimFrames < nFrames < totalFrames:
           if nFrames == stimFrames + 1:
               imgEndTime = waitTimer.getTime()
           fix_text.draw
           win.flip() # show
           
    #core.wait(.5) #wait .5 seconds, then:
    
    print('Image Duration was {} seconds'. format(imgEndTime - imgStartTime))
    
    
win.close() #close the window after trials have looped 
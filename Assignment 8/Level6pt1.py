from psychopy import event, visual, monitors, core 

mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(800,800), color=[-1,-1,-1])

nTrials=10
my_text = visual.TextStim(win)
fix = visual.TextStim(win, text='+')

rt_clock = core.Clock() #create a response time clock
cd_timer = core.CountdownTimer() #add countdown timer

for trial in range(nTrials):
    rt_clock.reset() #reset timing for every trial
    cd_timer.add(2) #add 2 seconds
    
    event.clearEvents(eventType='keyboard') #reset keys for every trial 
    count =-1 #reset counter for every while loop 
    while cd_timer.getTime() > 0: #after 2 seconds
        
        my_text.text = 'trial %i' % trial
        my_text.draw()
        wait.flip()
        
        keys = event.getKeys(keyList=['1', '2', 'escape']) # collect keypress after first
        
        if keys:
            count = count + 1
            if 'escape' in keys:
                win.close()
            if count == 0:
                resp_time = rt.clock.getTime() #use getTime to determine response time
                print(keys, resp_time) #print keys and response times 

    my_text.text = "Please make a keypress for trial " + str(trial)
    
    fix.draw()
    win.flip()
    core.wait(2)
    
    event.clearEvents() #clear events HERE
    
    my_text.draw()
    win.flip()
    core.wait(1)
    
    print('keys that were pressed', keys) #which keys were pressed?
    
    keys = event.waitKeys(maxWait=2), keyList=['1','2','3']) #waits for 2 seconds then continues 
    if keys:
        sub_resp = keys[0] #only take first response 
        print('response that was counted', sub_resp)
    
    remaining_time=2-resp_time
    my_text.draw()
    win.flip()
    core.wait(remaining_time)
    
win.close() 
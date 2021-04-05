
size (600,600)
background (100)
stroke (0)
noFill()
textAlign (CENTER, CENTER)

# STRETCH: Could you toad this data from an external file?
steps = [12045,11245,7645,10468,9804,13021,10213,6440,12643,8001,14163,10133,8966,9096,6695,18652,9505,11415,9353,9297,11642,9693,10463,13914,4956,4981,5910,8664,7213,9240,4844]
theMean = sum(steps) / len(steps)
shapeAdj = 130 # this is the
DEBUG = True

if DEBUG:
    print("---------------------")
    print("Number of days: %s" %(len(steps)))
    print("Average number of steps/ day (the mean): %s" %(theMean))
    print("Max steps in a day: %s" %(max(steps)))
    print("Min number of steps in a day: %s" %(min(steps)))
    print("---------------------")
    
i = 0
# STRETCH: could you enumerate () to generate i ?
for y in range (0, height, height/5):
    for x in range (0, width, width/6):
        # draw a box around each day
        noFill()
        #STRETCH: could you change the fill color in the box containing the max steps?
        stroke(0)
        rect(x,y,height/6,height/5)
        
        #draw a circle in there that indicates try makign a circle with diameter steps/100
        stroke(255)
        circle(x+width/12, y+height/10, steps [i]/shapeAdj)
        
        # the number of steps taken each day
        if DEBUG == True:
            msg = steps [i]
        else: 
            msg = 'march '+str(i+1)+'\n'+str(steps[i])
        text(msg, x+ width/12, y+ height/10)
        
        #increment the i index
        i +=1 #this is the same as i = i+1

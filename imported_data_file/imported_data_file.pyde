# Let's see my activities!
# import the python CSV module 
import csv
def setup():
    size(800,400)
    background(100)
    f = open("activities2.csv", "r")
    reader = csv.reader(f)
    # I am an ITERATOR!
    #for l in reader:
        #print (l)
    i = 0
    walking = []
    for row in reader:
        # print(i)
        if i == 1:
            for j,col in enumerate(row):
                if j > 0:
                    walking.append(col)
        i = i+1
    #print(walking)
    
    k= 0 
    margin = 50
    #yOffset = height/max(walking)
    pointGap = (width - (margin*2)) / len(walking)
    translate (0, height/2)
    line(0,0,width,0)
    for d in walking:
        stroke(255, 23, 0)
        fill (255, 23, 0)
        #stroke(23, 225, 0)
        #fill (23, 225, 0)
        xpt= margin+ (k*pointGap)
        ypt = float(d)* -40
        circle(xpt,ypt,10)
        k = k+1
    
    k= 0
    #for e in cycle:
        #stroke(255, 23, 0)
        #fill (255, 23, 0)
        #xpt= margin+ (k*pointGap)
        #ypt = float(e)* -40
        #circle(xpt,ypt,10)
        #k = k+1
    
    #pointGap = (width -2*margin) / len(walking)
    #print(pointGap)
    #stroke(23, 225, 0)
    #fill (23, 225, 0)
    #j=0
    #translate (0, height/2)  
    #for d in walking:
        #xpt= margin+j*pointGap
        #ypt = d*40
        #circle(xpt,ypt,10)
        #j = j+1

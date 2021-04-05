
size(1440,280)
background(0,0,200)
# STRETCH could you load an image in the background?
# bg = loadImage("daytonight.jpg")
# background(bg)
DEBUG = True
# there are 1440 minutes in a day

# The time that the FitBit recorded me  going to sleep 
# in March, 2019
tobed     = ["0:48","2:17","1:32","0:31","0:13","0:03","0:40","1:04","1:34","1:26","1:08","0:34","0:04","1:55","0:40","0:44","0:17","0:09","0:20","0:57","2:08","0:31","0:08","0:19","1:04","0:38","2:14","1:06"]
# minutes asleep
asleep    = [355,276,364,355,366,410,401,330,341,339,339,334,426,291,371,407,371,385,376,472,263,277,389,344,313,357,349,351]
# awake     = [22,24,32,39,34,56,42,30,37,41,31,51,54,34,70,61,29,23,84,31,22,32,53,46,31,31,30,33]
theMean = (sum(asleep) / len(asleep)) / 60.0

if DEBUG:
    # print(len(awake))
    print("----------------------")
    print("Number of days: %s" %(len(tobed)))
    print("Average hours of sleep/day(the mean): %s" %(theMean))
    print("Max minutes of sleep in a day: %s" %(max(asleep)))
    print("Min minutes of sleep of steps in a day: %s" %(min(asleep)))
    print("----------------------")
    
barHeight = height/len(tobed)

# Draw horizontal rectangels from the left side of the sketch 
# indicating the time to bed and length of sleep

y = 0
i = 0

while y < height:
    bedTime = str(tobed[i])
    hrs,mins = bedTime.split(":") # "1:15" hrs = 1, mins = 15 
    x = int(hrs)*60 + int(mins)
    fill(100)
    stroke(111)
    rect(x,y, x+int(asleep[i]), barHeight)
    
    y = y+barHeight 
    i = i + 1
    
# a title
fill(255)
textSize(24)
text("How much sleep in March?", 3* (width/4), 200)

fill(255)
textSize(12)

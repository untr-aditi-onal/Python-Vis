size(600,210)
background(100)

howTall = [63,62,64,63,62,60.5,63,63,63,63,69,50,58,59,68,66,67,65,51,72]
numKids = len(howTall)
theMean = sum(howTall) / numKids
maxHeight = max(howTall)
minHeight = min(howTall)
colWidth = width/numKids
yMultiplier = 1

print("----------------------")
print("Number of kids: %s" %(numKids))
print("Average height (the mean): %s" %(theMean))
print("Tallest (max): %s" %(maxHeight))
print("Shortest (min): %s" %(minHeight))
print("----------------------")
print("column width: %s" %(colWidth))
print("yMultiplier: %s" %(yMultiplier))

# Move the coordinate system to the bottom
translate(0,height-20)
# fill(255,255,0)
# rect(0,0, width, -20)
x = 0
i = 0

while x < width:
    y = (2*howTall[i]) * -1
    fill(255)                # white
    rect(x,0, colWidth, y)
    fill(0)                  # black
    #textSize(12)             # normal reading size
    text(howTall[i], x+5,-10)
    
    x = x+colWidth
    i = i+1
    
fill(255)
textSize(24)
text("How tall are the 5th graders? TALL!", 20, -170)

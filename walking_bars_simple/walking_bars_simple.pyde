import csv

def setup():
    size(1000, 400)
    background(128);
    f = open("walking.csv", "r")
    noStroke()
    
    # Drawing rectangles!
    rectMode(CORNERS)
    
    getData(csvFile="walking.csv")
    
    # grab data from the CSV file & put it in a list
    with f:
        reader = csv.reader(f)
        # Nette suggested this elegant method for parsing the CSV
        # Thanks, Nette!
        
        # Put the rows in a Dictionary
        rows = {}
        for row in reader:
            fix = [float(dst) for dst in row[1:]] #slice
            # Use the row labels for the keys!
            rows[row[0]] = fix
            #activities[row[0]] = fix
            #activities [row[0]] is {"walking":[1.1,2.2,3.3,...]}
        # header = rows['activity']
        walking = rows['walking']
        # cycling = rows['cycling']
        

    # set up the GUI variables
    margin = 80
    pointGap = (width-(2*margin))/5
    barW = pointGap/4
    vAdjust = 60
    pointGap = (width-2*margin)/(len(walking)-1.0)

    # Zero the Y coordinate system near the bottom and draw a line
    translate(0,height-20)
    stroke(100,200,222)
    line(0,0,width,0)

    # Loop over the list of activities and draw some bars!
    j=0
    fill(100,200,0)
    for d in walking:
        fill(100,200,0)
        # bottomLeft = margin+(j*pointGap)-pointGap,0
        # topRight = margin+(j*pointGap),-d*vAdjust
        rect(margin+(j*pointGap)-barW/2,0, 
            margin+(j*pointGap),-float(d)*vAdjust)
        fill(255)
        textSize(16)
        textAlign(CENTER,CENTER)
        text(j+1, margin+(j*pointGap)-pointGap/2, 10)
        j = j+1
        
        
# Stub for a new fuction to access the CSV data
def getData(csvFile):
    # 1/ Open the CSV file
    # 2/ parse the rows
    # 3/ return a dictionary with keys matching each row's name. 
    # Example:
    return { 'walking':[1.0, 1.3, 3.2],'cycling':[9.1, 2.9, 5.4] }
    return activities
    print("open me: %s" %csvFile)

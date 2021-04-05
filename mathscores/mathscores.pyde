import csv

def setup():
    global years, scores, margin, graphHeight, positions, title
    size(1000, 200)
    background(20)
    fill(255)
    title = "Average math scores for 3rd graders by year."
    years = []
    scores = []
    margin = 40
    positions = []
    graphHeight = (height - margin) - margin
    positions = processData(filename="math_scores.csv")
    drawData(positions, vertices=True,edges=False,grooves=True)
    drawCurves(vList=positions)
    
def processData(filename):
    global overallMin, overallMax, xSpacer
    f = open(filename, "r")
    with f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i > 0:
                years.append(int(row[1]))
                scores.append(int(row[2]))
    overallMin = min(scores) # What does Cairo say?
    overallMax = max(scores)
    xSpacer = (width - margin - margin) / (len(years) - 1)
    for i in range(0, len(scores)):
        adjScore = map(scores[i], overallMin, overallMax, 0, graphHeight)
        yPos = height - margin - adjScore
        xPos = margin + (xSpacer * i)
        positions.append(PVector(xPos, yPos))
    return positions

def drawData(positions, vertices=False,edges=False,grooves=False):
    for i in range(0, len(positions)):
        textSize(12)
        textAlign(CENTER,CENTER)
        text(years[i], positions[i].x, height - margin + 20)
        if grooves:
            # draw grooves
            stroke(200, 100)
            strokeWeight(1)
            line(positions[i].x, margin, positions[i].x, height - margin)
        if vertices:
            # Draw the vertices
            stroke(200, 100)
            circle(positions[i].x, positions[i].y, 7)
        if edges:
            # Draw the edges
            if(i > 0):
                # stroke(200)
                strokeWeight(2)
                line(positions[i].x, positions[i].y,
                    positions[i - 1].x, positions[i - 1].y)
    textSize(14)
    textAlign(LEFT,CENTER)
    text(overallMax, 5, margin)
    text(overallMin, 5, height - margin)
    textAlign(RIGHT,BOTTOM)
    text(title, width-margin,margin/2)
    
def drawCurves(vList):
    # Draw curved lines
    stroke(23, 225, 0)
    strokeWeight(3)
    noFill()
    beginShape()
    # start point
    curveVertex(vList[0].x,vList[0].y)
    for i in range(0,len(vList)):
        curveVertex(vList[i].x,vList[i].y)
    # end point
    curveVertex(vList[-1].x,vList[-1].y)
    endShape()

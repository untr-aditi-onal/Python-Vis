import csv
def setup():
    global lineWeight, palette, margin, pointGap
    mnth, walk, run, cycle = processData(filename="Activities.csv")
    size(800, 300)
    lineWeight = 5
    mnth = "January"
    margin = 50
    palette = [color(23, 0, 255), 
               color(239, 31, 193), 
               color(0, 216, 224)
               ]
def draw():
    background(255)
    strokeWeight(lineWeight)
    noFill()
    textAlign(CENTER)
    translate(0, height / 4)
    # Walk Line
    drawBezier(walk, palette[0])
    fill(palette[0])
    text("walk", width / 2 - 50, height / 2 + margin)
    # Run Line
    drawBezier(run, palette[1])
    fill(palette[1])
    text("run", width / 2, height / 2 + margin)
    # Cycle Line
    drawBezier(cycle, palette[2])
    fill(palette[2])
    text("cycle", width / 2 + 50, height / 2 + margin)
    noLoop()

def drawBezier(vals, c):
    global pointGap
    pointGap = 70 #mouseY / 2 #(width-(2*margin)) / len(vals[0]-1 
    feedBack(pointGap,"pointGap")
    print(vals)
    
    beginShape()
    noStroke()
    fill(c)
    ctens = 43 # mouseY / 2
    textSize(14)
    text(vals[0], margin, height / 2 - float(vals[0]) - 10)
    textAlign(CENTER)
    vertex(margin, height / 2 - float(vals[0]))
    for i in range(1, len(vals),1):
        posX = i * pointGap + margin
        posY = height / 2 - float(vals[i])
        c1 = (i - 1) * pointGap + margin + ctens
        c2 = height / 2 - float(vals[i - 1])
        c3 = posX - ctens
        c4 = posY
        text(int(round(float(vals[i]))), posX, posY - 10)
        bezierVertex(c1, c2, c3, c4, posX, posY)
        # viz invisible control points
        #circle(c1, c2,10)
        #stroke(255,255,0)
        #line(c1, c2, posX, posY)
        #circle(c3, c4,10)
        #stroke(255,0,255)
        #line(c3, c4, posX, posY)
    noFill()
    stroke(c)
    endShape()

def processData(filename):
    global mnth, walk, run, cycle
    mnth = []
    walk = []
    run = []
    cycle = []
    f = open(filename, "r")
    with f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            if i > 0:
                # print(row["Month"])
                mnth.append(row["Month"])
                walk.append(row["Walk"])
                run.append(row["Run"])
                cycle.append(row["Cycle"])
    return mnth, walk, run, cycle

def feedBack(astring="Hi",aTitle="New"):
    textSize(64)
    text(aTitle+" "+str(astring), width / 2, 0)

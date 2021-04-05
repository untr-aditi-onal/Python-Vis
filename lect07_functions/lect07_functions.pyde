def setup():
    global a
    a = 0
    size(600,600)
    #img = loadImage("Point.png")
    background(255)
    fill(0)
    textAlign(CENTER, CENTER)
    textSize(32)
    fill(100)
    translate(width/2, height/2)
    text("Hi, this is the setup function.", 0,0)

def draw():
    rotateText()
    pulseText()
    colorText()

def pulseText():
    global a
    textSize(64+a)

def colorText():
    fill(random(0,255),random(0,255),0)
    #manipulate fill color     
    
def rotateText():  
    global a
    if a < 360:
        background(255)  
        a = a+random(-2,2)
        translate(width/2, height/2)
        # textSize(64)
        rotate(radians(a))
        text("You're Cancelled", 0,0)

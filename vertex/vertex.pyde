#Livecoding Shiffman's video on custom shapes in Processing
# Polygon can be defined by vertices
# quad() let's you specify four points, 
# but we want a lot more.
# beginShape()
# vertex(x,y)
# vertex(x,y)
# endShape()
def setup():
    size (400,400)
    background(0)
    stroke(255)
    noFill()
def draw():
    background(0)
    strokeWeight(8)
    point(mouseX,mouseY)
    point(150,50)
    point(250,50)
    point(300,200)
    beginShape()
    strokeWeight(2)
    # spacing = map(mouseX, 0, width, 5, 100)
    # for a in range(0,360, int(spacing)):
    #     x = 100*sin(radians(a))+200
    #     y = 100*cos(radians(a))+200
    #     vertex(x,y)
    # order matters!
    # Catmull-Rom splines!
    # Ed Catmull works at Pixar!
    curveVertex(mouseX,mouseY)
    curveVertex(100,200)
    curveVertex(150,50)
    curveVertex(mouseX,mouseY)
    curveVertex(250,50)
    curveVertex(300,200)
    curveVertex(300,200)
    endShape()

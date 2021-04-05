size (600, 600)
background (113, 50, 150)

# Dynamically converts a font to the format used by Processing from a .ttf or .otf file 
# inside the sketch's "data" folder or a font that's installed elsewhere on the computer.

fontList = PFont.list()
for fnt in fontList:
    print(fnt)

fill(255)
myFont= createFont('Canterbury-Regular-48.vlw', 88)
textFont(myFont)
textAlign(CENTER, CENTER)
text ("Hello", 100, 370)

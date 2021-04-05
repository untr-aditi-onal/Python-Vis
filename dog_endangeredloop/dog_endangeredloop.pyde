# Generalizing the Endangered Species poster

# Load a SQUARE image of an endangered animal
# that has been resized so that the number of pixels 
# is equal to the number of surviving animals.
# 1,849 = 43x43 (approximately)

# load that image
img = loadImage("dog_38x38.png")

# set the size to a factor of the images width & height
size(760,760)

# chnk is equal to the width of the sketch 
# divided by the width of the image
chnk = width/img.width

# Loop over the rows
for y in range(0,height,chnk):
    # loop over the columns
    for x in range(0,width,chnk):
        # get the color of the pixel at (x,y) in the tiny image
        c = img.get(x/chnk,y/chnk)
        # set fill and stroke
        fill(c)
        stroke(c)
        # draw the rectangle
        rect(x,y, chnk,chnk)
        
# Can you annotate the image?
textSize(64)
fill(255)
text("1,409 African Wild Dog", chnk, height-chnk)
  
save("blocks.png")

# load that image
img = loadImage("floyd_44x44.png")

# set the size to a factor of the images width & height
size(760,760)

# chnk is equal to the width of the sketch f
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
textSize(40)
fill(255)
text("8 minutes and 46 seconds", chnk, height-chnk)
  
save("blocks.png")

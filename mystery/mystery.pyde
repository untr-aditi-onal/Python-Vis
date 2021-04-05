size(500,500)
background (0,0,0)
noStroke ()

img = loadImage("mystery_50x50.jpg")
c = get ()
chnk = (width / img.width)  

for y in range (0, height, chnk):
    for x in range (0, width, chnk):
        c = img.get (x/chnk, y/chnk)
        fill (c)
        circle (x+chnk/2, y+chnk/2, chnk)
        # square (x+chnk/2, y+chnk/2, chnk/2)
        # triangle (x, y, x+chnk/2, y+chnk*2, x+chnk, y)

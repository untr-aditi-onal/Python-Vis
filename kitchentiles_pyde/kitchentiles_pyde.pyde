# 3/ Prof. Goodwin is tiling the wall behind the kitchen stove.
# This wall is 96" x 60", and the tiles are 12" x 12" square.
# Add 20% extra tiles for breakage, he likes a stacked-bond look (like below),
# and you don't need to worry about the grout.

# This is Processing stuff
size(600, 960)   # set the size of the display window
background(120)  # the color of the display window
stroke(255)     # set stroke color, e.g the grout color
fill(38, 38, 75)  # a nice denim blue coded in an RGB triplet

# Begin Python code!
# Note on scale: we are using ten pixels to the inch
tileWidthIn = 120
tileHeightIn = 120



# Printing message to the console area below
print("-row 1-------------------------")

# first row # # # # # # # # # # # # # # # # # # # # # #
x = 0
y = 0
i = 1
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)

i = i + 1
x = x + tileWidthIn
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)


x = x + tileWidthIn
i = i + 1
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)


x = x + tileWidthIn
i = i + 1
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)


x = x + tileWidthIn
i = i + 1
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)


print("-row 2-------------------------")

# second row # # # # # # # # # # # # # # # # # # # # # #
x = 0
y = y + 120
i = i + 1
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)

# YOUR CODE HERE
# Finish the wall!

x = x + tileWidthIn
i = i + 1
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)

x = x + tileWidthIn
i = i + 1
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)

x = x + tileWidthIn
i = i + 1
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)

x = x + tileWidthIn
i = i + 1
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)


print("-row 3-------------------------")

x = 0
y = y + 120
i = i + 1
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)

x = x + tileWidthIn
i = i + 1
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)

x = x + tileWidthIn
i = i + 1
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)

x = x + tileWidthIn
i = i + 1
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)

x = x + tileWidthIn
i = i + 1
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)

print("-row 4-------------------------")

print("-row 5-------------------------")
x = 0
y = y + 120
i = i + 2
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)

x = x + tileWidthIn
i = i + 1
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)

x = x + tileWidthIn
i = i + 1
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)

x = x + tileWidthIn
i = i + 1
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)

x = x + tileWidthIn
i = i + 1
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)


print("-row 6-------------------------")
x = 0
y = y + 120
i = i + 4
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)

x = x + tileWidthIn
i = i + 1
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)

x = x + tileWidthIn
i = i + 1
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)

x = x + tileWidthIn
i = i + 1
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)

x = x + tileWidthIn
i = i + 1
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)

print("-row 7-------------------------")
x = 0
y = y + 120
i = i + 5
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)

x = x + tileWidthIn
i = i + 1
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)

x = x + tileWidthIn
i = i + 1
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)

x = x + tileWidthIn
i = i + 1
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)

x = x + tileWidthIn
i = i + 1
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)

print("-row 8-------------------------")
x = 0
y = y + 120
i = i + 2
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)

x = x + tileWidthIn
i = i + 1
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)

x = x + tileWidthIn
i = i + 1
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)

x = x + tileWidthIn
i = i + 1
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)

x = x + tileWidthIn
i = i + 1
print(i, x, y, tileWidthIn, tileHeightIn)
rect(x, y, tileWidthIn, tileHeightIn)

print("\nThe wall is %sx%s inches. Tiles are %sx%s inches." % (60, 96, 12, 12))
print("Prof. Goodwin needs %s tiles to finish the wall." % (i))
extra = int(i * 0.2)
total = i + extra
print("Adding 20 percent extra (%s) makes %s tiles total.\n" % (extra, total))
print("There are 6 tiles in a box, tell him to buy %s boxes." % (total / 6))

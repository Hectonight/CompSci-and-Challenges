# Write more code in all 4 methods below.
# You do NOT need a mouseReleased() function for this problem.

def setup():
    global p1X, p1Y, p2X, p2Y
    p1X = 0
    p1Y = 0
    p2X = 0
    p2Y = 0
    size(400, 400)    
    fill(127)

def draw():
    global p1X, p1Y, p2X, p2Y
    background(255)
    
    
    rect(p1X, p1Y, p2X - p1X, p2Y - p1Y)

def mousePressed():
    global p1X, p1Y, p2X, p2Y
    p1X = mouseX
    p1Y = mouseY
    p2X = mouseX
    p2Y = mouseY

def mouseDragged():
    global p2X, p2Y
    p2X = mouseX
    p2Y = mouseY

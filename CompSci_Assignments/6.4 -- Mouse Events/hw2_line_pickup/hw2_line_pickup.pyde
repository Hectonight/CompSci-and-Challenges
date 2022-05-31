# Setup is done.
def setup():
    size(400, 400)
    global aMoving, bMoving, xa, ya, xb, yb, radius
    
    aMoving = False
    bMoving = False
    
    xa = width/3
    ya = height/2
    
    xb = 2 * width/3
    yb = height/2
    
    radius = 10
    stroke(0)
    fill(255)

# Draw is done
def draw():
    background(255)
    global aMoving, bMoving, xa, ya, xb, yb, radius
    
    line(xa, ya, xb, yb)
    circle(xa, ya, radius*2)
    circle(xb, yb, radius*2)
    

# Complete the mouse event handlers.
def mousePressed():
    global aMoving, bMoving, xa, ya, xb, yb, radius
    
    if dist(xa, ya, mouseX, mouseY) <= radius:
        aMoving = True
        xa = mouseX
        ya = mouseY
    
    if dist(xb, yb, mouseX, mouseY) <= radius:
        bMoving = True
        xb = mouseX
        yb = mouseY
        
        
    
def mouseDragged():
    global aMoving, bMoving, xa, ya, xb, yb, radius
    
    if aMoving:
        xa = mouseX
        ya = mouseY
    
    if bMoving:
        xb = mouseX
        yb = mouseY
    
    
def mouseReleased():
    global aMoving, bMoving, xa, ya, xb, yb, radius
    
    aMoving = False
    bMoving = False
    
    

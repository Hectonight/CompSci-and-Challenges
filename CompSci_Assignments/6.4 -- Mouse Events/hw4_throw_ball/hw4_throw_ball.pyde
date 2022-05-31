def setup():
    size(800, 700)
    global x, y               # Actual location of the ball.
    global startX, startY     # The starting location of the ball, before it is dragged.
    global pickup             # Boolean: True/False. Whether the ball is being dragged now.
    global falling            # Boolean: True/False. Whether the ball is falling now.
    global speedx, speedy     # Velocity of the ball in the x and y directions.
    
    x = 100
    y = 500
    
    startX = 100
    startY = 500
    
    pickup = False
    falling = False
    
    speedx = 0
    speedy = 0
    
    fill(255, 170, 0)         # Orange for a basketball.

def draw():
    global x, y, startX, startY, pickup, falling, speedx, speedy
    background(255)
    
    
    gravity = 0.2             # Nice value found by trial and error. You can change this.

    # More code here
    
    if falling:
        speedy += gravity
    
    x += speedx
    y += speedy


    if y >= 700 or y <= 0 or x <= 0 or x>= 800:
        falling = False
        x = startX
        y = startY
        speedx = 0
        speedy = 0



    circle(x, y, 50)



# Write code for each of the event handlers.

def mousePressed():
    global x, y, startX, startY, pickup, falling, speedx, speedy
    
    if dist(startX, startY, mouseX, mouseY) <= 50:
        pickup = True
    
    
def mouseDragged():
    global x, y, startX, startY, pickup, falling, speedx, speedy
    
    if pickup:
        x = mouseX
        y = mouseY
    

def mouseReleased():
    global x, y, startX, startY, pickup, falling, speedx, speedy
    if pickup:
        falling = True
    pickup = False
    
    speedx = (startX - x) * 0.1
    speedy = (startY - y) * 0.1  

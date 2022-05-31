def setup():
    global rectLen, distance
    
    rectLen = 400
    
    size(800, 400)
    fill(0, 200, 200)

def draw():
    global rectLen
    
    background(255)
    
    rect(0, 0, rectLen, 400)

def mouseDragged():
    global rectLen, distance
    if (distance >= 0):
        rectLen = mouseX + distance


def mousePressed():
    global distance, rectLen
    distance = rectLen - mouseX
    
    

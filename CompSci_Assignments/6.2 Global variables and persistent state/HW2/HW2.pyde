speed = 5

def setup():
    global RGBval
    RGBval = 0
    noStroke()
    size(600, 400)

def draw():
    global RGBval
    
    if keyPressed and key == CODED:
        if keyCode == RIGHT:
            RGBval += speed if RGBval + speed <= 255 else 0
        if keyCode == LEFT:
            RGBval -= speed if RGBval - speed >= 0 else 0
    
    fill(RGBval)
    rect(0, 0, 300, 400)

    fill(RGBval, 0, 255-RGBval)
    rect(300, 0, 300, 400)

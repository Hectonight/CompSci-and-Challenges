def setup():
    global mars, ingenuity, x, y, speedX, speedY, coded_set
    coded_set = set()

    mars = loadImage("mars.png")
    ingenuity = loadImage("ingenuity.png") 
    size(600, 400)
    x = 250
    y = 250
    speedX = 0
    speedY = 0

    
def draw():
    global mars, ingenuity, x, y, speedX, speedY, coded_set
    
    image(mars, 0, 0, 600, 400)
    
    
    if y >= 250 and speedY > 0:
        speedY = 0
        y = 250
    
    print(y)
    
    if UP in coded_set:
        speedY -= 0.1
    if y <= 250:
            speedY += 0.05
    else:
        speedY = 0    
    
    y += speedY

    
    if y >= 250:
        speedX = 0
    else:
        if RIGHT in coded_set:
            speedX += 0.1
        if LEFT in coded_set:
            speedX -= 0.1
    
    posAfterMove = x + speedX
    
    
    if posAfterMove >= 600:
        x = -70
    elif posAfterMove <= -100:
        x = 570
    else:
        x = posAfterMove

    image(ingenuity, x, y, 100, 100)


def keyPressed():
    global coded_set
    coded_set.add(keyCode)
    

def keyReleased():
    global coded_set
    coded_set.remove(keyCode)
    

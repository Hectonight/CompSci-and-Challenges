def setup():
    global x, y, xstore, ystore, diameter, letGo
    x = 300
    y = 300
    xstore = x
    ystore = y
    diameter = 50
    letGo = False
    size(600, 600)
    
def draw():
    global x, y, xstore, ystore, diameter, letGo
    background(0)
    fill(0, 0, 255)
    
    if keyPressed:
        
        if key == CODED:
            if keyCode == LEFT:
                x -= 5 if x != 0 else 0
        
            if keyCode == RIGHT:
                x += 5 if x != 600 else 0
            
            if keyCode == UP:
                y -= 5 if y != 0 else 0
            
            if keyCode == DOWN:
                y += 5 if y != 600 else 0
                
        elif key == "h":
            x = 300
            y = 300
        elif key == "p":
            diameter += 5 if diameter != 200 else 0
        elif key == "l":
            diameter -= 5 if diameter != 10 else 0
    
    
    circle(mouseX if mousePressed else x, mouseY if mousePressed else y, diameter)


    

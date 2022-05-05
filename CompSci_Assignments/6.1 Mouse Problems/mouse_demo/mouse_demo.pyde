def setup():
    size(400, 400)
    noFill()
    stroke(255)
    strokeWeight(3)

def draw():
    background(0)
    
    if mousePressed:
        strokeWeight(10)
    else:
        strokeWeight(3)
    
    ellipse(mouseX, mouseY, 100, 100)
    
    strokeWeight(1)
    line(0, 0, mouseX, mouseY)

def setup():
    size(600, 400)
    noFill()
    stroke(255)
    strokeWeight(3)


def draw():
    background(0)
    vertX = 600 if mousePressed else 0
    vertY = 0 if mousePressed else 400
    line(vertX, vertY, mouseX, mouseY)
    line(vertX, vertY, mouseX/2, mouseY/2)
    line(mouseX, mouseY, mouseX/2, mouseY/2)

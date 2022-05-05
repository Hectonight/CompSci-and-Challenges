def setup():
    size(400, 400)
    noFill()
    stroke(255)
    strokeWeight(3)


def draw():
    background(255)
    fill(255 if mousePressed else 0, 0, 0 if mousePressed else 255)
    ellipse(200, 200, mouseX, mouseY)

from math import pi
def setup():
    size(1000,1000, P3D)
    frameRate(50)

def draw():
    background(0)
    translate(width/2, height/2, 0)
    rotateX(float(mouseX)/ width*2*PI)
    rotateY(float(frameCount)/200)
    noFill()
    stroke(255)
    sphereDetail(10)
    sphere(300)
    
    translate(0, 0, 0)
    box(500)
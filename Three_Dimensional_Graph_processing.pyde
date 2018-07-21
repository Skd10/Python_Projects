def setup():
    size(1000, 1000, P3D)
    fill(250)

def draw():
    lights() #adds shadow to dimensions
    background(0) # 0 is black, 250 is white
    text("Processing's 3-D Axis",50, -50, 50)
    camera(mouseX, 50, 200.0,
           0.0, 0.0, 0.0,
           0.0,1.0, 0.0)
        
    stroke(255) #opacity (how visible)
    strokeWeight(5) #thickness of the lines
    
    text("+X", 100, 0, 0)
    stroke(0, 255, 0)#green, X Axes
    line(-100,0,0,100,0,0)
    
    text("+Y", 0,100,0)
    stroke(255, 0, 255)#pink Y Axes
    line(0,-100,0,0,100,0)
    
    text("+Z", 0,0,100)
    stroke(0, 255, 255)#blue Z Axes
    line(0,0,-100,0,0,100)
    
    fill(255,255,255)
    strokeWeight(20)
    point(0,0,0)
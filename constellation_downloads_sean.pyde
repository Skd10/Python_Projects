from math import pi
#0,0 is in the upper right hand corner? 
def setup():
    size(1000,1000, P3D)

def draw():
    strokeWeight(1)
    background(0)
    translate(width/2,height/2,0)
    #rotateX(float(mouseX)/ 200)
    #rotateY(float(frameCount)/200)
    noFill()
    stroke(255)
    sphereDetail(25,25)
    sphere(300)
    box(500)
    
    #cardinalDirections
    textSize(50)
    fill(240, 245, 245)
    text("N", -50,-400,50)
    text("S",-25, 400, 50)
    text("W",-350, -50,50)
    text("E",300, -50, 50)
    textSize(100)

    
    strokeWeight(3) 
    textSize(20)
    fill(26, 140, 255)
    
    #---------Canis Minor----------------
    ellipse(200, -300, 10, 10) #(x,y,how wide, how tall)
    ellipse(250, -250, 20, 20)
    line(250, -250, 200, -300) 
    text("Canis Minor", 210, -300)
    #-------------------------------------
    
    #---------Cassiopeia----------------
    ellipse(-30,-170, 5, 5)
    ellipse(-5,-190, 5, 5)
    line(-30,-170,-5,-190)
    line(-5,-190,-10,-170) 
    #-------------------------------------
    
    #---------Cygnus---------------------
    ellipse(-90,-20,5,5) #D
    line(-90,-20,-120,0)
    ellipse(-120,0,5,5) #A
    text("Cygnus", -150,-20)
    ellipse(-170,-10,5,5)#C
    line(-170,-10,-70,10)
    ellipse(-70,10,5,5)#B
    line(-120,0,-140,50)
    ellipse(-140,50,5,5)#E
    #-------------------------------------   
    
    #---------Cepheus----------------------------------
    text("Cepheus", 0,-70,20) #x,y,z
    triangle(-25,-50, -50,-110,5,-100) #C,B,A  25, -100
    quad(-50,-110, -25,-50, -60,-45, -95,-100) #B,C,D,E
    #--------------------------------------------------
    
    #-------------------Ursa Minor------------------
    ellipse(20,-50,10,10) #A
    line(20,-50,10,-5)
    ellipse(15,-30,5,5) #B
    ellipse(10,-5,5,5) #C
    quad(10,-5,25,10,15,25,-10,15)
    #----------------------------------------
    
    #---------Corvus---------------------
    triangle(185,75,150,100,225,100) #corvusTOP
    triangle(185,150,150,100,225,100)
    text("Corvus", 185,150,50)
    #-------------------------------------
    
    #---------Libra--------------------- 
    text("Libra", 0,210,50)
    quad(-50,250,-15,225,25,250,0,265)
    line(0,265,20,290)
    text(".", 10, 290)
    #-------------------------------------
    
    #--------------Bootes----------------
    text("Bootes", 20,75,30)
    quad(-15,75,-5,50,20,75,30,150)
    #-------------------------------------
    
    #--------------Leo----------------
    text("Leo", 220,-50,-50)
    ellipse(200, -50,10,10)
    ellipse(170, 20,5,5)
    line(200,-50,170,20)
    ellipse(160, -20,5,5)
    ellipse(185, -20,5,5)
    line(160,-20,170,20)
    line(160,-20,185,-20)
    line(200,-50, 180,-50)
    line(180,-50,170,-40)
    line(170,-40,160,-45)
    line(160,-45,150,-90)
    line(170,-95,150,-90)
    #-------------------------------------
    
    #---------Scorpio--------------------- 
    ellipse(-100, 300,10,10)
    ellipse(-60, 290, 5, 5)
    line(-100,300,-60,290)
    ellipse(-50, 287, 10, 10)
    line(-60, 290, -45, 287)
    ellipse(-35, 290, 5, 5)
    line(-45, 287, -35, 290)
    ellipse(-15, 287, 5, 5)
    line(-35, 290, -15, 287)
    ellipse(-17, 300, 5, 5)
    line(-15, 287, -17, 300)
    ellipse(-20, 275, 5, 5)
    line(-15, 287, -20, 275)
    ellipse(-107, 315, 5, 5)
    line(-100, 300, -107, 315)
    ellipse(-115, 325, 5, 5)
    line(-107, 315, -115, 325)
    #-------------------------------------
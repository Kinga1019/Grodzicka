def setup():
    size(600, 600)
    background(0)
    myFont = createFont("Georgia",200)
    textFont(myFont)
    
def draw():
    clear()
    
    fill(0,0,255,255)
    text("G", width/2, height/2+50)
    if keyPressed:
        if key == 'g':
            fill(0,255,0,255)
            text("G", width/2, height/2+50)
            
    fill(0,0,255,255)
    text("K", width/2-120, height/2-20)
    if keyPressed:
        if key == 'k':
            fill(0,255,0,255) 
            text("K", width/2-120, height/2-20) 
        
            
    if keyPressed:
        if key == CODED:
            if keyCode == RIGHT:
                fill(255,0,0,255)
                text("G", width/2, height/2+50)
            
            elif keyCode == LEFT:
                fill(255,0,0,255)
                text("K", width/2-120, height/2-20)

    p = createShape()
    p.beginShape()
    p.fill(0,0,110,180)
    p.stroke(0,255,0,200)
    p.vertex(100, height/2)
    p.vertex(300, 500)
    p.vertex(500, height/2)
    p.vertex(530, 420)
    p.vertex(70, 420)
    p.endShape(CLOSE)
    shape(p, 25, 25)
    
    if mouseButton:
        if mouseX < 320 and mouseX > 200 and mouseY < 280 and mouseY > 130:
            fill(0,255,0,255) 
            text("K", width/2-120, height/2-20)
        
        
    
def mouseMoved():
    
    if mouseX < 320 and mouseX > 200 and mouseY < 280 and mouseY > 130:
        fill(0,255,0,255) 
        text("K", width/2-120, height/2-20)
        
        
    
            
            
    

            
 

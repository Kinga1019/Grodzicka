def setup():
    c=color(172, 225, 175)
    fill(c)
    size(800,800)
    rectMode(CORNERS)

def draw():
    point(50, 50)
    line(mouseX, mouseY, 20, 30)
    rect(mouseX, mouseY, width, height)
    print(mouseX, mouseY, mousePressed)
    
    if mousePressed:
        clear()
        
    else:
        print(mouseX, mouseY)
        rect(20, 50, 10, 50)
        
    
    
        
    
    

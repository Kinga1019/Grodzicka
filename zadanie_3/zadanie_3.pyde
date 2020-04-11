def setup():
    size(600, 600)
    background(0)
    myFont = createFont("Georgia",200)
    textFont(myFont)
    global defaultKolor, zaznaczeniaKolor, czyG
    defaultKolor = (0,0,255,255)
    zaznaczeniaKolor = (0,255,0,255)
    czyG=False
    
def draw():
    clear()
    global czyG
    fill(*defaultKolor)
    text("G", width/2, height/2+50)
    text("K", width/2-120, height/2-20)
    if keyPressed:
        if key == 'g':
            fill(*zaznaczeniaKolor)
            text("G", width/2, height/2+50)
            czyG = True
        
        if key == CODED and keyCode == LEFT and czyG:
                fill(*zaznaczeniaKolor)
                text("K", width/2-120, height/2-20)
                fill(*defaultKolor)
                text("G", width/2, height/2+50)
    else:
        czyG=False

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
    
    #if mouseButton:
    if mouseX < 320 and mouseX > 200 and mouseY < 280 and mouseY > 130:
        fill(*zaznaczeniaKolor) 
        text("K", width/2-120, height/2-20)
        if keyPressed and keyCode == RIGHT:
            text("G", width/2, height/2+50)
            fill(*defaultKolor)
            text("K", width/2-120, height/2-20)
        
'''    
def mouseMoved():
    
    if mouseX < 320 and mouseX > 200 and mouseY < 280 and mouseY > 130:
        fill(0,255,0,255) 
        text("K", width/2-120, height/2-20)
        '''
# trochę za podobne do rozwiązania Niny... jeśli się to powtórzy, będę musiała podjąć jakieś środki zapobiegawcze...
# strzałki działały też gdy żadna litera nie byłą zaznaczona
# przeanalizuj jak działa po moich popawkach
# 1,5pkt

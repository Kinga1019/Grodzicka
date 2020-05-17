import random
add_library('pdf')

def setup():
    global zdjecie, okulary, wasy, wasyx, okularyx # można też jednolinijkowo
    size(700, 700) # to nie jest proporcja zdjęcia dokumentowego
    textSize(20)
    okularyx = False
    wasyx = False
    zdjecie = loadImage("zdjecie.jpg")
    okulary = loadImage("okulary.png")
    wasy = loadImage("wasy.png")
    
    print(random.random())
    print(type(zdjecie))
    print(type(okulary))
    print(type(wasy))
    fill(20,255,200)
    
def draw():
    global okularyx
    global wasyx
    global zdjecie
    global okulary
    global wasy
    image(zdjecie, 0, 0, height, width)

    if okularyx or wasyx:
        beginRecord(PDF, "outzdjecie.pdf") # dzięki temu, że znajduje się dopiero tutaj, nie powinny się zapisać elementy mini UI
        image(zdjecie, 0, 0, height, width)
        if okularyx: # skrótowy zapis w domyśle ma  '== True'
                image(okulary, 180, 210, height/2, width/2-150)    
        if wasyx:
            image(wasy, 233, 365, height/2-100, width/2-220)
    else:
        image(okulary, 10, 0, height/8, width/12)
        image(wasy, 600, 0, height/8, width/12)
        fill(0,0,0)
        text("ZAPISZ", 120, 30)
    
    
def mouseClicked():
    global okularyx
    global wasyx
    if mouseX < 100 and mouseX > 0 and mouseY < 50 and mouseY > 0:
        if okularyx == False: 
            okularyx = True
        elif okularyx == True:
            okularyx = False
    elif mouseX < 700 and mouseX > 600 and mouseY < 45 and mouseY > 0:
        if wasyx == False:
            wasyx = True
        elif wasyx == True:
            wasyx = False
    
def mousePressed():
    if mouseX < 200 and mouseX > 120 and mouseY < 50 and mouseY > 10:
        endRecord()
        exit()

# plus do aktywności za ładne mini UI
# 1,5 pkt

            
    
        
    
    

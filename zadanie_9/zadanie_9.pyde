import random

def setup():
    global jez, ramkaC, ramkaN
    size(800, 800)
    textSize(40)
    jez = loadImage("jez.jpg")
    ramkaC = loadImage("ramkaCzerwona.png")
    ramkaN = loadImage("ramkaNiebieska.png")
    print(random.random())
    print(type(jez))
    print(type(ramkaC))
    print(type(ramkaN))
    fill(20,255,200)
    
def draw():
    global jez, ramkaC, ramkaN
    
    try:
        image(jez, 0, 0, height, width)
    except:
        text ("Niestety nie znaleziono obrazka :(", 70, 380)
        print "Niestety nie znaleziono obrazka :( "
        image(ramkaC, 0, 0, height, width)
    else:
        image(ramkaN, 0, 0, height, width)
        text ("Zabieram Cie na wycieczke!", 150, 150)
        print "Zabieram Cie na wycieczke!"
        
def mousePressed():
    exit()

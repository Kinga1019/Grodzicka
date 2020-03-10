def setup():
    size(600, 800)
    stroke(255, 0, 0)
    strokeWeight(3)
    global natezenie 
    natezenie = 0
    global index
    index = 0
    frameRate(10)
    global szerokosc
    szerokosc = 0
    global wysokosc
    wysokosc = 0

def draw():
    global natezenie
    natezenie = natezenie + 1
    if natezenie == 255:
        natezenie = 0
    line(mouseX, mouseY, width/3, height/3)
    fill(0, 0, natezenie, 120)
    rect(400, 40, 120, 140)
    fill(0, natezenie, 0, 120)
    global szerokosc
    global wysokosc
    szerokosc += 1
    wysokosc += 1
    rect(szerokosc, wysokosc, 100, 100)
    slownik = {"czerwony":(255, 0, 0), "niebieski":(0, 0, 255), "zielony":(0, 255, 0)}
    print(slownik["zielony"])
    stroke(*slownik["zielony"])
    lista = []
    global index
    for nazwa, wartosc in slownik.items():
        lista.append(wartosc)
    index += 1
    if index == 3:
        index = 0
    stroke(*lista[index])
    
def mousePressed():
    exit()
    

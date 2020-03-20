def setup():
    size(600, 600)
    stroke(255, 192, 203)
    strokeWeight(3)
    global natezenie 
    natezenie = 0
    global szerokosc
    szerokosc = 300
    global wysokosc
    wysokosc = 0
    global szybkoscWys
    szybkoscWys = 5
    global szybkoscSzer
    szybkoscSzer = 5

def draw():
    global natezenie
    
    natezenie = natezenie + 1
    if natezenie == 184:
        natezenie = 0
    
    global szerokosc
    global wysokosc
    global szybkoscWys
    global szybkoscSzer
    
    szerokosc = szerokosc + szybkoscSzer
    if (szerokosc > width  or szerokosc < 0):
        szybkoscSzer = szybkoscSzer *-1
        
    wysokosc = wysokosc + szybkoscWys
    if (wysokosc > height  or wysokosc < 0):
        szybkoscWys = szybkoscWys *-1
            
    fill(natezenie, 3, 255, 120)
    circle(szerokosc, wysokosc, 70)
    
def mousePressed():
    exit() #to miało być poo okrążeniu samo, a nie na klik
    
#1,25 pkt bo nie są użyte kolekcje do ustawiania kolorów, a je różnież mieliśmy powtórzyć
    

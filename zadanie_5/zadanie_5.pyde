class Kulka():
    
    def __init__(self, a, pozx, pozy, pr, r, g, b):
        self.nazwa = a
        self.colorr = r
        self.colorg = g
        self.colorb = b
        fill(3,255,120)
        self.klikniety = False
        self.pozx = pozx
        self.pozy = pozy
        self.pr = pr
        
    def RysujKulke(self):
        if self.klikniety:
            fill(self.colorr, self.colorg, self.colorb) 
        else:
            fill(3,255,120)
        
        circle(self.pozx, self.pozy, self.pr)

    def kliknij(self):
        if odl(mouseX, mouseY, self.pozx, self.pozy) < self.pr:
            print(self.nazwa) 
            self.klikniety = not self.klikniety

def setup():
    size(600, 400)
    background(255)
    stroke(100, 192, 203)
    strokeWeight(3)
    global kulka1 
    global kulka2 
    global kulka3 
    global kulka4
    global kulka5 
    global kulka6
    kulka1 = Kulka("kulka1", 100, 120, 150, 255, 5, 120)
    kulka2 = Kulka("kulka2", 100, 290, 150, 120, 100, 255)
    kulka3 = Kulka("kulka3", 300, 120, 150, 100, 100, 200)
    kulka4 = Kulka("kulka4", 300, 290, 150, 255, 255, 5)
    kulka5 = Kulka("kulka5", 500, 120, 150, 200, 55, 100)
    kulka6 = Kulka("kulka6", 500, 290, 150, 255, 100, 100)

def draw():
    kulka1.RysujKulke()
    kulka2.RysujKulke()
    kulka3.RysujKulke()
    kulka4.RysujKulke()
    kulka5.RysujKulke()
    kulka6.RysujKulke()
    
def odl(x1, y1, x2, y2):
  import math

  roz_y = y1 - y2
  roz_x = x1 - x2

  return math.sqrt(roz_x * roz_x + roz_y * roz_y)
    
def mousePressed():
    kulka1.kliknij()
    kulka2.kliknij()
    kulka3.kliknij()
    kulka4.kliknij()
    kulka5.kliknij()
    kulka6.kliknij()
    

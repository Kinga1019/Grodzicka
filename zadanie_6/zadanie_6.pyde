import math

class Kolo():
    def __init__(self, promien): 
        self.promien = promien
    def sketch(self, x, y):
        self.x = x
        self.y = y
        circle(self.x, self.y, self.promien)
        
class PasiasteKolo(Kolo): 
    def sketchPasiaste(self, x, y, paski): 
        Kolo.sketch(self, x, y) 
        space = self.promien/paski 
        _xLinii_ = 0 
        r = self.promien/2
        for pasek in range(0, (paski+1)/2): 
            line(x+_xLinii_, y-math.sqrt(r * r - _xLinii_ * _xLinii_), x+_xLinii_, y+math.sqrt(r * r - _xLinii_ * _xLinii_))
            _xLinii_ += space
        for pasek in range(0, (paski+1)/2): 
            line(x+_xLinii_-r, y-math.sqrt(r * r - (r -_xLinii_) * (r -_xLinii_)), x+_xLinii_-r, y+math.sqrt(r * r - (r -_xLinii_) * (r -_xLinii_)))
            _xLinii_ -= space
            
class KoloroweKolo(Kolo):
    def sketchKolorowe(self, x, y, r, g, b):
        Kolo.sketch(self, x, y)
        self.r = r
        self.g = g
        self.b = b
        fill(self.r, self.g, self.b)
            
def setup():
    size(600, 600)
    maleKoloroweKolo = KoloroweKolo(50)
    maleKoloroweKolo.sketchKolorowe(100, 200, 0, 128, 0)
    srednieKoloroweKolo = KoloroweKolo(90)
    srednieKoloroweKolo.sketchKolorowe(400, 450, 184, 3, 255)
    duzeKoloroweKolo = KoloroweKolo(180)
    duzeKoloroweKolo.sketchKolorowe(500, 150, 255, 192, 203)
    maleKolo = Kolo(40) 
    maleKolo.sketch(300, 400) 
    duzeKolo = Kolo(210)
    duzeKolo.sketch(120, 400)
    maleKolo.sketch(50, 100) 
    malePasiasteKolo = PasiasteKolo(30) 
    malePasiasteKolo.sketchPasiaste(500, 200, 10) 
    sredniePasiasteKolo = PasiasteKolo(60)
    sredniePasiasteKolo.sketchPasiaste(150, 200, 12) 
    duzePasiasteKolo = PasiasteKolo(140)
    duzePasiasteKolo.sketchPasiaste(300, 100, 20)
    duzePasiasteKolo.sketch(450, 300) 
    

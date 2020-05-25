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
            
def setup():
    size(600, 600)
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
    

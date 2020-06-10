from abc import ABCMeta, abstractmethod 
class Pet():
    __metaclass__=ABCMeta 
    @abstractmethod 
    def speak(self): 
        super().__init__()
        return 'no sound'
    
class Cat(Pet): 
    def __init__(self, name):
        self.name = name
    def speak(self): 
        text('meow', random(50, width-70), random(50, height-50))
        return 'meow'
    def __add__(self, other): 
        return self.name[0]+ ' i ' + other.name[0]
class Dog(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self):
        text('woof', random(50, width-70), random(50, height-50))
        return 'woof'
    def gimmePaw(self):
        image(loadImage("lapa.png"), random(50, width-70), random(50, height-100))
    def __add__(self, other): 
        return self.name[0]+ ' i ' + other.name[0]
class Bunny():
    pass
class Hedgehog(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self):
        text('PISK', random(50, width-60), random(50, height-70))
        return 'PISK'
    def gimmeHog(self):
        image(loadImage("jez.png"), random(50, width-70), random(50, height-100))
    def __radd__(self, other): #nie kojarzę takiej funkcji wbudowanej, a na pewno nie odpowiada za odejmowanie
        return self.name[0]+ ' i ' - other.name[0] # nie zadziałą, bo jak ma odjąć pierwsze litery od siebie?
    def __sub__(self, other): # jakby sprawdzić w specyfikacji to tak włąśnie brzmi zarezerwowana wbudowana nazwa na operację odejmowania
        pass # tu trzebaby zaimplementować co ma się zadziać jeżeli odejmujemy od siebie jeże
        
def setup():
    size(600,600)
    textSize(20)
    rex = Dog('Rex') 
    benio = Dog('Benio')
    skrypcik = Cat('Skrypcik') 
    janusz = Bunny() 
    kuro = Hedgehog('Kuro')
    kenma = Hedgehog('Kenma')
    global list_of_pets
    list_of_pets = [rex, benio, skrypcik, kuro, kenma] 
    print(isinstance(skrypcik, Pet)) 
    print(rex+benio) 
    print(isinstance(benio, Pet))
    print(benio+kuro)
    print(kuro - kenma)
    print(skrypcik+skrypcik)  # nie wywołujesz odejmowania, a wciąż dodawanie, które jest zaimplementowane w innych klasach

def draw(): 
    pass
    
def mouseClicked():
    for pet in list_of_pets:
        pet.speak() 
        if isinstance(pet, Dog):
            pet.gimmePaw() 
        if isinstance(pet, Hedgehog):
            pet.gimmeHog()
            
# 1,5pkt

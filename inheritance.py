class vehicle():
    def __init__(self,model):
        self.model=model
    def start(self):
        print(f"{self.model} arac baslatılıyor...")

class car(vehicle):
    def __init__(self,model):
        super().__init__(model)
class truck(vehicle):
    def __init__(self,model):
        super().__init__(model) # super( kalıtım aldıgım clası ifade eder)
        print(f"{self.model} kamyonet baslatılıyor...") # method overriding
# polymorphism araştır
class motocyle(vehicle):
    def __init__(self,model):
        super().__init__(model)
        
car1=car("hyundai")
car1.start()
truck1=truck("scania")
truck1.start()
class car(): # nesne kalıbı
    # constructor - yapıcı method
    def __init__(self, model, year=2025):
        self.__model=model
        self.year=year  
        print("car nesnesi oluşturuldu")
    def start(self,a): # self classın kendisi
        print(f"{self.__model} {self.year} {a} araba çalıştırılıyor...")
        self.startengine()
    def startengine(self):
        print("Motor başlatılıyor...")
    def set_model(self,model):
        if len(model)< 3:
            print("model ismin min 3 hane olmalıdır")
            return
        self.__model=model
    def get_model(self):
        return self.__model
          
car1=car("Toyota") # car instance

car1.set_model("ab") # get-set
print(car1.get_model()) # get
car1.start(1)

car2=car("BMW",2020) # car classının yapıcı methodu
print(car2.get_model()) # get
car2.start(2)


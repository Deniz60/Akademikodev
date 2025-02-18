# sınıflar>= class
# modules
#paket yönetimi

class human:
    name="deniz"
    #built in
    #constructor
    #initiliaze
    def __init__(self,name):
        self.name= name

        print("bir human instance üretidi")
    def __str__(self):
        return f"str foksiyonunda dönen değer: {self.name}"
    def talk(self,sentence):
        
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking...")
# instance => örnek
human1= human("ismail")
human1.talk("merhaba")
human1.walk()
print(human1)

human2= human("mehmet")
human2.talk("selam")
human2.walk()
print(human2)
faiz = 1.59
vade = 36
krediAdi = "İhtiyaç Kredisi"
print(type (faiz))
print(type (vade))
print(type (krediAdi))

print(int(vade)+ 12)

faiz = str(faiz)
print(type (faiz))
vade= 36 #int(input("girmek istediginiz vade sayısını giriniz: "))
print(type(vade))
vade= vade+12
print("sectigimiz vade sonucu: " + str(vade))
print("sectigimiz vade sonucu: {vadesayisi} " .format(vadesayisi=vade))
print(f"sectigimiz vade sonucu: {vade}")

isim = "Halit"
metin = "Merhaba {name}".format(name=isim)
print(metin)

metin= f"hoşgeldiniz {isim}"
print(metin)

dizi= ["ihtiyaç kredisi", 10, 5.2, True ]
print(dizi)

krediler= ["ihtiyaçkredisi", "taşitkredisi", "konutkredisi "]
print(type(krediler))
print(krediler[0])
print(krediler[1])
print(krediler[2])
print(len(krediler))
krediler.append("özel kredi")
print(krediler)

krediler.append("x kredisi")
print(krediler)
krediler.pop()
print(krediler)
krediler.append("taşitkredisi")
print(krediler)
krediler.remove("taşitkredisi")

print(krediler)

krediler.extend(["y kredisi", "z kredisi"])

print(krediler)

for i in range(10):
    print("xxxxxxxx")
    print(i)
    
print("*****************")
for i in range(5, 10): 
    
    print(i)

print("*****************")

for i in range(0, 51, 10):
    print(i)
print("*****************")

krediler= ["ihtiyaçkredisi", "taşitkredisi", "konutkredisi"]

for kredi in krediler:
    print(kredi)
print("*****************")

for i in range(len(krediler)):
    print(krediler[i])
print("*****************")
i=0
while i< 10:
    print("x")
    i+=1
    

print("y")
print("*****************")
while True:
    print("x")
    break
print("*****************")    
i=0
while i< len(krediler):
    
    print(krediler[i])
    i+=1
    if krediler[i]=="konutkredisi":
        break
    
# fonksionlar
print("*****************") 
fiyat =100
indirim=20

def calculate():
    print(100-20)
    
def calculatewithparams(fiyat,indirim):
    print(fiyat-indirim)
        
def sayhello(name):
    print(f"merhaba {name}")    

def calculateandreturn(fiyat, indirim):  
    return fiyat-indirim
yenifiyat= calculateandreturn(200,50)
print(yenifiyat)
calculate()
calculatewithparams(50,10)
sayhello("deniz")
sayhello("mevlüt")

def calculateprice(price, discount):
    print(price-discount)
def calculatepriceandreturn(price, discount):
    return price-discount
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
fonk1=calculateprice(100,50)
fonk2=calculatepriceandreturn(300,100)

print(fonk1)

print(fonk2)

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")


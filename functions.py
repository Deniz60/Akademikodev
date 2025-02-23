#fonksiyonlar 
# kullanılabilirlik ve bakım maliyeti azaltma

print("functions")

price = 100
total_price = price+ (price*0.2)
print(total_price)
print("****************************************")
# tanımlama sırası> required argümanlar sonra default argümanlar
def calculate_tax(price,rate=20):
    total_price = price+ (price*(rate/100))
    return total_price
    
price1=calculate_tax(100)
price2=calculate_tax(200)
price3=calculate_tax(600,20)
price4=calculate_tax(900,76)

print(price1)
print(price2+50)

def empty():
    pass

empty()

print("****************************************")
# *args bu parametre bir tuple olarak(liste) kullanıcı kac adet gönderirse o kadar gelecek

def sum(*a):
    result=0
    for sayi in a:
        result+=sayi
    return result
    
print(sum(1,5))
print(sum(1,5,67,34,32,23))


# **kwargs => araştıralım ve 1 örnek kullanım yapalım


#
# lambda tek satırlık fonk syntax alternatif
topla =lambda a,b : a+b

print(topla(5,7))
selamla= lambda isim : print(f"merhaba {isim}")

selamla("Deniz")
# Değişken sayıda anahtar-değer çifti alan fonksiyonlar için kullanılır.
def example_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


example_function(name="deniz", age=21, city="istanbul")

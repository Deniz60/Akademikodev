def topla(a,b):
    return a+b

def cikar(a,b):
    return a-b

def carp(a,b):
    return a*b

def bol(a,b):
    if b==0:
        return "Sıfıra bölmeye çalışıyosunuz"
    return a/b

print(topla(13,12))
print(cikar(13,12))
print(carp(13,12))
print(bol(13,12))
print(bol(13,0))

def polindrom(kelime):
    return kelime == kelime[::-1]
def harf(kelime):
    return kelime.isalpha()
kelime = input("kelime giriniz: ")
if(harf(kelime)):
    if polindrom(kelime):
        print(f"{kelime} bir polindromdır")
    else:
        print(f"{kelime} bir polindrom değildir")
else:
    print("Girdiğiniz kelime alf olmalıdır")    
    
def son100(yaş):
    if yaş>=100:
        return "100 yaşını geçmişsiniz"
    else:
        fark= 100-yaş
        return fark
yaş= int(input("yaşınızı giriniz: "))
değer=son100(yaş)

print(f"{yaş} yaşındasınız, {değer} yıl sonra 100 olucaksınız..")
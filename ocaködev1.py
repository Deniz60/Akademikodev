ad= (input("adınızı giriniz: "))
yaş= int(input("yaşınızı giriniz: "))
dogum_yılı= int(input("dogum yılınızı giriniz: "))

print(f"merhaba {ad}! {yaş} yaşındasın ve {dogum_yılı} yılında doğmuşsun.")

def topla():
    return sayi1+sayi2
def çıkar():
    return sayi1-sayi2
def carp():
    return sayi1*sayi2
def bol():
    if sayi2!=0:
        return sayi1/sayi2
    else:
        return "sıfıra bölünmeye çalışıyorsunuz"
    

sayi1= int(input("sayi giriniz: "))
sayi2= int(input("sayi giriniz: "))
print(topla())
print(çıkar())
print(carp())
print(bol())


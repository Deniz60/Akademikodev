sayi = int(input("sayi giriniz:" ))

if sayi % 2 == 0:
    print("girilen sayi cifttir")
else:
    print("girilen sayi tekdir")
    
notu = int(input("not giriniz: "))

if 100 >= notu >= 90:
    print("notunuz A")
elif 89 >= notu >= 80:
    print("notunuz B")
elif 79>= notu >=70:
    print("notunuz C")
elif 69 >= notu >= 60:
    print("notunuz D")
elif 59 >= notu >=0:
    print("notunuz F")
else:
    print("gecersiz not girdiniz!!!!!")
    
    
yaş = int(input("yaş giriniz: "))

if 0 <= yaş <= 12:
    print("Çocuk")
elif 13 <= yaş <= 19:
    print("Genç")
elif 20 <= yaş <= 59:
    print("Yetişkin")
elif yaş >= 60:
    print("Yaşlı")
else:
    print("Geçersiz yaş girdiniz!!!!!")
    
        
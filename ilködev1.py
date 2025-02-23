print("Kodlamaio")
baslik = "Taşıt Kredisi"
print(baslik)
#string => metinsel ifade
baslik = "İhtiyaç Kredisi"
print(baslik)
#int, integer => tam sayı
vade = 36
vade2 = "36"
ekVade=6
# float, decimal, double
aylikodeme =200.50
#bool, boolean => True veya False
yukselisteMi = False
#matematiksel operatörler
print(5 + 5)

print(vade +12)
print(vade + ekVade)
print(36 + 6)
print(5-5)
print(vade-12)
print (vade - ekVade)
print(36-6)

print(5*5)
print(vade * 2)
print(vade * ekVade)
print(10*10)

print(5/5)
print(vade / 2)
print(vade/ekVade)
print(10/2)
################################
yenivade = vade / 2
fiyat = 100
indirimliFiyati = fiyat - 20
print(yenivade)
print(indirimliFiyati)
#% => mod operator
print(10%2)
print(vade % 5)
print(vade % ekVade)
print (30 % 10)

# mantıksal operatörler
print(1 == 1)
print(1 == 2)
# CTRL K + CTRL C
print(1 > 2)
print(3 > 1)
print (1 > 1)
print (1 >= 1)
print(1 < 2)
print(3 < 1)
print(1 < 1)
print(1 <= 1)
print(1!=1)
print(1!=2)


#or => veya
print(1 > 2 or 5 > 2)
print(1 > 2 and 5 > 2)
print(1 > 2 or 5 > 2 and 3 > 2)
print(1 > 2 and 5 > 2 and 3 > 2)
print(2 > 1 or 1 > 2 and 3 > 2)

#karar yapıları
# if else
sayi1 = 15
sayi2 = 15
# sayil sayi2'den büyükse ekrana sayi 1 daha büyük yazdır
#condition
#indent
if sayi1 <= sayi2:
    print("Sayi 1 Sayi 2'den büyüktür")
    print("Hala if bloğunun içerisindeyim")
elif sayi1 == sayi2:
    print("Sayi 1 Sayi 2'den eşittir")
else:
    print("Sayi 1 Sayi 2'den büyüktür")
    
print("Burası if bloğunun dışıdır.")

if sayi1 <=sayi2:
    print("Sayi 1 Sayi 2'den küçüktür")
if sayi1 == sayi2:
    print("İki sayi eşittir")
else:
    print("Sayi 1 Sayi 2'den büyüktür")
print("Burası if bloğunun dışıdır.")

#ilk video bitti.----------------------------------------------------------------


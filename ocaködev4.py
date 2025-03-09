liste=[]
for i in range(0,5):
    sayi=int(input(f"{i+1}. sayıyı giriniz. "))
    liste.append(sayi)
toplam=sum(liste)
print(f"Girdiğiniz sayılar: {liste}")
print(f"listenin toplamı: {toplam}")
print(f"listenin ortalaması: {toplam/len(liste)}")
print(f"listenin en büyük elemanı: {max(liste)}")
print(f"listenin en küçük elemanı: {min(liste)}")

liste2=[]
for i in range(0,5):
    kelime=(input(f"{i+1}. kelimeyi giriniz. "))
    liste2.append(kelime)
print(f"Girdiğiniz kelimeler: {liste2}")
liste2.reverse()
print(f"ters hali: {liste2}")
list(set(liste2))
print(f"tekrarsız hali: {liste2}") # benzersiz tekrarları kaldırır
tuple=(1,2,3,4,5)
print(tuple)   # tuple oluşturulduktan sonra degiştirilemez, parantez ile gösterilir
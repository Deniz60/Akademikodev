def asal_mi(sayi):
    if sayi <= 1:  # 1 ve negatif sayılar için kontrol
        return f"{sayi} 2 veya daha büyük olmalıdır."
    
    for i in range(2, sayi): 
        if sayi % i == 0:
            return f"{sayi} asal degildir"
    
    return f"{sayi} asaldir"  # Döngüden çıkarsa asaldır

n = int(input("Sayı giriniz: "))
print(asal_mi(n))

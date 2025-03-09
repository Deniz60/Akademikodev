#dosya işlemleri yazma, okuma

def dosya_yaz():
    with open('dosya.txt', 'w') as dosya:
        for i in range(5):
            satir = input(f"Lütfen {i+1}. satır veriyi girin: ")
            dosya.write(satir + '\n')
def dosyayi_Oku():
    with open('dosya.txt', 'r') as dosya:
        print("Dosyanın İçeriği: tanıtım")
        for satir in dosya:
            print(satir.strip()) #boşluklar için


dosya_yaz()
dosyayi_Oku()


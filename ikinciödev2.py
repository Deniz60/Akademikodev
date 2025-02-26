def hesap_makinesi(sayi1, sayi2,sembol):
    if sembol == '+':
        return sayi1+sayi2
    elif sembol == '-':
        return sayi1-sayi2
    elif sembol == '*':
        return sayi1*sayi2
    elif sembol == '/':
        if sayi2!= 0:
            return sayi1/sayi2
        else:
            return "Sıfıra bölünmeye çalışıyorsunuz"
    else : return "geçersiz işlem türü"    

print(hesap_makinesi(13, 14,'+'))
print(hesap_makinesi(13, 14,'-'))
print(hesap_makinesi(13, 14,'*'))
print(hesap_makinesi(13, 14,'/'))
print(hesap_makinesi(13, 14,'%'))
print(hesap_makinesi(13, 0,'/'))
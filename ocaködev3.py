for i in range(1,100):
    print(f"{i+1}. eleman {i}")
    
for i in range(1,100):
    if i%2==0:
        print(f"cift sayi {i}")

sayi= int(input("faktoriyeli alınacak sayıyı giriniz: "))
i=1
faktoriyel=1
while i<=sayi:
    faktoriyel *= i
    i=i+1
print(f"{sayi}! = {faktoriyel}")   

def asal_mı(sayi2):
    if sayi2 < 2:
        return False
    for i in range(2, sayi2):
        if sayi2 % i == 0:
            return False
    return True

for sayi2 in range(1,100):
    if asal_mı(sayi2):
        print(f"{sayi2}. sayi asal")
    
        
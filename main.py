print("hello world")
age =50
print(age)
age =25
print(age)
print(type(age))
age="merhaba"
print(age)
print(type(age))

print(1+1)
print(5-1)
print(5*2)
print(25/5)
print(25//5)
print(101/5)
print(101//5)
print(5**3)
print(100%3)

name="deniz"
number=50
number+=10
number-=5
print(number)
number2=5
number2 **=3
print(number2)

print(1==1)
print(1==2)
print(10>5)
print(10>=10)
print(10<=5)
print(1!=2)
print("deniz"=="deniz")
print("car">"bus")

print(1==1 and 10>5)
print(1==1 and 5<3)
print(1==1 or 10>5)
print (1==1 or 5<3)

print(1==1 and 5>3 or 10==10 and 5>=5)
print(1==1 and 5<3 or 10==10 and 5>=5)
print(1==1 and 5<3 or 10==10 and 5>=6)
# soldan öncelik not> and > or
print((1==1 and 2>5) or 6>=6 and (10>5 or 5==5))

print (not 1==1)
students = ["emir","yasin","emirhan","barış","zeynep",5, 10.1 ,2 ]
print(students)
a=5
b=a
b+=4
print(a)
print(b)

students2 = students

students2.append("ahmet")

print(students)
print(students2)

# dögüler
#indentation scopeları belirler
for i in range(5):
    print(i)
    print("merhaba") # main> for scope
print("for bitti")# main scope

for i in range(5,10): # i isim bezerliği
    print(i)
   
for i in range(5,50,5):
    print(i)

students3= ["ali","aybüke","büşra","deniz"]
for student in students3:
    print("hesaplama yapılıyor: "+ student)
print("*********************************")
for student in students3:
    if student == "büşra":
        continue # devam et döngüye
    print("hesaplama yapılıyor: "+ student)
print("*********************************")
for student in students3:
    if student == "büşra":
        break # manuel olarak bitirmeyi hedefler
    print("hesaplama yapılıyor: "+ student)


#
# while

#while True: # while sonsuz döngü (infinite loop)
  #  print("while")

x=50
while x<100:
    print(x)
    x+=1

user_imput= input("kullanıcıdan değer alınız, cıkmak için q tuşuna basınız.")
while user_imput!= "q":
    print(f"girdiniz:  {user_imput}")
    user_imput= input("kullanıcıdan değer alınız, cıkmak için q tuşuna basınız.")

#

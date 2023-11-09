"""
f = 5
s = 7
print(s+f) #12

a = "furkan"
print(a[1]) #u
print(a[-2]) #a
# print(a[6]) #out of range error
print(a[2:4]) #rk # 2. ve 3. indexi yazdırır
print(a[:4]) #furk
print(a[2:]) #rkan
print(a[:]) #furkan
print(a[:-1]) #furka
print(a[::2]) #fra # 1-3-5. indexleri yazdı
print(a[::-1]) #nakruf
"""

"""
isim = "ebru"
print(len(isim))

a=25
print(float(a)) #25.0

b= 3.14
print(int(b)) #3

c= "12345"
print(int(c)+1) #12346
"""

"""
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))  #I want 3 pieces of item 567 for 49.95 dollars.

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) #I want to pay 49.95 dollars for 3 pieces of item 567.
"""

"""
print("furkan\tçetin") #furkan	çetin
print("furkan","çetin") #furkan çetin
print("furkan\nçetin") #furkan
                       #çetin
print(1,2,3,4,sep="-") #1-2-3-4

print(*"Python") #P y t h o n
print(*"Python",sep="/") #P/y/t/h/o/n

print("{:.2f},{:.3f}".format(3.14564,9.897569)) #3.15,9.898
"""

"""
liste= [1,"sdfasf",5,8]
print(type(liste)) #<class 'list'>
print(len(liste)) #4
print(liste[2]) #5

liste2=[1,2,3]
print(liste2*2) #[1, 2, 3, 1, 2, 3]

liste2[0]=10
print(liste2[:2]) #[10, 2]

print(liste2) #[10, 2, 3]

liste2.append("Python") #[10, 2, 3, 'Python']
print(liste2)

liste2.pop()
print(liste2) #[10, 2, 3]

liste2.pop(0)
print(liste2) #[2, 3]

listeM =[15,6,7,1,56,41,69,2,37]
listeM.sort()
print(listeM) #[1, 2, 6, 7, 15, 37, 41, 56, 69]
listeM.sort(reverse=True)
print(listeM) #[69, 56, 41, 37, 15, 7, 6, 2, 1]

listeL=[[1,2],[3,4],[5,6],[7,8]]
print(listeL[2][1]) #6

print(listeM*3)
"""

"""
tuple=(1,1,1,2,2,3,4,5,5) #listelerden en temel farkı değiştirilemiyor olmasıdır
print(tuple.count(1)) #3
print(tuple.index(3)) #5

dictionary={"bir":1,"iki":2,3:"üç",4:[1,2,3,4],5:[[1,2],[3,4]]}

print(dictionary["bir"]) #1
print(dictionary[3]) #üç

print(dictionary[5][0][1]) #2

dic2={"sayılar":{1:"bir",2:"iki",3:"üç"}}
print(dic2["sayılar"][2]) #iki

print(dic2.keys()) #dict_keys(['sayılar'])
print(dic2.values()) #dict_values([{1: 'bir', 2: 'iki', 3: 'üç'}])
print(dic2.items()) #dict_items([('sayılar', {1: 'bir', 2: 'iki', 3: 'üç'})])
"""

"""
k=input("Enter a value:")
print("Your value is:",k)

a=int(input("Enter a num:"))
print(a*3)

print(1!=2 and 3 <=5) #True
print(1==2 or 3 <=5) #True
print(1==2 or 3 >=5) #False
print(not "ali" != "murat") #False
print("A" > "B") #False

if(5<8):
    print("Yes")

age = int(input("Enter age:"))

if age >= 18 and age < 60:
    print("You can drink alcohol")
elif age >=60 :
    print("You can drink but not much")
else :
    print("You can't drink")

firstNum= int(input("Enter first num:"))
process= input("Enter process(+,-,*,/):")
secondNum= int(input("Enter second num:"))

if(process=="+"):
    print(firstNum+secondNum)
elif(process=="-"):
    print(firstNum-secondNum)
elif(process=="*"):
    print(firstNum*secondNum)
elif(process=="/"):
    print(firstNum/secondNum)
else:
    print("Wrong selection")
"""

"""
print(5 in [1,2,3,4]) #False
print("ab" in "Merhaba") #True
print(not 5 in [1,2,3,4]) #True

liste =[1,2,3,4]
for eleman in liste:
    print(eleman)

list =[(1,2),(3,4),(5,6),(7,8)]
for (i,j) in list:
    print("i:{} j:{}".format(i,j))

dictionary={"bir":1,"iki":2,"üç":3}
for (i,j) in dictionary.items():
    print("Key:",i,"Değer:",j)
"""

"""
i=0
while(i<10):
    print(i)
    i+=1 # i++ ifadesi pythonda kullanılmıyor

print(*range(20)) #0 dan 19 a kadar sayıları yazar
print(*range(1,8)) #1 den 7 ye kadar sayıları yazar

# YILDIZLA ŞEKİL ÇİZME ÖRNEĞİ
k=4
for i in range(1,10,2):
    print(" "* k, "*"*i)
    k=k-1
                           
l=0
for i in range(9,0,-2):
    print(" "*l,"*"*i)
    l=l+1

i=0
while(i<10):
   if( i == 5 ):
        break  #Döngünün dışına çıkar
   print("i:",i)
   i+=1

for i in range(1,10):
    if(i==3 or i==5):
        continue #Değerleri atlar
    print("i:",i)
"""

"""
liste3 = [1,2,3,4,5]
liste4 = [i for i in liste3]
print(liste4) #[1, 2, 3, 4, 5]

listeNew=[]
listeNested = [ [1,2],[3,4],[5,6]]
for i in listeNested :
    for x in i:
        listeNew.append(x)
print(listeNew) #[1, 2, 3, 4, 5, 6]

listeNew2 = [x for i in listeNested for x in i]
print(listeNew2) #[1, 2, 3, 4, 5, 6]
"""

""" DÖNGÜLERLE OLUŞTURULMUŞ KULLANICI GİRİŞİ
sys_kullanıcı_adı="furkan"
sys_parola=12345
giriş_hakkı=3

while True:
     input_k=input("Kullanıcı adını giriniz:")
     input_p=int(input("Parolayı giriniz:"))

     if(input_k == sys_kullanıcı_adı and input_p==sys_parola):
         print("Giriş Yapılıyor...")
         break
     else:
        print("Kullanıcı adı veya parola hatalı.")
        print("Tekrar deneyiniz")
        giriş_hakkı -=1

     if giriş_hakkı==0:
         print("Hesabınız bloke olmuştur.")
         break
"""

"""
# BİR SAYININ FAKTÖRİYELİNİ BULMA
while True:
    sayı = input("Enter a num:")
    if(sayı=="q"):
        print("Program sonlandırılıyor...")
        break
    else:
        sayı = int(sayı)
        faktöriyel=1

        for i in range(2,sayı+1):
            faktöriyel *= i
        print(faktöriyel)
"""

"""
# Fibonacci dizisini bulma

a=1
b=1
fibonacci=[a,b]
for i in range(20):
    a,b=b,a+b
    fibonacci.append(b)
print(fibonacci)
"""

"""
a = [1,2,3,4,5]

a.insert(1,"Furkan")
a.append("Python")
print(a) #[1, 'Furkan', 2, 3, 4, 5, 'Python']
a.pop()
print(a) #[1, 'Furkan', 2, 3, 4, 5]

help(a.append) #Metodun ne yaptığını söyler

def selamla():
    print("Merhaba")
    print("Nasılsınız ?")

selamla()

def isim_yaz(isim):
    print("İsminiz:",isim)

isim_yaz("Ebru")

def faktöriyel_hesapla(sayı):
    faktöriyel=1
    if(sayı==0 or sayı==1):
        print(faktöriyel)
    else:
        while (sayı >=1):
            faktöriyel*=sayı
            sayı-=1
        print("Faktöriyel:",faktöriyel)

faktöriyel_hesapla(9)

def toplama(a,b,c):
    return a+b+c

def ikiyleçarp(a):
    return a*2

toplam=toplama(1,2,3)
print(ikiyleçarp(toplam)) #12
print(ikiyleçarp(toplama(1,2,3))) #12

def selamla(isim="İsimsiz"):
    return isim
print(selamla()) #İsimsiz
print(selamla("Ali")) #Ali

def toplama(*a): #Tuple şeklinde tutulur
    print(a)
toplama(1,2,3,4,5) #(1, 2, 3, 4, 5)

def toplama(*a):
    toplam=0
    for i in a:
        toplam+=i
    print(toplam)
toplama(1,8,4,7) #20

d=5
def fonksiyon():
    global d
    d=3
    print(d)
fonksiyon() #3
print(d) #3

# if ve while gibi kısımların içinde yazılan değişkenler global değişken olur.
# fonksiyon içindeki değişken yerel değişkendir.

e=5
if True:
    e=4
    print(e) #4
print(e) #4

liste1=[1,2,3,4,5]
liste2=[i*2 for i in liste1]
print(liste2) #[2, 4, 6, 8, 10]

def ikiyleçarp(x):
    return x*2
print(ikiyleçarp(3)) #6

ikiyleçarp2 = lambda x : x*2
print(ikiyleçarp2(3)) #6

toplama= lambda x,y,z : x+y+z
print(toplama(1,5,3)) #9
"""

""" Asal olup olmadığını bulma
def asalmı(sayı):
    if(sayı ==1 ):
        return False
    elif(sayı==2):
        return True
    else:
        for i in range(2,sayı):
            if(sayı%i==0):
                return False
        return True

while True:
    num = input("Bir sayı giriniz:")
    if( num == "q"):
        print("Programdan çıkılıyor...")
        break
    else:
        num = int(num)

        if(asalmı(num)):
            print(num, "asal sayıdır")
        else:
            print(num,"asal değildir")

asalmı(num)
"""

""" Tam bölenleri bulma
tam_bölen_liste = []
def tam_bölen_bul(sayı):
    for i in range(1,sayı+1):
        if(sayı % i == 0):
            tam_bölen_liste.append(i)
    for i in range(len(tam_bölen_liste)):
        print(tam_bölen_liste[i])

tam_bölen_bul(999)
"""

import math

print(dir(math)) #Kullanılabilecek fonsiyonların isimleri görünür

print(math.factorial(5)) #120
print(math.floor(5.6)) #5
print(math.ceil(5.2)) #6

import math as matematik

print(matematik.factorial(4)) #24

from math import * # math kütüphanesi içindeki bütün fonsiyonları elde etmek için
print(factorial(6)) #720*

from math import floor,ceil # math kütüphanesinden sadece 2 tane fonksiyon aldık
print(floor(6.8)) #6



import modül1

print(modül1.toplama(1,8,3)) #12
print(modül1.programlama_dilleri) #['Python', 'Php', 'Java', 'C']

import random
import time

rastgele_sayı = random.randint(1,40) #1 ile 40 arasında rastgele sayı döndürür

print(rastgele_sayı)
while True:
    sayı=input("Tahmininizi giriniz:")
    sayı= int(sayı)
    if(sayı == rastgele_sayı):
        print("Bildiniz.Tebrikler")
        break
    else:
        print("Kontrol ediliyor...")
        time.sleep(1) #Program 1 saniyeliğine durur
        print("Tekrar deneyin")









import turtle
import time
import random

WIDTH,HEIGHT = 500,500     #ekran boyutları tanımlandı
COLORS = ['red','green','blue','orange','yellow','black','pink','purple','brown','cyan']  #rastgele seçilecek kaplumbağa renkleri listeye atandı

def yariscisayisi() :   #yarışacak kaplumbağa sayısını alacak fonksiyon
    yariscilar = 0
    while True :        #yanlış değerler girilmesi halinde tekrar değer istenmesi için döngü
        yarisci = input('Yarışçı sayısı giriniz : ')
        if(yarisci.isdigit()) :   #girilen değerin sayısal olup olmadığını tespit eder
            yariscilar = int(yarisci)
        else :
            print('Girilen değer sayısal değil')
            continue

        if(2<=yariscilar<=10) :   #girilen değerin istenilen aralıkta olup olmadığını kontrol eder
            return yariscilar
        else :
            print('İstenilen aralıkta bir değer giriniz(2-10)')


def yaris(renkler): #belirlenen renk sayısı kadar kaplumbağa yarışacak
    kaplumbagalar = kaplumbagaolusturma(renkler)  #yarış fonksiyonun içinde çağrılan fonksiyon ile kaplumbağalar oluşturulacak.
    while True:
        for yarisci in kaplumbagalar:
            mesafe = random.randrange(1,20) #1 ile 20 piksel arasında rastgele belirlenen piksel kadar kaplumbağa yukarı gidecek
            yarisci.forward(mesafe)

            x,y = yarisci.pos()  #kaplumbağanın koordinatları
            if(y>=HEIGHT//2 - 10) : #400 pikel bir ekranda 390'a ulaşıldığında (yani y=190) yarış biter
                return renkler[kaplumbagalar.index(yarisci)] #kazanan kaplumbağa , kaplumbağalar listesinin indexinden tespit edilip rengi elde edilir

def kaplumbagaolusturma(renkler): #belirlenen renk sayısı kadar kaplumbağa oluşturulacak
    kaplumbagalar = []            #fonksiyonun sonunda yarışacak kaplumbağa listesi boş şekilde oluşturulur
    kaplumbagabosluk = WIDTH // (len(renkler)+1)  #yarışacak kaplumbağa sayısının bir fazlası x ekseni uzunluğuna bölünerek kaplumbağalar arası eşit uzunluk belirlenir

    for i,renk in enumerate(renkler):   #i rengin sırasını, color rengi tutar, enumerate(colors):renk listesindeki her rengi ve index numarasını döner
        yariscisayisi = turtle.Turtle() #ekranda nesne oluşturur
        yariscisayisi.color(renk)       #nesnenin rengini belirler
        yariscisayisi.shape('turtle')   #nesnenin şeklini belirler
        yariscisayisi.left(90)          #nesneler her zaman sağa dönük oluşturulduğu ve yarış aşağıdan yukarıya olacağı için nesnenin yönü 90 derece sola çevrilir(yukarı doğru bakar).
        yariscisayisi.penup()           #merkezde oluşturulan kaplumbağanın yarış çizgisine gelene kadar iz bırakmaması sağlanır.
        yariscisayisi.setpos(-WIDTH//2 + (i + 1) * kaplumbagabosluk , -HEIGHT//2 + 20)  #400'e 400 bir ekranın 0.indeksindeki yani soldan 1.sırasındaki kaplumbağa için (i=0) (x,y)=(-120,-180)
        #setpos(x , y):kaplumbağayı ekrandaki belirli bir koordinata taşır
        yariscisayisi.pendown()         #yarış sırasında kaplumbağa iz bırakacak hale getirilir
        kaplumbagalar.append(yariscisayisi) #Oluşturulan kaplumbağa nesnesi kaplumbagalar listesine eklenir
    return kaplumbagalar

def ekranolusturma():
    screen = turtle.Screen()       #turtle modülüyle ekran başlatıldı
    screen.setup(WIDTH,HEIGHT)     #ekran belirtilen boyutlarda oluşturuldu
    screen.title('Kaplumbağa Yarışı')

yariscisayisi = yariscisayisi()   #fonksiyon çağrıldı 
ekranolusturma()

random.shuffle(COLORS)            #renkler karıştırılır
renkler = COLORS[:yariscisayisi]  
# .. : .. -> (1:4 ->1'den 4'e kadar)
# (:4) , (0:4) aynı şey yani alınan yarışmacı sayısı kadar(örnekte 4) renk oluşturulacak)

print("Kaplumbağa renkleri:", renkler)              #kullanıcıya yarışacak kaplumbağa renkleri belirtilir
tahmin = input("Hangi renk kaplumbağa kazanacak? ") #kullanıcı belirtilen renklerden tahminde bulunur

kazanan = yaris(renkler)   #yarış fonksiyonu çağırılıp yarış başlatılır ve kazanan değişkene atanır

if(tahmin == kazanan) :
    print(f"Tahmininiz doğru, tebrikler! {kazanan} renkteki kaplumbağa kazandı!")
else :
    print(f"Maalesef {kazanan} renkteki kaplumbağa kazandı. Tahmininiz yanlıştı.")








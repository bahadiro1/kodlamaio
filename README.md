*** Python Veri Tipleri *** 

int : Tam sayılardır.  ex: 15,4,100

string(str) : Metinsel karakter içeren ifadelerdir. Tek tırnak işareti veya çift tırnak işareti içinde ifade edilmektedir.

bool : Sadece True veya False değerlerini alabilien mantıksal veri türüdür. 

float : Ondalıklı sayılardır.  ex: 5.78 

set : dictionary, list, tuple vb. veri türlerini içeren veri tipidir.

dictionary : Bir anahtar kelime ve bir değer barındırır.  ex: {"elma":4, "armut":2"}

list : Sıralı nesnelerden oluşan değerler barındırır.  ex: [5,6,7]

tuple : List ile aynıdır, tek farkı atanan değerler değiştirilemez.  ex: ("ahmet","mehmet")


*Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.

Kursların tamamlanma yüzdesini gösteren sayılar integer.
Kategori ve Eğitmenler list veri tipidir.
Kurslarım kısmı string veri tipidir.

*Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.

Kurslarım sayfasına girdiğimizde sırasıyla; Ders Programı, Değerlendirme ve Ödev kısımları çıkıyor.


islem=input("""Yapmak istedğiniz işlemi seçin:
x)Ders Programı
y)Değerlendirme
z)Ödev
""")
if islem=="x":
    print("Ders Programı Gözüküyor")
elif islem=="y":
    print("Değerlendirmeler gözüküyor")
elif islem=="z":
    print("Ödevler gösteriliyor")  

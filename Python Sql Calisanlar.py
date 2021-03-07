import sqlite3
import time

baglanti=sqlite3.connect("calisanlar.db")
imlec=baglanti.cursor()

def tablo_olusturma():
    imlec.execute("CREATE TABLE IF NOT EXISTS calisanlar(İsim TEXT,Soyisim TEXT,Yas INT,Departman TEXT,Maas INT)")
    baglanti.commit()

def veri_ekleme():
    imlec.execute("INSERT INTO calisanlar VALUES('Samet','KILIÇ',35,'Alım Satım Müdürü',7400)")
    baglanti.commit()
    
def klavyeden_veri_alinarak_ekleme(isim,soyisim,yas,dept,maas):
    imlec.execute("INSERT INTO calisanlar VALUES(?,?,?,?,?)",(isim,soyisim,yas,dept,maas))
    baglanti.commit()

def tablodaki_verileri_okuma():
    imlec.execute("Select * FROM calisanlar")
    tablo=imlec.fetchall()
    for i,j,k,l,m in tablo:
        print(i,j,k,l,m )


while True:
   isim=input("Calisanin ismini giriniz yada Eger Çıkış yapmak istiyorsanız q ya basiniz")
    
    if isim=='q':
        print("\nÇıkış işleminiz başarıyla gerçekleşti...")
        time.sleep(1)
        break
    else:
        soyisim=input("\nCalisanin soyismi:")
        yas=int(input("\nCalisanin yasi:"))
        dept=input("\nCalisanin depertmani:")
        maas=int(input("\nCalisanin maasi:"))
        klavyeden_veri_alinarak_ekleme(isim,soyisim,yas,dept,maas)
        print("\nTabloya ekleme yapiliyor...\n")
        time.sleep(1)    



#tablodaki_verileri_okuma()
#veri_ekleme()
#tablo_olusturma() 


baglanti.close()

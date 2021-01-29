#Bir televizyon kumandası uygulaması
#İşlemler : 1,2,3,4

from random import randint as r

class Kumanda:
    def __init__(self,tvDurum=False,tvSes=0,kanalListesi=["Trt"],kanal="Trt"):
        print("Kumanda nesnemiz olusturulmaktadır")
        self.TvSesi = tvSes
        self.TvDurumu = tvDurum
        self.KanalListesi = kanalListesi
        self.Kanal = kanal
    def SesAzaltArttir(self):
        while True:
            if self.TvDurumu!=True:
                print("Lutfen önce tv'yi acınız")
                break
            karakter = input("Sesi azaltmak icin '<', Arttırmak icin '>', Cıkıs icin 'q' tusuna basınız")
            if karakter =='<' and self.TvSesi!=0:
                self.TvSesi -=1
            elif karakter=='>' and  self.TvSesi!=15:
                self.TvSesi+=1
            elif karakter =="q":
                print("Ses => {}.. Menüden cıkılıyor...".format(self.TvSesi))
                break
            print("Ses => {}".format(self.TvSesi))
    def TvKapat(self):
        if self.TvDurumu ==True:
            print("Tv Kapatılıyor")
            self.TvDurumu =False
        else:
            print("Tv zaten kapalı")
    def TvAc(self):
        if self.TvDurumu ==False:
            print("Tv Acılıyor")
            self.TvDurumu = True
        else :
            print("Tv zaten acık")
    def RastgeleKanal(self):
        rastgele = r(0,len(self.KanalListesi)-1)
        self.Kanal = self.KanalListesi[rastgele]
        print("Su anki kanal => {}".format(self.Kanal))
    def KanalEkle(self,kanal):
        print("Kanal eklendi. Eklenen kanal => {}".format(kanal))
        self.KanalListesi.append(kanal)
    def KanalBilgileriniGoster(self):
         for x in self.KanalListesi:
             print(x)
    def __str__(self):
        return "Tv Durumu: {}\nSes: {}\nKanallar:{}\nSu anki kanal : {}\n".format(self.TvDurumu,self.TvSesi,self.KanalListesi,self.Kanal)



























import numpy as np

#from matplotlib import pyplot as plt



                        ###veriler ####
giris=np.array([[0, 1, 0],  #bağımsız değişkenler  sütunu
                   [0, 1, 1],
                   [0, 0, 0],
                   [1, 0, 0],
                   [1, 1, 1],
                   [1, 0, 1]])


cıkıs=np.array([[0], [0], [0], [1], [1], [1]]) #bağımlı değişkenler sütunu


                        ##### ####




class yps():
    def __init__(self,giris,cıkıs):#ön işlemler verilerin yps ağına parametre olarak göderilir. ağırlıkları vs standart örnekleme işlemleri...
        self.giris=giris
        self.cıkıs=cıkıs
        self.agırlık=np.array([[.50], [.50], [.50]]) #ağırlıkları dilediğiniz gibi değiştirerek değişimi inceleyebilirisniz.

        self.hata_gecmisi=[]
        self.dönem_listesi=[]




    def aktivasyonfc(self,x,anahtar=False):
        if anahtar==True:
            return x * (1 - x)
        return 1/(1+np.exp(-x))   #sigmoid fonskiyondur genellikle sınıflama algoritmalarında benzer özelliklerden hangi sınıfta olduğunu tahmin etmekiçin kullanırız bu formülü


    def ileri_besleme(self):
        self.besleme=self.aktivasyonfc(np.dot(self.giris, self.agırlık))#np.dot  çarpımını alıyor


    def geri_yayılım(self):
        self.hata=self.cıkıs-self.besleme
        delta=self.hata * self.aktivasyonfc(self.besleme,anahtar=True)
        self.agırlık +=np.dot(self.giris.T, delta)



    def deneme(self,devir=25000):# 0.1. işlem deneme fonk çağrılır ve çalışmaya başalnır örneklenen sinir ağı ve öğrenmeye başlar 
        for devir in range(devir):
            self.ileri_besleme()#1. işlem besleme çarpılık geri yayılıma yollanır. ve aktivasyon fonksiyonuna yollanır.
            self.geri_yayılım()#
            self.hata_gecmisi.append(np.average(np.abs(self.hata)))#mutlak değer alır  math.abs aynıdır karışmaması için np.absolute() yazabilirsiniz.

            self.dönem_listesi.append(devir)



    def tahmin(self,yeni_giris):
        tahmin_islem=self.aktivasyonfc(np.dot(yeni_giris, self.agırlık))
        return tahmin_islem








YSA=yps(giris, cıkıs)

YSA.deneme()



example = np.array([[1, 1, 1]])
example_2 = np.array([[0, 1, 1]])
print(YSA.tahmin(example), ' - Gerçek: ', example[0][0])
print(YSA.tahmin(example_2), ' - Gerçek: ', example_2[0][0])


#-Eee kardeşim ikisinide bilemedi ne yapacağız ?  Merak etmeyin bu iyi haber sinir ağımız overfiting yapmamış!  
#Bu tip verilerden çokça denerseniz ne kadar başarılı olup olmadığını sayarak anlayabilirsiniz.

from numpy import *



def hata_miktarı_maliyeti(c,m,veriseti):
    toplam_hata = 0
    # Iterate
    for i in range(0, len(veriseti)):
        x = veriseti[i, 0]
        y = veriseti[i, 1]
        toplam_hata += (y - (m * x + c)) ** 2
    return toplam_hata / float(len(veriseti))

def yarı_kademeli_dusurme(c, m,veriseti, ogrenme_oranı):
    
    c_yarı_k_d=0
    m_yarı_k_d=0
    N = float(len(veriseti))
    for i in range(0,len(veriseti)):
        x=veriseti[i,0]
        y=veriseti[i,1]
        
        c_yarı_k_d += - (2/N)*(y-((m * x)+ c ))# gerçek değerden tahmin değeri çıkarıyorum -(2/N)... devam .. aşşağıda.. 
        m_yarı_k_d += - (2/N)*x*(y-((m * x)+ c))# gerçek değerden tahmin değeri çıkarıyorum
    
    yeni_c= c-(ogrenme_oranı*c_yarı_k_d) #çıkan sonucu öğrenme oranıyla çarpıp değeri güncelliyorum sayının negatifini alarak
    yeni_m= m-(ogrenme_oranı* m_yarı_k_d)#çıkan sonucu öğrenme oranıyla çarpıp değeri güncelliyorum pozitif değere döner eğer  desent eğrisi yukarı dönük değilse
    print("c değeri {} m değeri{}".format(yeni_c,yeni_m))
    return [yeni_c,yeni_m]


def kademeli_düsürme(veriseti,baslangıc_c,baslangıc_m,ogrenme_oranı,ogrenme_tekrarı):
    
    c=baslangıc_c
    m=baslangıc_m
    for i in range(ogrenme_tekrarı):
        c,m=yarı_kademeli_dusurme(c,m,array(veriseti),ogrenme_oranı)
    return c,m
    print(veriseti,baslangıc_c,baslangıc_m,ogrenme_oranı,ogrenme_tekrarı)




def anafonc():
  
    veriseti=genfromtxt('data.csv' , delimiter=',')
    ogrenme_oranı=0.0001
    
    baslangıc_c=0
    baslangıc_m=0
    
    ogrenme_tekrarı=10000
    
    [c, m]=kademeli_düsürme(veriseti,baslangıc_c,baslangıc_m,ogrenme_oranı,ogrenme_tekrarı)
    
    hata_miktarı=hata_miktarı_maliyeti(c,m,veriseti)
    print("m degeri :{0} c degeri{1}  o_tekrarı:{2} hata_miktarı:{3}".format(m,c,ogrenme_tekrarı,hata_miktarı))


          
          
          
          
          
          

if __name__ == '__main__':
    anafonc()
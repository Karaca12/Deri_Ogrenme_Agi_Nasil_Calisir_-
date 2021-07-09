# Deri_Ogrenme_Agi_Nasil_Calisir_-
Derin öğrenme ağının nasıl çalıştığını, ileri ve geri yayılımların nasıl çalıştığını bulabileceksiniz.
Daha doğrusu bir yapay sinir ağı nasıl öğrenir onu burada anlamaya çalışacağız. Çok fazla sinir ağıyla katmanlı modelleme yapmadan önce 1 yapay sinir ağı nasıl çalışır bunu öğrenmek çok kıymetlidir. Öğrenme tam olarak nedir, nasıl çalışır  bunları **yapaysiniragı.py   dosyasında incelemeye başlayın !!**

## Yapay sinir ağı neye benzer ?
<br>

Sinir Sistemi	| Yapay Sinir Ağı
<br>
1.Nöron	|1.İşlem Elemanı
<br>
2.Dentrit	|2.Toplama Fonksiyonu
<br>
3.Hücre Gövdesi|	3.Aktivasyon Fonksiyonu
<br>
4.Akson	|4.Eleman Çıkışı
<br>
5.Sinaps|5.Ağırlıklar
<br>
<img width="900" height="500" src="https://github.com/Karaca12/Deri_Ogrenme_Agi_Nasil_Calisir_-/blob/main/sinirag%C4%B11.jpg">

### İyi güzelde nasıl çalışyor ?
Veriye ihtiyaç olduğunu söylüyorum ve geçiyorum. Klasik olarak bir methodun ihtiyacı olan bir girdi ve çıktı silsilesi düşünüldüğünde.
Neyse! 
Öncelikle öğrenme ve tahmin işlemlerinin farklı şeyler olduğunu kesinlikle aklına kazımalısın.
Öğrenme işlemi ayrı zamanda koşturulur,tahmin işlemi ayrı zamanda.
Burada anlaştıysak devam edelim.

Öncelikle deneme() yada try() fonskiyonu koşmaya başlar ; Bu fonksiyon öğrenme işlemidir.
bu fonksiyonun altında şu fonksiyonlar koşturulur;

1.ileriyayılım() koştur. --> giriş ve önceden belirlediğimiz (değişkenlere atadğımız ağırlıklarla çarpımını alır) bir değişkene sonuçları kaydeder ve geriyayılım methoduna gönderir()
2.geriyayılım() koştur --->   gerçek sonuçtan tahmin değerini çıkarır. bu hata miktarı olarak kaydeder. ve bunuda günün sonu sonunda başlangıçta belirlediğimiz ağırlıklara ekleme/çıkarma yaparak bias yani ön yargın değerlerimizi verir. 



### Tahmin Nasıl Çalışıyor ? 

ileri ve geri yayılım methodlarımız sayesinde başlangıçta belirlediğimiz ağırlıklar  yapılan try(), deneme() ,öğren() her neyse  altında çalışan ileir ve geri yayılım  methodları sayesinde ağırlıkları başlangıç ağırlıklarına ekleyerek yada çıkarark yeni biaslar elde ederi. ve bunun sonunda aktivasyon fonksiyonu ateşlenir ve biz sınıflama aktivasyon fonksiyonu oluşturmuşsak   1 yada 0  döndürür girilen değere bağlı olarak.



## Aktivasyon  kod'da : def aktivasyonfc():
<img align="left" width="900" height="500" src="https://github.com/Karaca12/Deri_Ogrenme_Agi_Nasil_Calisir_-/blob/main/aktivasyon%20fonksiyonu.png">

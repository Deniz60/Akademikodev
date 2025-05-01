1. Decision Tree (Karar Ağacı)
Decision Tree, bir veri setindeki örüntüleri öğrenmek ve bu örüntüleri kullanarak yeni verileri sınıflandırmak veya tahmin etmek için kullanılan bir makine öğrenmesi algoritmasıdır. Temel olarak, veri setini dallara ayırarak karar verme sürecini ağaç yapısı şeklinde modelleyen bir yöntemdir.

Nasıl Çalışır?

Kök Düğüm (Root Node): Ağacın başlangıç noktasıdır ve tüm veri setini içerir.
Düğümler (Nodes): Veri setini bölmek için kullanılan kararları temsil eder. Her düğüm, bir öznitelik (feature) üzerinde bir test yapar.
Dallar (Branches): Testin sonucuna göre veri setinin bölündüğü yolları temsil eder.
Yaprak Düğümleri (Leaf Nodes): Ağacın en altındaki düğümlerdir ve sınıf etiketlerini veya tahmin değerlerini içerir.

Avantajları:

Yorumlanabilirlik: Ağaç yapısı oldukça anlaşılır ve yorumlanabilir.
Kullanım Kolaylığı: Özellik ölçeklendirme gibi ön işlemler gerektirmez.
Görselleştirme: Ağaç yapısı görselleştirilebilir ve anlaşılması kolaydır.

Dezavantajları:

Aşırı Uyum (Overfitting): Karmaşık ağaçlar veri setine aşırı uyum sağlayabilir ve genelleme yapamaz.
Dengesizlik: Veri setindeki küçük değişiklikler ağacın yapısını büyük ölçüde değiştirebilir.

2. Rastgele Orman (Random Forest)
Random Forest (Rastgele Orman) algoritması; birden çok karar ağacı üzerinden her bir karar ağacını farklı bir gözlem örneği üzerinde eğiterek çeşitli modeller üretip, sınıflandırma oluşturmanızı sağlamaktadır.

Kullanım kolaylığı ve esnekliği; hem sınıflandırma hem de regresyon problemlerini ele aldığı için benimsenmesini ve kullanımının yaygınlaşmasını hızlandırdı.

Algoritmaya yönelik en beğenilen nokta ise; veri kümeniz üzerinde çeşitli modellerin oluşturulması ile kümenizi yeniden ve daha derin keşfetme imkanı sunmasıdır.

Algoritma;

Analiz edilecek veri seti hazırlanır,
(Analiz edilecek küme oluşturulur, gerekli görülürse veri temizlemesi gerçekleştirilir.)
Algoritma her bir örnek için karar ağacı oluşturur ve her bir karar ağacının tahmini değer sonucu oluşur,
Tahmin sonucu oluşan her değer için oylama gerçekleştirilir,
*(Sınıflandırma problemi için Modu (Mode), Regresyon problemi için Ortalamayı (Mean))
Son olarak algoritma son tahmin için en çok oylanan değeri seçerek sonuç oluşturur.
 adımları ile analiz gerçekleştirmektedir. 
 
 Avantajları:

Daha Düşük Overfitting Riski: Birden fazla ağaç kullanıldığı için overfitting riski azalır.
Daha Yüksek Doğruluk: Tek bir ağaca göre daha iyi genelleme yapar ve daha doğru tahminler sağlar.
Esneklik: Hem sınıflandırma hem de regresyon problemlerinde kullanılabilir.

Dezavantajları:

Yorumlanabilirlik: Tek bir ağaca göre daha az yorumlanabilir.
Hesaplama Gereksinimi: Daha fazla ağaç kullanıldığı için eğitim süresi daha uzundur.
 
 
 







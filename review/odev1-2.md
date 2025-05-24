**Aktivasyon Fonksiyonu Nedir?**
Sinir ağının önemli bir parçası, aldığı bilgiye göre bir nöronun etkinleştirilip etkinleştirilmeyeceğini seçen bir etkinleştirme işlevidir. Aktivasyon fonksiyonunun ana işlevi ağı daha az doğrusal hale getirmektir. Girdilerin yalnızca ölçeklendirildiği ve toplandığı doğrusal bir model altında ağın çıktısı da girdilerin doğrusal bir birleşimi olacaktır.

**Doğrusal Olmamanın Önemi**
Sinir ağlarının başarısında önemli bir faktör doğrusal olmamadır. Gerçek dünyadaki birçok olay ve bağlantı doğası gereği doğrusal olmadığından bu önemlidir. Yalnızca temel doğrusal bağlantıları simüle edebildikleri göz önüne alındığında, doğrusal aktivasyon fonksiyonlarının karmaşık modelleri yakalama yetenekleri sınırlıdır. Doğrusal olmama olmasaydı, sinir ağları yalnızca doğrusal işlevleri temsil edebilirdi; bu da onların karmaşık sorunları ele alma kapasitelerini önemli ölçüde sınırlayacaktı. Öte yandan sinir ağları, doğrusal olmayan aktivasyon fonksiyonları sayesinde verilerdeki karmaşık ilişkileri tahmin edip ifade edebilmektedir. Ağlara, gerçek dünyada meydana gelen karmaşıklıkları ve doğrusal olmayan ilişkileri yansıtan karmaşık modelleri öğrenme ve simüle etme yeteneği sağlarlar.

**Aktivasyon Fonksiyonu Türleri?**
*Sigmoid Aktivasyon fonksiyonu*
Çoğu kişi sigmoid aktivasyon fonksiyonunu kullanmayı tercih eder. S-şekilli bir eğri ile girdiyi 0 ile 1 arasındaki bir aralığa aktarır. Amaç iki sınıftan hangisinin gerçekleşeceğini tahmin etmek olduğunda ikili sınıflandırma sorunları için kullanılabilir. Sigmoid fonksiyonu, girdiyi olasılıksal bir aralıkta yoğunlaştırarak belirli bir sınıfa ait olma olasılığı olarak anlaşılabilecek anlaşılır bir çıktı üretir.

*Tanh aktivasyon fonksiyonu*
Girdiyi -1 ile 1 arasında bir aralığa çevirse de hiperbolik tanjant (tanh) aktivasyon fonksiyonu, S şeklinde bir eğriye sahip olması nedeniyle sigmoid fonksiyonla karşılaştırılabilir. Tanh, sınıf olasılıklarına çevrilebilecek olasılıksal bir çıktı üreterek, sigmoid işlevine benzer şekilde ikili sınıflandırma konularında yardımcı olur. Tanh fonksiyonu, sıfır merkezli çıktılar üretme avantajına sahiptir ve bu, belirli modellerin eğitimi için faydalı olabilir.

*Düzeltilmiş Doğrusal Birim (ReLU)*
Doğrultulmuş Doğrusal Birim (ReLU) olarak bilinen yaygın olarak kullanılan aktivasyon işlevi, pozitif girişleri orijinal değerlerinde tutarken tüm negatif girişleri sıfırlar. Bu basit aktivasyon kuralının yardımıyla ReLU, verilere doğrusal olmama özelliği ekleyebilir ve verilerdeki karmaşık kalıpları tespit edebilir. ReLU'nun hesaplama verimliliği ana faydalarından biridir. Aktivasyon fonksiyonunun hesaplanması, basit eylemler gerektirdiğinden diğer fonksiyonlara göre daha kolaydır. Ancak ReLU'nun bazı zorlukları var.

*Softmax aktivasyon fonksiyonu*
Softmax işlevi, amaç bir girdiyi birkaç potansiyel sınıftan birine kategorize etmek olduğunda, çok sınıflı sınıflandırma sorunlarında sıklıkla kullanılır. Gerçek değerlerin girdi vektörünü olasılık dağılımına göre normalleştirir. Softmax işlevi, çıktı olasılıklarının toplamının 1'e kadar çıkmasını sağlar, bu da onu bir arada bulunamayan sınıfları içeren durumlar için uygun hale getirir. Softmax fonksiyonu, çıktıları, girdilerin her bir sınıfa düşme olasılığı olarak yorumlamamızı sağlayan bir olasılık dağılımı oluşturur.

**Backpropagation Nedir?**
Backpropagation (geri yayılım), yapay sinir ağlarının eğitiminde kullanılan bir algoritmadır. Ağın her bir katmanındaki hata miktarını hesaplar ve bu hataları azaltmak için ağın parametrelerini (ağırlıkları) günceller.

**Optimizer Nedir?**
Optimizer, sinir ağı eğitiminde kullanılan bir algoritmadır. Ağın kaybını (loss) azaltmak için ağırlıkları ve diğer parametreleri günceller. Bu işlem, geriye doğru hesaplama (backpropagation) sonrasında yapılır.

**Optimizer Türleri:**

*Gradient Descent (GD)*: En temel optimizer türü, her adımda ağırlıkları kayıp fonksiyonunun negatif gradyanına göre günceller.

*Stochastic Gradient Descent (SGD)*: GD'nin mini-batch şeklidir, her adımda rastgele seçilen küçük bir veri alt kümesi üzerinde çalışır.

*Adam Optimizer*: Adaptive Moment Estimation (Adam), yaygın olarak kullanılan bir optimizerdir. Hızlı ve etkili bir şekilde öğrenme oranını ayarlar.

*RMSprop*: Root Mean Square Propagation, ağırlıkların güncellenmesinde gradyan karelerinin hareketli ortalamasını kullanır.

*Adagrad*: Her parametrenin öğrenme oranını ayrı ayrı adapte eder, nadir görülen olaylar için iyi çalışabilir.
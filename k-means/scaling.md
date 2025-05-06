Verinin dağılımı: Verinin normal dağılıp dağılmaması, bazı algoritmaların çalışmasını etkileyen bir faktör. Veriler sağa yatık, ya da sola yatıksa, model performansı bu durumdan etkilenebilir.
Özellikler arasındaki ölçek farklılıkları: Klasik bir örnekten gidecek olursak, verimiz yaş ve gelir boyutlarını içeriyor olsun. Yaş aralığı 0-90 yaşlarını kapsıyor ve gelir boyutu da 0- 250.000 TL arasında değerler içeriyor olsun. Burada Öklid, Manhattan gibi uzaklık bazlı hesaplamaları kullanan algoritmalar için değerler sapacaktır. Bu bağlamda bu özellliklerin ortak bir veri aralığına çekilmesi ile daha doğru sonuçlar elde edebiliriz.
Bu değerleri normal hale getirmek ve baskınlığı azaltmak adına bazı yöntemler mevcuttur. Bunlar, normalizasyon, standardizasyon gibi metodlardır. Bu metodlar uzaklık tabanlı ve gradyan tabanlı tahminleyici algoritmaları kullanmadan önce uygulanması faydalı olan yöntemlerdir. Peki bu metodlar nedir ve hangi durumlarda kullanılır?

**MinMax Scaling**, verinin 0 ile 1 arasında değerler aldığı bir durumdur. Burada dağılım, verinin dağılımı ile benzerdir. Burada ‘outlier’ denilen dışta kalan verilere karşı hassasiyet durumu vardır, bu yüzden bu değerlerin fazla olduğu bir durumda iyi bir performans gösteremeyebilir.

**Robust Scaler**, Normalizasyon ile benzer şekilde çalışır. Aykırı değerlere sahip verilerde daha iyi sonuçlar verebilir. Yine veri dağılımı ile benzerlik gösterir ancak aykırı değerler dışarıda kalır. Medyan değeri sonradan kullanılmak üzere elenir ve değerler 1.ve 3. kartil aralığına oturtulur.

**MaxAbs Scaler**, her özelliğin maksimum mutlak değeri 1 olacak şekilde her özelliği ayrı ayrı ölçeklendirir ve dönüştürülür.

**Standardizasyon**, ortalama değerin 0, standart sapmanın ise 1 değerini aldığı, dağılımın normale yaklaştığı bir metoddur. Formülü şu şekildedir, elimizdeki değerden ortalama değeri çıkartıyoruz, sonrasında varyans değerine bölüyoruz.

**PowerTransformer**, varyansı stabilize etmek ve çarpıklığı en aza indirmek için en uygun ölçeklendirme faktörünü bulur. Yine ortalama değerin 0, standart sapmanın ise 1 değerini aldığı bir metoddur.
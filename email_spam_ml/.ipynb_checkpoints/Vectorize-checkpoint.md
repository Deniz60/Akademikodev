Vectorize ifadesi, metin verilerinin sayısal bir formata dönüştürülmesi anlamına gelir. Bu işlem, makine öğrenimi algoritmalarının metin verilerini işleyebilmesi için gereklidir.
TF-IDF (Term Frequency-Inverse Document Frequency) ise, metin vektörizasyonunda kullanılan bir tekniktir ve her bir kelimenin bir belge içindeki önemini hem sıklığına (TF) hem de tüm belge koleksiyonundaki (IDF) tersine sıklığına göre hesaplar. 
Bu süreçte:
TF, bir kelimenin belgede ne sıklıkta geçtiğini toplam kelime sayısına bölerek hesaplar. 
IDF, bir kelimenin tüm belgelerdeki oranını dikkate alarak, kelimenin genel önemini azaltır. 
TF-IDF değerleri, metinlerin benzerliklerini ve farklılıklarını daha doğru bir şekilde analiz etmek için kullanılır.

Term Frequency (TF)
Örneğin:
E-posta metni: "buy cheap cheap office software now"
"cheap" kelimesi 2 kez geçiyor. Toplam 6 kelime varsa:
→ TF(cheap) = 2/6 = 0.33

Inverse Document Frequency (IDF)
Sık geçen kelimeler (örneğin: "the", "email", "please") düşük IDF alır.
Nadir ve anlamlı kelimeler yüksek IDF alır.

TF × IDF = TF-IDF
Aynı dokümanda sık geçen,
Ama genel olarak nadir olan kelimeler öne çıkar.

TF-IDF Vectorizer Ne Yapar?
TfidfVectorizer sınıfı şunları yapar:

Tüm veri setini inceler.
Her metni bir kelime vektörüne dönüştürür (her kelime için TF-IDF skoru).
Vektörler genellikle sparse matrix (seyrek matris) olarak saklanır.

|              **Avantajı**         |            **Açıklama**         |

| **Önemli kelimeleri öne çıkarır** | Nadir ama anlamlı kelimelere yüksek skor verir |
| **Genel kelimeleri ezer**         | "the", "email", "please" gibi kelimeler düşük etkiye sahiptir |
| **Sayısal forma dönüştürür**      | Makine öğrenmesi için zorunludur |
| **Esnektir**                      | `ngram`, `max_df`, `min_df` gibi ayarlarla çok özelleştirilebilir |



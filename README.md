# 🚀 Quantum_Force - Kuantum Algoritması Yarışması

Bu depo, Kuantum Algoritması Yarışması kapsamında geliştirdiğimiz projenin kaynak kodlarını ve dokümantasyonunu içermektedir.

## 👥 Ekibimiz

* **Takım Kaptanı:** Mehmet Çelik
* **Ekip Üyeleri:**
  * Muhammet Berat Beket
  * Muhammet Berat Yanar
  * Hüsne Nur Kurt
  * Saria Taljo
  * Zeynep Aslan

---

## 🎯 Proje Karar ve Geliştirme Süreci Özeti

Projenin fikir aşamasında ekibimizle birlikte haberleşme afet lojistiği finans ve bankacılık gibi farklı sektörler üzerinde detaylı bir beyin fırtınası gerçekleştirdik ilk başta veriyi ve sektörü tamamen soyutlayıp arkadaki matematiksel şablonu tahminleme regresyon anomali tespiti siber güvenlik ve kuantum optimizasyonu olarak sabit tutan modüler ve hibrit bir yapı kurmayı tartıştık bu sayede aynı motora banka verisi beslendiğinde zırhlı araç rotalaması afet verisi beslendiğinde ise iha haberleşme rotalaması yapabilen sektörel bağımsız bir platform oluşturmayı hedeflemiştik

Ancak ekibimizle yaptığımız detaylı kısıt analizi ve tartışmalar sonucunda şu önemli kararları aldık ve projenin yönünü netleştirdik

* **Neden Afet ve Haberleşme Senaryolarından Vazgeçtik:** Afet anı öncelik tahminlemesi için gerçekçi ve somut veri setlerine ulaşmanın neredeyse imkansız olduğunu gördük sentetik veri setleri projenin gerçekçiliğini azaltıp jüri gözünde okul projesi muamelesi görmesine yol açabilirdi ayrıca sahada drone cell veya mobil baz istasyonlarının şarj optimizasyonları eşzamanlı hareket kısıtları ve sinyal kopma riskleri gibi elimizde donanım olmadan hayalden kodlanamayacak çok fazla beklenmedik teknik sürpriz barındırıyordu siber atak durumunda afet bölgesindeki bir istasyonu insan hayatı söz konusu olduğu için haritadan öylece çıkaramayacak olmamız da kurduğumuz anomali mantığıyla çelişiyordu llm ile kriz raporlaması ve telegram botu işi de eylemin ön planda olduğu afet anında havada kalıyordu
* **Neden Hibrit Modeli Eledik:** Yarışma kısıtlarını ve kısıtlı süremizi göz önüne aldığımızda odağımızı %50 %50 bölmenin projenin kalitesini düşüreceğine karar verdik tek bir alana %100 yoğunlaşmak jüri karşısında işe ne kadar hakim olduğumuzu göstermek ve daha kusursuz bir kod mimarisi çıkarmak için en mantıklı yoldu ayrıca jürinin ticari uygulanabilirlik maliyet azaltma ve finansal karşılık bulma beklentilerine en iyi cevap veren alanın bankacılık olduğunu gördük
* **Nihai Karar ve Bankacılık Modeli:** Tüm bu riskleri bertaraf etmek için ayakları yere basan somut veri setine erişebileceğimiz ve simülasyonunu koordinat sistemiyle tıkır tıkır gösterebileceğimiz bankacılık alanına odaklanmayı seçtik kurduğumuz matematiksel şablonu atmlerin geçmiş para çekme verilerini regresyonla analiz edip önümüzdeki 24 saat için kritiklik skoru çıkaran mesafe ve zırhlı araç kapasitesine göre gezgin satıcı + knapsack problemlerini kuantum qaoa vqe algoritmalarıyla çözen anomali içeren işlemleri ve siber atakları filtreleyen ve kriz anında llm destekli raporu telegramdan fırlatan bütünleşik bir bankacılık zırhlı araç operasyon sistemine dönüştürdük

Komitenin alana dair son dakika kontenjan veya problem değişiklikleri yapma ihtimalini bilerek arkadaki modüler matematik motorumuzu her duruma hazırlıklı olacak şekilde esnek tuttuk ama enerjimizin tamamını bu somut bankacılık şablonu üzerinden kusursuz kodlamaya harcayacağız geliştirme sürecinde önce kuantum ml istatistik ve python temellerini bireysel eğitimlerle sağlamlaştırıp ardından beraber veri dönüştürme fonksiyon modelleme ve algoritma mimarisi adımlarına geçerek projemizi gerçek bir kuantum bilgisayarda test edip hayata geçireceğiz

---

## 🛠 Kurulum ve Başlangıç

Projede kullanılan tüm kütüphaneleri lokal ortamınıza yüklemek için terminale şu komutu yazın:

```bash
pip install -r requirements.txt

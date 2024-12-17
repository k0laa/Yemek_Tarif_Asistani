# Tarif Uygulaması

Bu proje, yemek tariflerini detaylı bir şekilde kullanıcıya sunan bir uygulamadır. Kullanıcı, tariflerin özetini, görsellerini, kişilik bilgilerini ve hazırlanma süresini görebilir. Ayrıca farklı işlevler eklenerek daha kapsamlı bir deneyim sunulabilir.

---

## Yapılacaklar

### **Tekrar Düzenlenecekler**
- **HTML Sayfaları**:
  - Daha düzenli ve estetik bir görünüme kavuşturulacak.
  - **CSS** dosyaları eklenebilir.
  - **Bootstrap** kullanılabilir.
  - Çeşitli **UI elementleri** ile zenginleştirilebilir.

---

## Kesinlikle Eklenecekler
**`get_recipe_details` fonksiyonu ile sağlanacak ve HTML'de gösterilecek:**
- **`summary`**: Tarifin kısa özeti. (HTML formatında olabilir, Türkçeye çevirmek için `bs4` kullanılacak.)
- **`image`**: Tarifin görselinin URL'si. (Görsel doğrudan gelmezse, URL üzerinden indirilebilir.)
- **`servings`**: Tarifin kaç kişilik olduğu. (int)
- **`readyInMinutes`**: Tarifin hazırlanma süresi. (Dakika cinsinden)

---

## Eklenebilir Özellikler

### **Fonksiyon Olarak Eklenebilecekler**:
- **Random Tarif Getirme**: Rastgele bir tarif önerisi.
- **Anahtar Kelimeye Göre Tarif Getirme**: Belirli bir kelimeye uygun tarif önerileri.
- **Alışveriş Listesi Oluşturma**: Tarifin malzemeleri üzerinden liste oluşturma.
- **Tarifi Adım Adım Gösterme**: Tarifin adım adım detaylandırılması.

### **HTML'de Gösterilebilecek Ekstralar**:
- **`dishTypes`**: Tarifin türü (örnek: tatlı, ana yemek, çorba). (list)
- **`diets`**: Diyet türleri (örnek: vejetaryen, vegan). (list)
- **`cuisines`**: Tarifin ait olduğu mutfak (örnek: Türk, İtalyan). (list)
- **`analyzedInstructions`**: Adım adım talimatlar. (list)
  - **`name`**: Bölüm başlığı. (string)
  - **`steps`**: Adımlar listesi.
  - **`number`**: Adım numarası. (int)
  - **`step`**: Adım açıklaması. (string)
  - **`ingredients`**: Bu adımda kullanılan malzemeler. (list)
  - **`equipment`**: Kullanılan ekipmanlar. (list)

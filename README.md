# Tarif Uygulaması

Bu proje, yemek tariflerini detaylı bir şekilde kullanıcıya sunan bir uygulamadır. Kullanıcı, tariflerin özetini, görsellerini, kişilik bilgilerini ve hazırlanma süresini görebilir. Ayrıca farklı işlevler eklenerek daha kapsamlı bir deneyim sunulabilir.

---

## Nasıl Kullanılır? (API Keys Hakkında Rehber)

1. **API Keys Dosyasını Oluşturma**:
   - Proje dizininde `SPOONACULAR_API_KEYS.txt` adında bir dosya oluşturun.
   - Bu dosyanın içerisine kullanacağınız API anahtarlarını her satıra bir anahtar gelecek şekilde ekleyin.
   
     Örnek:
     ```
     your_first_api_key_here
     your_second_api_key_here
     your_third_api_key_here
     your_fourth_api_key_here
     ```

2. **API Keys Dosyasını Gizli Tutma**:
   - `SPOONACULAR_API_KEYS.txt` dosyasının yanlışlıkla versiyon kontrolüne dahil olmaması için `.gitignore` dosyanızda şu satırın bulunduğundan emin olun:
     ```
     SPOONACULAR_API_KEYS.txt
     ```

3. **API Keys'in Kullanımı**:
   - Uygulama çalıştırıldığında bu dosyadaki API anahtarlarını sırasıyla kullanır ve kota dolarsa bir sonraki anahtara geçer.
   - API anahtarlarının geçerliliğini ve kotasını düzenli olarak kontrol edin.



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

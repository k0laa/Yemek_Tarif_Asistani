# Tarif Uygulaması

Bu proje, yemek tariflerini detaylı bir şekilde kullanıcıya sunan bir uygulamadır. Kullanıcı, tariflerin özetini, görsellerini, kişilik bilgilerini ve hazırlanma süresini görebilir. Ayrıca farklı işlevler eklenerek daha kapsamlı bir deneyim sunulabilir.

---

## Nasıl Kullanılır? (API Keys Hakkında Rehber)

1. **API Keys Dosyalarını Oluşturma**:
   - Proje dizininde `SPOONACULAR_API_KEYS.txt` ve `DEEPL_API_KEYS.txt`  adında bir dosya oluşturun.
   - Bu dosyanın içerisine kullanacağınız API anahtarlarını her satıra bir anahtar gelecek şekilde ekleyin.
   
     Örnek:
     ```
     your_first_api_key_here
     your_second_api_key_here
     your_third_api_key_here
     your_fourth_api_key_here
     ```

2. **API Keys Dosyalarını Gizli Tutma**:
   - `SPOONACULAR_API_KEYS.txt` dosyasının yanlışlıkla versiyon kontrolüne dahil olmaması için `.gitignore` dosyanızda şu satırın bulunduğundan emin olun:
     ```
     SPOONACULAR_API_KEYS.txt
     DEEPL_API_KEYS.txt
     ```

3. **API Keys'in Kullanımı**:
   - Uygulama çalıştırıldığında dosyalardaki API anahtarlarını sırasıyla kullanır ve kota dolarsa bir sonraki anahtara geçer.
   - API anahtarlarının geçerliliğini ve kotasını düzenli olarak kontrol edin.


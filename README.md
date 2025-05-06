# Tarif Uygulaması

Bu proje, kullanıcıların evdeki mevcut malzemeleri girerek hızlı bir şekilde yemek tarifleri bulmasını sağlayan bir sistemdir. Proje, kullanıcı dostu bir arayüz, API entegrasyonları ve geniş tarif veritabanıyla yemek yapmayı kolaylaştırmayı hedefler.

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
      ```

2. **API Keys Dosyalarını Gizli Tutma**:
    - `SPOONACULAR_API_KEYS.txt` ve
      `DEEPL_API_KEYS.txt` dosyalarının yanlışlıkla versiyon kontrolüne dahil olmaması için
      `.gitignore` dosyanızda şu satırın bulunduğundan emin olun:
      ```
      SPOONACULAR_API_KEYS.txt
      DEEPL_API_KEYS.txt
      ```

3. **API Keys'in Kullanımı**:
    - Uygulama çalıştırıldığında dosyalardaki API anahtarlarını sırasıyla kullanır ve kota dolarsa bir sonraki anahtara geçer.
    - API anahtarlarının geçerliliğini ve kotasını düzenli olarak kontrol edin.

---

## `app.py` Nasıl Çalıştırılır?

1. **Gerekli Kütüphaneleri Kurun**:
    - Proje dizininde aşağıdaki komutla gerekli kütüphaneleri yükleyin:
      ```bash
      pip install -r requirements.txt
      ```

2. **Uygulamayı Çalıştırın**:
    - Konsolda aşağıdaki komutu yazarak uygulamayı başlatabilirsiniz:
      ```bash
      python app.py
      ```

3. **Kullanıcı Arayüzüne Erişim**:
    - Uygulama çalıştırıldıktan sonra konsolda aşağıdaki gibi bir çıktı alırsınız:
      ```
      * Running on http://127.0.0.1:5001/ (Press CTRL+C to quit)
      ```
    - Web tarayıcınızı açarak bu adresi ziyaret edin ve uygulamayı kullanmaya başlayın..

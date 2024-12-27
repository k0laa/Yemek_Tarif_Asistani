import deepl

last_api_key = None

def translate(text, source_lang, target_lang):
    if text is None or text == "":
        return None
    global last_api_key

    if last_api_key is not None:
        response = translate_api(last_api_key, text, source_lang, target_lang)
        if response is not None:
            return response

    api_keys = load_api_keys()
    for api_key in api_keys:
        response = translate_api(api_key, text, source_lang, target_lang)
        if response is not None:
            last_api_key = api_key
            return response
    return None


def translate_api(api_key, text, source_lang, target_lang):
    translator = deepl.Translator(api_key)
    try:
        # API'ye çeviri isteği gönder
        response = translator.translate_text(text, source_lang=source_lang, target_lang=target_lang)
        return response.text  # Çeviriyi döndür
    except deepl.DeepLException as e:
        # Kota limiti aşıldığında veya başka bir hata olduğunda burası çalışır
        if "quota exceeded" in str(e).lower():
            print("Kota bitti veya kota sınırına yaklaşıldı.")
        else:
            print(f"Hata: {e}")
        return None


def load_api_keys(filename="DEEPL_API_KEYS.txt"):
    with open(filename, 'r') as file:
        api_keys = [line.strip() for line in file.readlines()]
    return api_keys

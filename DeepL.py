import deepl
from bs4 import BeautifulSoup

last_api_key = None


# Metni çevir
def translate(text, source_lang, target_lang):
    # Boş veya None ise çevirme
    if text is None or text == "":
        return None
    global last_api_key

    # Önce son kullanılan API anahtarını dene
    if last_api_key is not None:
        response = _translate_api(last_api_key, text, source_lang, target_lang)
        if response is not None:
            return response

    # Son kullanılan API anahtarı ile çeviri yapılamadıysa diğer API anahtarlarını dene
    api_keys = load_api_keys()
    for api_key in api_keys:
        response = _translate_api(api_key, text, source_lang, target_lang)
        if response is not None:
            last_api_key = api_key
            return response
    return None


# Tarif detaylarını çevir
def translate_recipe_details(details):
    # Tarif başlığını çevir
    details['title'] = translate(details['title'], 'EN', 'TR')

    # Tarif özetini çevir
    soup = BeautifulSoup(details['summary'], "html.parser")
    summary_text = soup.get_text(separator="\n")
    details['summary'] = translate(summary_text, 'EN', 'TR')

    return details


# DeepL API'ye çeviri isteği gönder
def _translate_api(api_key, text, source_lang, target_lang):
    # API'yi başlat
    translator = deepl.Translator(api_key)

    try:
        # API'ye çeviri isteği gönder
        response = translator.translate_text(text, source_lang=source_lang, target_lang=target_lang)
        return response.text  # Çeviriyi döndür
    except deepl.DeepLException as e:
        # Kota limiti aşıldığında veya başka bir hata olduğunda burası çalışır
        if "quota exceeded" in str(e).lower():
            #print("Kota bitti veya kota sınırına yaklaşıldı.")
            pass
        else:
            print(f"Hata: {e}")
        return None


def translate_recipe_instructions(recipe_details):
    # Malzeme açıklamalarını çevir
    for ingredient in recipe_details.get('extendedIngredients', []):
        ingredient['original'] = translate(ingredient['original'], 'EN', 'TR')

    # Tarif adımlarını çevir
    if 'instructions' in recipe_details and recipe_details['instructions']:
        soup = BeautifulSoup(recipe_details['instructions'], "html.parser")
        instructions_text = soup.get_text(separator="\n")
        recipe_details['instructions'] = translate(instructions_text, 'EN', 'TR')

    return recipe_details


def translate_analyzed_instructions(analyzed_instructions):
    # Tarif adımlarını çevir
    analyzed_instructions[0]['name'] = translate(analyzed_instructions[0]['name'], 'EN', 'TR')
    for instruction in analyzed_instructions[0]['steps']:
        instruction['step'] = translate(instruction['step'], 'EN', 'TR')
        for equipment in instruction['equipment']:
            equipment['name'] = translate(equipment['name'], 'EN', 'TR')
        for ingredient in instruction['ingredients']:
            ingredient['name'] = translate(ingredient['name'], 'EN', 'TR')
    return analyzed_instructions


# API anahtarlarını yükle
def load_api_keys(filename="DEEPL_API_KEYS.txt"):
    with open(filename, 'r') as file:
        api_keys = [line.strip() for line in file.readlines()]
    return api_keys

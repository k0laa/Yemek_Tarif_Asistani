import deepl

auth_key = "c0c9ec71-49cc-4b12-9b57-f7168f9a9399:fx"  ##aylık 500.000 karakter
translator = deepl.Translator(auth_key)

def translate(text, source_lang, target_lang):
    response = translator.translate_text(text, source_lang=source_lang, target_lang=target_lang)
    return response


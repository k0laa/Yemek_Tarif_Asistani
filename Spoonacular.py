import requests
import DeepL as dl
from bs4 import BeautifulSoup

base_url = "https://api.spoonacular.com/recipes/"
recipe_count = 4


# Malzemelere göre tarif arar
def find_recipe(ingredients):
    api_keys = load_api_keys()
    for api_key in api_keys:
        # API ile tarif aramasını dene
        recipes = get_recipe_from_api(api_key, ingredients)
        if recipes is not None:
            return recipes

    return None


# Rastgele bir tarif arar
def find_random_recipe(include_tags, exclude_tags):
    api_keys = load_api_keys()
    for api_key in api_keys:
        # API ile tarif aramasını dene
        details = find_random_recipe_from_api(api_key, include_tags, exclude_tags)
        if details is not None:
            return details

    return None


# ID si gelen tarifin detaylarını getirir
def get_recipe_details(recipe_id):
    api_keys = load_api_keys()
    for api_key in api_keys:
        # API ile tarif aramasını dene
        details = get_recipe_details_from_api(api_key, recipe_id)
        if details is not None:
            return details

    return None


# ID si gelen tariflerin detaylarını getirir
def get_multi_recipe_details(recipe_ids):
    api_keys = load_api_keys()
    for api_key in api_keys:
        # API ile tarif aramasını dene
        details = get_multi_recipe_details_from_api(api_key, recipe_ids)
        if details is not None:
            return details

    return None


# Malzemelere göre tarif arar
def get_recipe_from_api(api_key, ingredients):
    ingredients_en = dl.translate(ingredients, 'TR', 'EN-US')
    search_url = f"{base_url}findByIngredients"
    params = {
        "ingredients": ingredients_en,
        "number": recipe_count,
        "apiKey": api_key
    }
    response = requests.get(search_url, params=params)

    # Kota bittiğinde kontrol
    if response.status_code == 402:
        return None
    return response.json()


# Rastgele bir tarif arar
def find_random_recipe_from_api(api_key, include_tags, exclude_tags):
    random_url = f"{base_url}random"
    params = {
        "includeNutrition": True,
        "include-tags": include_tags,
        "exclude-tags": exclude_tags,
        "number": recipe_count,
        "apiKey": api_key
    }
    response = requests.get(random_url, params=params)

    if response.status_code == 402:
        return None
    return response.json()['recipes']


# ID si gelen tarifin detaylarını getirir
def get_recipe_details_from_api(api_key, recipe_id):
    details_url = f"{base_url}{recipe_id}/information"
    response = requests.get(details_url, params={"apiKey": api_key})

    if response.status_code == 402:
        return None
    return response.json()


# ID si gelen tarifin detaylarını getirir
def get_multi_recipe_details_from_api(api_key, recipe_ids):
    details_url = f"{base_url}informationBulk"
    params = {
        "ids": recipe_ids,
        "apiKey": api_key
    }
    response = requests.get(details_url, params=params)

    if response.status_code == 402:
        return None
    return response.json()


# Bulanan tarifleri konsola yazdırır (main.py için)
def print_recipe_id(recipes):
    print("\nBulunan Tarifler:")
    for idx, recipe in enumerate(recipes, 1):
        title_tr = dl.translate(recipe['title'], 'EN', 'TR')
        print(f"{idx}. {title_tr} (ID: {recipe['id']})")
        image_url = recipe.get('image', 'No image available')
        print(f"Image: {image_url}")


# Tarifin detaylarını konsola yazdırır (main.py için)
def print_recipe_details(recipe_details):
    # Tarifin malzemeleri ve adımları
    title_tr = dl.translate(recipe_details['title'], 'EN', 'TR')
    print(f"\nTarif Adı: {title_tr}")
    print("Malzemeler:")
    for ingredient in recipe_details['extendedIngredients']:
        ingredient_tr = dl.translate(ingredient['original'], 'EN', 'TR')
        print(f"- {ingredient_tr}")

    print("\nAdımlar:")
    instructions = recipe_details.get('instructions', 'Adımlar bulunamadı.')
    soup = BeautifulSoup(instructions, "html.parser")
    instructions_text = soup.get_text(separator="\n")  # Her bir maddeyi yeni satırda yazdırır
    instructions_tr = dl.translate(instructions_text, 'EN', 'TR')
    print(instructions_tr)


# API keyleri dosyadan okur
def load_api_keys(filename="SPOONACULAR_API_KEYS.txt"):
    with open(filename, 'r') as file:
        api_keys = [line.strip() for line in file.readlines()]
    return api_keys

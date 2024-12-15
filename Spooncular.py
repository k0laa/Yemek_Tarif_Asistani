import requests
import DeepL as dl
from bs4 import BeautifulSoup

api_key = "83b2b1202ace49ebb26496ac998fedb4"  ##günlük kota 150
base_url = "https://api.spoonacular.com/recipes/"


def find_recipe(ingredients):
    ingredients_en = dl.translate(ingredients, 'TR', 'EN-US')
    # API'ye tarif bulma isteği gönder
    search_url = f"{base_url}findByIngredients"  #
    params = {
        "ingredients": ingredients_en,
        "number": 5,  # Gösterilecek tarif sayısı
        "apiKey": api_key
    }
    response = requests.get(search_url, params=params)
    recipes = response.json()
    return recipes


def print_recipe_id(recipes):
    print("\nBulunan Tarifler:")
    for idx, recipe in enumerate(recipes, 1):
        title_tr = dl.translate(recipe['title'], 'EN', 'TR')
        print(f"{idx}. {title_tr} (ID: {recipe['id']})")


def get_recipe_details(recipe_id):
    details_url = f"{base_url}{recipe_id}/information"
    response = requests.get(details_url, params={"apiKey": api_key})
    recipe_details = response.json()
    return recipe_details


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

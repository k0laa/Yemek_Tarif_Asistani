from bs4 import BeautifulSoup
from flask import Flask, render_template, request
import Spoonacular as sp
import DeepL as dl

finded_recipes_details = []
ingredients = ''

app = Flask(__name__)


# Tarif arama sayfası
@app.route('/')
def index():
    return render_template('index.html')


# Tarif arama sonuçları sayfası
@app.route('/find_recipe', methods=['POST'])
def find_recipe():
    global finded_recipes_details, ingredients

    ingredients_form = request.form['ingredients']  # Formdan gelen malzemeleri alır

    if ingredients_form != ingredients:  # sayfa yenilendiğinde aynı malzemeleri tekrar aramamak için
        finded_recipes_details.clear()
        ingredients = ingredients_form
        recipes = sp.find_recipe(ingredients)  # Malzemelere göre tarif arar
        for recipe in recipes:  #
            details = sp.get_recipe_details(recipe['id'])  # Tarif detaylarını getirir
            details['title'] = dl.translate(details['title'], 'EN', 'TR')  # Detaylardaki başlığı çevirir
            finded_recipes_details.append(details)

    return render_template('recipes.html', recipes=finded_recipes_details)


# Tarif detayları sayfası
@app.route('/recipe_details/<int:recipe_id>')
def recipe_details(recipe_id):
    recipe_id = int(recipe_id)
    global finded_recipes_details
    recipe_details = None

    # İlgili tarifin detaylarını bul
    for recipe in finded_recipes_details:
        if recipe['id'] == recipe_id:
            recipe_details = recipe
            break

    if recipe_details is None:
        return "Tarif bulunamadı", 404

    # Malzeme açıklamalarını çevir
    for ingredient in recipe_details.get('extendedIngredients', []):
        ingredient['original'] = dl.translate(ingredient['original'], 'EN', 'TR')

    # Tarif adımlarını çevir
    if 'instructions' in recipe_details and recipe_details['instructions']:
        soup = BeautifulSoup(recipe_details['instructions'], "html.parser")
        instructions_text = soup.get_text(separator="\n")
        recipe_details['instructions'] = dl.translate(instructions_text, 'EN', 'TR')

    return render_template('recipe_details.html', recipe_details=recipe_details)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

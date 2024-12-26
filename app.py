from bs4 import BeautifulSoup
from flask import Flask, render_template, request
import Spoonacular as sp
import DeepL as dl

finded_recipes_details, translated_recipes = [], []
ingredients = ''

app = Flask(__name__)


# Tarif arama sayfası
@app.route('/')
def index():
    return render_template('index.html')


# Rastgele tarif arama sayfası
@app.route('/random_recipe')
def random_recipe():
    return render_template('random_recipe.html')


# Tarif arama sonuçları sayfası
@app.route('/find_recipe', methods=['POST'])
def find_recipe():
    global finded_recipes_details, ingredients

    ingredients_form = request.form['ingredients']  # Formdan gelen malzemeleri alır

    if ingredients_form != ingredients:  # sayfa yenilendiğinde aynı malzemeleri tekrar aramamak için kontrol
        finded_recipes_details.clear()
        ingredients = ingredients_form

        recipes = sp.find_recipe(ingredients)  # Malzemelere göre tarif arar
        recipe_ids = ', '.join(str(recipe['id']) for recipe in recipes)  # Tariflerin ID'lerini alır
        recipes_details = sp.get_multi_recipe_details(recipe_ids)  # ID si gelen tariflerin detaylarını getirir

        for details in recipes_details:
            details['title'] = dl.translate(details['title'], 'EN', 'TR')  # Detaylardaki başlığı çevirir

            soup = BeautifulSoup(details['summary'], "html.parser")
            summary_text = soup.get_text(separator="\n")
            details['summary'] = dl.translate(summary_text, 'EN', 'TR')

            finded_recipes_details.append(details)

    return render_template('recipes.html', recipes=finded_recipes_details)


# Rastgele tarif sonuçları sayfası
@app.route('/find_random_recipe', methods=['POST'])
def find_random_recipe():
    global finded_recipes_details, ingredients
    finded_recipes_details.clear()
    ingredients = ''

    print(request.form)
    include_tags = [request.form['include_tags']]
    exclude_tags = [request.form['exclude_tags']]
    print(include_tags)
    print(exclude_tags)
    recipes = sp.find_random_recipe(include_tags, exclude_tags)  # Rastgele bir tarif arar
    print(recipes)
    recipe_ids = ', '.join(str(recipe['id']) for recipe in recipes)  # Tariflerin ID'lerini alır
    recipes_details = sp.get_multi_recipe_details(recipe_ids)  # ID si gelen tariflerin detaylarını getirir

    for details in recipes_details:
        details['title'] = dl.translate(details['title'], 'EN', 'TR')

        soup = BeautifulSoup(details['summary'], "html.parser")
        summary_text = soup.get_text(separator="\n")
        details['summary'] = dl.translate(summary_text, 'EN', 'TR')

        finded_recipes_details.append(details)

    return render_template('recipes.html', recipes=finded_recipes_details)


# Tarif detayları sayfası
@app.route('/recipe_details/<int:recipe_id>')
def recipe_details(recipe_id):
    recipe_id = int(recipe_id)
    global finded_recipes_details, translated_recipes
    recipe_details = None
    translated = False

    # İlgili tarifin detaylarını bul
    for recipe in finded_recipes_details:
        if recipe['id'] == recipe_id:
            recipe_details = recipe.copy()
            break

    # İlgili tarifin çevirilmiş detaylarını bul
    for recipe in translated_recipes:
        if recipe['id'] == recipe_id:
            recipe_details = recipe.copy()
            translated = True
            break

    if recipe_details is None:
        return "Tarif bulunamadı", 404

    # Tarif daha önce çevrildiyse tekrar çevirme
    if translated:
        return render_template('recipe_details.html', recipe_details=recipe_details)

    # Malzeme açıklamalarını çevir
    for ingredient in recipe_details.get('extendedIngredients', []):
        ingredient['original'] = dl.translate(ingredient['original'], 'EN', 'TR')

    # Tarif adımlarını çevir
    if 'instructions' in recipe_details and recipe_details['instructions']:
        soup = BeautifulSoup(recipe_details['instructions'], "html.parser")
        instructions_text = soup.get_text(separator="\n")
        recipe_details['instructions'] = dl.translate(instructions_text, 'EN', 'TR')

    # Tarif adımlarını çevir
    analyzed_instructions = sp.get_analyzed_recipe_instructions(recipe_details['id'])

    analyzed_instructions[0]['name'] = dl.translate(analyzed_instructions[0]['name'], 'EN', 'TR')
    for instruction in analyzed_instructions[0]['steps']:
        instruction['step'] = dl.translate(instruction['step'], 'EN', 'TR')
        for equipment in instruction['equipment']:
            equipment['name'] = dl.translate(equipment['name'], 'EN', 'TR')
        for ingredient in instruction['ingredients']:
            ingredient['name'] = dl.translate(ingredient['name'], 'EN', 'TR')

    recipe_details["analyzedInstructions"] = analyzed_instructions

    # Tarifin daha önce çevrildiğini belirt
    translated_recipes.append(recipe_details)
    return render_template('recipe_details.html', recipe_details=recipe_details)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

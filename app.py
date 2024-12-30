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
    print(ingredients_form)

    if ingredients_form != ingredients:  # sayfa yenilendiğinde aynı malzemeleri tekrar aramamak için kontrol
        finded_recipes_details.clear()
        ingredients = ingredients_form

        recipes = sp.find_recipe(ingredients)  # Malzemelere göre tarif arar
        recipe_ids = ', '.join(str(recipe['id']) for recipe in recipes)  # Tariflerin ID'lerini alır
        recipes_details = sp.get_multi_recipe_details(recipe_ids)  # ID si gelen tariflerin detaylarını getirir

        # Tarif detaylarını çevir ve listeye ekle
        for details in recipes_details:
            details = dl.translate_recipe_details(details)
            finded_recipes_details.append(details)

    return render_template('recipes.html', recipes=finded_recipes_details)


# Rastgele tarif sonuçları sayfası
@app.route('/find_random_recipe', methods=['POST'])
def find_random_recipe():
    global finded_recipes_details, ingredients
    finded_recipes_details.clear();
    ingredients = ''

    include_tags = [request.form['include_tags']]
    exclude_tags = [request.form['exclude_tags']]
    recipes = sp.find_random_recipe(include_tags, exclude_tags)  # Rastgele bir tarif arar
    recipe_ids = ', '.join(str(recipe['id']) for recipe in recipes)  # Tariflerin ID'lerini alır
    recipes_details = sp.get_multi_recipe_details(recipe_ids)  # ID si gelen tariflerin detaylarını getirir

    # Tarif detaylarını çevir ve listeye ekle
    for details in recipes_details:
        details = dl.translate_recipe_details(details)
        finded_recipes_details.append(details)

    return render_template('recipes.html', recipes=finded_recipes_details)


# Tarif detayları sayfası
@app.route('/recipe_details/<int:recipe_id>')
def recipe_details(recipe_id):
    global finded_recipes_details, translated_recipes

    recipe_details = None
    translated = False
    recipe_id = int(recipe_id)

    # Tarif daha önce çevrildiyse çevrilen tarifi getir
    for recipe in translated_recipes:
        if recipe['id'] == recipe_id:
            recipe_details = recipe.copy()
            translated = True
            break

    if translated:
        return render_template('recipe_details.html', recipe_details=recipe_details)

    # Tarif daha önce çevrilmemişse çevir
    for recipe in finded_recipes_details:
        if recipe['id'] == recipe_id:
            recipe_details = recipe.copy()
            break

    if recipe_details is None:
        return "Tarif bulunamadı", 404

    # Tarif detaylarını çevir
    recipe_details = dl.translate_recipe_instructions(recipe_details)

    # Tarif adımlarını getir ve çevir
    analyzed_instructions = sp.get_analyzed_recipe_instructions(recipe_details['id'])
    analyzed_instructions = dl.translate_analyzed_instructions(analyzed_instructions)

    # çeviriyi tarife ekle
    recipe_details["analyzedInstructions"] = analyzed_instructions

    # Tarifin daha önce çevrildiğini belirt
    translated_recipes.append(recipe_details)
    return render_template('recipe_details.html', recipe_details=recipe_details)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

from bs4 import BeautifulSoup
from flask import Flask, render_template, request
import Spoonacular as sp
import DeepL as dl

app = Flask(__name__)


# tarif arama sayfası
@app.route('/')
def index():
    return render_template('index.html')


# tarif arama sonuçları sayfası
@app.route('/find_recipe', methods=['POST'])
def find_recipe():
    ingredients = request.form['ingredients']  # formdan gelen malzemeleri alır
    recipes = sp.find_recipe(ingredients)  # malzemelere göre tarif arar
    for recipe in recipes:
        recipe['title'] = dl.translate(recipe['title'], 'EN', 'TR')  # tarif adını çevirir

    return render_template('recipes.html', recipes=recipes)


# tarif detayları sayfası
@app.route('/recipe_details/<int:recipe_id>')
def recipe_details(recipe_id):
    # tarif detaylarını getirir
    recipe_detail = sp.get_recipe_details(recipe_id)

    # tarif detaylarını çevirir
    for ingredient in recipe_detail['extendedIngredients']:
        ingredient['original'] = dl.translate(ingredient['original'], 'EN', 'TR')
    recipe_detail['title'] = dl.translate(recipe_detail['title'], 'EN', 'TR')

    # tarif adımlarını çevirir
    soup = BeautifulSoup(recipe_detail['instructions'], "html.parser")
    instructions_text = soup.get_text(separator="\n")  # Her bir maddeyi yeni satırda yazdırır
    recipe_detail['instructions'] = dl.translate(instructions_text, 'EN', 'TR')

    return render_template('recipe_details.html', recipe_detail=recipe_detail)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

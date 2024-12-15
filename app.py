from flask import Flask, render_template, request
import Spoonacular as sp
import DeepL as dl

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/find_recipe', methods=['POST'])
def find_recipe():
    ingredients = request.form['ingredients']
    recipes = sp.find_recipe(ingredients)
    for recipe in recipes:
        recipe['title'] = dl.translate(recipe['title'], 'EN', 'TR')

    return render_template('recipes.html', recipes=recipes)

@app.route('/recipe_details/<int:recipe_id>')
def recipe_details(recipe_id):
    recipe_details = sp.get_recipe_details(recipe_id)
    for ingredient in recipe_details['extendedIngredients']:
        ingredient['original'] = dl.translate(ingredient['original'], 'EN', 'TR')
    recipe_details['instructions'] = dl.translate(recipe_details['instructions'], 'EN', 'TR')
    recipe_details['title'] = dl.translate(recipe_details['title'], 'EN', 'TR')
    return render_template('recipe_details.html', recipe_details=recipe_details)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
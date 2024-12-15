import Spoonacular as sp

if __name__ == "__main__":
    ingredients = input("Hangi malzemelere sahipsiniz? (Virgülle ayırın): ")

    recipes = sp.find_recipe(ingredients)
    sp.print_recipe_id(recipes) if recipes else print("Bu malzemelerle tarif bulunamadı.")

    recipe_id = input("\nDetaylarını görmek istediğiniz tarifin ID'sini girin: ")

    if recipe_id:
        recipe_details = sp.get_recipe_details(recipe_id)
        sp.print_recipe_details(recipe_details) if recipe_details else print("Bu ID'ye ait tarif bulunamadı.")

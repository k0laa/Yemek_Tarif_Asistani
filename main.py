import Spoonacular as sp
import DeepL as dl

finded_recipes_details, translated_recipes = [], []
ingredients = ''


# Kullanıcıdan malzemeleri alarak tarif arar ve listeler
def list_recipes():
    global finded_recipes_details, ingredients

    print("\nÖrneğin: 'yumurta, un, süt'")
    ingredients_form = input("Malzemeleri bir virgül ve boşluk ile ayırarak girin: ")

    if ingredients_form != ingredients:  # Aynı malzemeleri tekrar aramamak için kontrol
        finded_recipes_details.clear()
        ingredients = ingredients_form

        recipes = sp.find_recipe(ingredients)  # Malzemelere göre tarif arar
        recipe_ids = ', '.join(str(recipe['id']) for recipe in recipes)  # Tariflerin ID'lerini alır
        recipes_details = sp.get_multi_recipe_details(recipe_ids)  # ID'ye göre tariflerin detaylarını getirir

        # Tarif detaylarını çevir ve listeye ekle
        for details in recipes_details:
            details = dl.translate_recipe_details(details, 'EN', 'TR')
            finded_recipes_details.append(details)

    sp.print_recipe_id(finded_recipes_details)


# Kullanıcıdan etiketleri alarak rastgele tarif arar ve listeler.
def random_recipe():
    global finded_recipes_details, ingredients
    finded_recipes_details.clear()
    ingredients = ''

    include_tags = []  # input("Dahil edilmesini istediğiniz etiketler (virgülle ayırın): ").split(',')
    exclude_tags = []  # input("Hariç tutulmasını istediğiniz etiketler (virgülle ayırın): ").split(',')

    recipes = sp.find_random_recipe(include_tags, exclude_tags)  # Rastgele bir tarif arar
    recipe_ids = ', '.join(str(recipe['id']) for recipe in recipes)  # Tariflerin ID'lerini alır
    recipes_details = sp.get_multi_recipe_details(recipe_ids)  # ID'ye göre tariflerin detaylarını getirir

    # Tarif detaylarını çevir ve listeye ekle
    for details in recipes_details:
        details = dl.translate_recipe_details(details, 'EN', 'TR')
        finded_recipes_details.append(details)

    sp.print_recipe_id(finded_recipes_details)


# Kullanıcıdan bir tarif numarası alarak tarif detaylarını gösterir.
def show_recipe_details():
    global finded_recipes_details, translated_recipes

    try:
        recipe_id = int(input("\nDetaylarını görmek istediğiniz tarifin numarasını girin: "))
        for finded_recipe in finded_recipes_details:
            if finded_recipe['id'] == recipe_id:
                recipe = finded_recipe
                break

        # Tarif daha önce çevrildiyse çeviriyi kullan
        for translated_recipe in translated_recipes:
            if translated_recipe['id'] == recipe['id']:
                recipe = translated_recipe
                break
        else:
            # Tarif daha önce çevrilmemişse çevir
            recipe = dl.translate_recipe_instructions(recipe, 'EN', 'TR')
            analyzed_instructions = sp.get_analyzed_recipe_instructions(recipe['id'])
            analyzed_instructions = dl.translate_analyzed_instructions(analyzed_instructions, 'EN', 'TR')
            recipe['analyzedInstructions'] = analyzed_instructions
            translated_recipes.append(recipe)

        print(f"\nTarif Adı: {recipe['title']}")
        print(f"\nMalzemeler:")
        for ingredient in recipe['extendedIngredients']:
            print(f"- {ingredient['original']}")
        print("\nTalimatlar:")
        for instruction in recipe['analyzedInstructions']:
            for step in instruction['steps']:
                print(f"{step['number']}. {step['step']}")
    except ValueError:
        print("Geçerli bir sayı girin.")


def main():
    # Kullanıcı menüsü
    while True:
        print("\nYemek Tarif Asistanı")
        print("1. Tarif Ara")
        print("2. Rastgele Tarif Bul")
        print("3. Tarif Detaylarını Göster")
        print("4. Çıkış")

        choice = input("Seçiminizi yapın: ")

        if choice == '1':
            list_recipes()
        elif choice == '2':
            random_recipe()
        elif choice == '3':
            show_recipe_details()
        elif choice == '4':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")


if __name__ == '__main__':
    main()

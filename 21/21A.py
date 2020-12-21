all_ingredients = []

allergens_dict = dict()
for line in open('input.txt', 'r').readlines():
    line = line.rstrip().replace(")", "")
    (ingredients, allergens) = line.split(" (contains ")
    ingredients = ingredients.split(" ")
    all_ingredients += ingredients
    ingredients = set(ingredients)
    allergens = allergens.split(", ")
    for allergen in allergens:
        if allergen not in allergens_dict:
            allergens_dict[allergen] = ingredients
        else:
            allergens_dict[allergen] = allergens_dict[allergen].intersection(ingredients)
for allergen in allergens_dict:
    print("%s -> %s" % (allergen, allergens_dict[allergen]))
ingredients_with_allergens = []
for ingrs in allergens_dict.values():
    ingredients_with_allergens += ingrs
print("Answer: " + str(len(list(filter(lambda ing: ing not in ingredients_with_allergens, all_ingredients)))))
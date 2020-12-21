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

while len(list(filter(lambda ingrs: len(ingrs) > 1, allergens_dict.values()))) > 0:
    determined_ingrs = filter(lambda ingrs: len(ingrs) == 1, allergens_dict.values())
    determined_ingrs = list(map(lambda ingrs: next(iter(ingrs)), determined_ingrs))
    undeterminded_allergens = list(filter(lambda a: len(allergens_dict[a]) > 1, allergens_dict))
    for ingr in determined_ingrs:
        for ua in undeterminded_allergens:
            ingrs = allergens_dict[ua]
            if ingr in ingrs:
                ingrs.remove(ingr)
                allergens_dict[ua] = ingrs
for allergen in allergens_dict:
    print("%s -> %s" % (allergen, allergens_dict[allergen]))
allergens = list(allergens_dict.keys())
allergens.sort()
canonical_dangerous_ingredients = ",".join(list(map(lambda a: list(allergens_dict[a])[0], allergens)))
print("Canonical dangerous ingredients: " + canonical_dangerous_ingredients)
spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    names = []

    for food in spicy_foods:
        names.append(food['name'])
    return names



def get_spiciest_foods(spicy_foods):
    spicy_foods_list = []

    for food in spicy_foods:
        if food['heat_level'] > 5:
            spicy_foods_list.append(food)
    return spicy_foods_list


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food['name']
        cuisine = food['cuisine']
        heat_level = food['heat_level']

        formatted_food = f"{name} ({cuisine}) | Heat Level: {'🌶' * heat_level}"

        print(formatted_food)




def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    found_food = None

    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            found_food = food
            break

    return found_food




def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food['heat_level'] > 5:
            name = food['name']
            cuisine = food['cuisine']
            heat_level = '🌶' * food['heat_level']

            formatted_food = f"{name} ({cuisine}) | Heat Level: {heat_level}"

            print(formatted_food)



def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0  

    total_heat_level = 0
    count = 0

    for food in spicy_foods:
        total_heat_level += food['heat_level']
        count += 1

    average_heat_level = total_heat_level / count

    return average_heat_level

def create_spicy_food(spicy_foods, spicy_food):
    new_spicy_foods = spicy_foods.copy()

    new_spicy_foods.append(spicy_food)

    return new_spicy_foods
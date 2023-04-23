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
    spicy_names = []
    for food in spicy_foods:
        spicy_names.append(food['name'])
    return spicy_names


def get_spiciest_foods(spicy_foods):
    highest_spices = [food for food in spicy_foods if food["heat_level"] > 5]
    return highest_spices


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        peppers = '🌶' * int(food['heat_level'])
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {peppers}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            peppers = '🌶' * int(food['heat_level'])
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {peppers}")

def get_average_heat_level(spicy_foods):
    total_spice = 0
    for food in spicy_foods:
        total_spice = total_spice + food["heat_level"]
    return total_spice / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

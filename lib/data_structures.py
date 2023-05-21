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
   for food in spicy_foods:
    print(food["name"])
get_names(spicy_foods)   

def get_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        result = food["heat_level"] > 5
        if result:
            print(food)
get_spiciest_foods(spicy_foods)            

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        foodName = food["name"]
        foodCuisine = food["cuisine"]
        foodHeatLevel = "Heat Level: " + food["heat_level"]*"🌶"
        print(foodName,"(", foodCuisine,") |", foodHeatLevel)
print_spicy_foods()

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            print(food)
get_spicy_food_by_cuisine(spicy_foods, "American")
get_spicy_food_by_cuisine(spicy_foods, "Thai")     

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        spiciestFood = food["heat_level"] > 5
        if spiciestFood:
            print_spicy_foods(food)
print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    theSum = 0
    for food in spicy_foods:
        theSum = theSum + food["heat_level"]
    print(theSum // len(spicy_foods))   
get_average_heat_level(spicy_foods)    

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    print(spicy_foods)
create_spicy_food(spicy_foods, {"name": "Chapati","cuisine": "KFC", "heat_level": 1,},)   

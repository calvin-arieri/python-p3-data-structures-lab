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
   namesOfFood = []
   for food in spicy_foods:
    food_list = food["name"]
    namesOfFood.append(food_list)
   return namesOfFood 
get_names(spicy_foods)   

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]
get_spiciest_foods(spicy_foods)            

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        foodName = food["name"]
        foodCuisine = food["cuisine"]
        foodHeatLevel = "Heat Level: " + food["heat_level"]*"🌶"
        print (f"{foodName} ({foodCuisine}) | {foodHeatLevel}")
print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
get_spicy_food_by_cuisine(spicy_foods, "American")
get_spicy_food_by_cuisine(spicy_foods, "Thai")     

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        spiciestFood = food["heat_level"] > 5
        if spiciestFood:
            foodName = food["name"]
            foodCuisine = food["cuisine"]
            foodHeatLevel = "Heat Level: " + food["heat_level"]*"🌶"
            print (f"{foodName} ({foodCuisine}) | {foodHeatLevel}")
print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    theSum = 0
    for food in spicy_foods:
        theSum = theSum + food["heat_level"]
    return theSum // len(spicy_foods)  
get_average_heat_level(spicy_foods)    

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
create_spicy_food(spicy_foods, {"name": "Griot","cuisine": "Hatian", "heat_level": 10,},)   

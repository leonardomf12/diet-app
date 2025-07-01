from statistics import quantiles

import IPython
from pathlib import Path
import json

from urllib3.util.wait import select_wait_for_socket


class Food:
    def __init__(self, food : dict, mult = 1):
        self.food = food
        self.mult = mult
        # Names
        self.name = f'{self.food["Name"]} - {self.food["Brand"]}'

        # Units
        self.units = list(self.food["units"].keys())
        #self.main_unit = food["units"][0] # TODO Define a way to handle main units

        # MacroNutrients
        #self.base


    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Food(self.food, self.mult * other)
        return None

    def __add__(self, other):
        if isinstance(other, Food):
            return Meal([self, other])

        elif isinstance(other, Meal):
            return Meal([self] + other.food_list)
        return NotImplemented

    # def __getitem__(self, key):
    #     if key == "name":
    #         return self.name
    #     elif key == "units":
    #         return self.units
    #     return None

    def get(self, mult = 1):
        return {"Name": self.name,
                "Multiplier": mult,
                "Units": self.units[0],
                "Calories": self.food["units"][self.units[0]]["kcals"] * mult,
                "Protein": self.food["units"][self.units[0]]["protein"]* mult,
                "CarbHid": self.food["units"][self.units[0]]["carbhid"]* mult,
                "Fat": self.food["units"][self.units[0]]["fat"]* mult,
                }

class Meal:
    def __init__(self, food : list[Food], name = None):
        assert all(isinstance(f, Food) for f in food)
        self.name = name
        self.food_list = food

    def __add__(self, other):
        if isinstance(other, Food):
            return Meal(self.food_list + [other])

        elif isinstance(other, Meal):
            return Meal(self.food_list + other.food_list)
        return NotImplemented

    def get(self):

        meal_info = {"Ingredients": [],
                     "Quantities": [],
                     "Calories": 0,
                     "Protein": 0,
                     "CarbHid": 0,
                     "Fat": 0}

        for f in self.food_list:
            f_info = f.get()
            meal_info["Ingredients"].append(f_info["Name"])
            meal_info["Quantities"].append(f_info["Multiplier"])

            meal_info["Calories"] += f_info["Calories"]
            meal_info["Protein"] += f_info["Protein"]
            meal_info["CarbHid"] += f_info["CarbHid"]
            meal_info["Fat"] += f_info["Fat"]

        if self.name is not None:
            meal_info["Name"] = self.name
        else:
            meal_info["Name"] = "-".join(meal_info["Ingredients"])
        return meal_info




def load_food_db(root = "src/db/food_db.json"):
    with open(root, 'r') as f:
        food_db = json.load(f)

    food_list = []
    for food in food_db:
        food_list.append(Food(food))
    return food_list

if __name__ == '__main__':
    import json

    # Load JSON data from file
    with open('db/food_db.json', 'r') as file:
        food_db = json.load(file)

    pao = Food(food_db[0])
    Meal([pao, pao]).get()
class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }
    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
    def is_resource_sufficient(self, drink):
        for ingredient, amount_needed in drink.ingredients.items():

         if self.resources.get(ingredient, 0) < amount_needed:
            print(f"Sorry there is not enough {ingredient}.")
            return False

        return True
    def make_coffee(self, order):
        for ingredient, amount_needed in order.ingredients.items():
            self.resources[ingredient] -= amount_needed
  
        print(f"Here is your {order.name} ☕")
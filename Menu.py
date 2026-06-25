from MenuItem import MenuItem
class Menu:
    def __init__(self):
        self.menu=[MenuItem(
                "espresso",
                1.5,
                {
                    "water": 50,
                    "coffee": 18
                }
            ),
            MenuItem(
                "latte",
                2.5,
                {
                    "water": 200,
                    "milk": 150,
                    "coffee": 24
                }
            ),
            MenuItem(
                "cappuccino",
                3.0,
                {
                    "water": 250,
                    "milk": 100,
                    "coffee": 24
                }
            )]
    def get_items(self):
        return "/".join(item.name for item in self.menu)
    def find_drink(self,order_name):
        for item in self.menu:
            if order_name==item.name:
               return item
        return None
        
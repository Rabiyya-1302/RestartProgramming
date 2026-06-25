class MenuItem:
    def __init__(self,name,cost,ingredients):
        self.name=name
        self.cost=cost
        self.ingredients=ingredients
class Menu(MenuItem):
    def __init__(self):
     self.menu=[]
    def get_items(self):
        names=[]
        for item in self.menu:
            names.append(item.name)
        return "/".join(names)
            
    def find_drink(self,order_name):
        for item in self.menu:
            if item.name==order_name:
                return item
        return None
class CoffeeMaker(Menu):
    def __init__(self,resources):
        self.resources={
            "Water":300,
            "Milk":200,
            "Coffee":100
        }
    def report(self):
        print(f"Water:{self.resources["water"]}")
        print(f"Milk:{self.resources["milk"]}ml")
        print(f"Coffee:{self.resources["coffee"]}ml")
    def is_resource_sufficient(self,drink):
        for ingredient in drink.ingredients:
            if self.resources[ingredient]>drink.ingredients[ingredient]:
                print("Sorry not enough resources available")
                return False
        return True
    def make_coffee(self,order):
        for ingredient in order.ingredients:
            self.resources["ingredient"]-=order.ingredients[ingredient]
        print(f"Here is your {order.name}")
            
    class MoneyMachine:
        def __init__(self):
            self.profit=0
        def make_payment(self, cost):
          amount_received = float(input("Insert money: $"))

          if amount_received < cost:
              print("Sorry that's not enough money. Money refunded.")
              return False

          change = amount_received - cost

          if change > 0:
            print(f"Here is ${change:.2f} in change.")

          self.profit += cost
          return True
                 
            
            
            
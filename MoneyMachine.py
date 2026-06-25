class MoneyMachine:
    def __init__(self):
        self.profit = 0
    def report(self):
       print(f"Money: ${self.profit}")
    def make_payment(self, cost):

       amount_received = float(
        input("Insert money: $")
    )

       if amount_received < cost:
        print("Sorry that's not enough money.")
        return False

       change = amount_received - cost

       if change > 0:
        print(f"Here is ${change:.2f} in change.")

       self.profit += cost

       return True
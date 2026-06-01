bid_dict = []

print("Lets Start the Bid")

def user_data():
    name = input("What is your name: ")
    bid = int(input("What is your bid:$"))
    return name, bid

def creating_list(bid_dict, name, bid):
    bid_dict.append({"name": name, "bid": bid})

# first user
name, bid = user_data()
creating_list(bid_dict, name, bid)

another_person = input("Is there any other person in the room (yes,no): ")

while another_person != "no":
    print("\n" * 50)

    name, bid = user_data()
    creating_list(bid_dict, name, bid)

    another_person = input("Is there any other person in the room (yes,no): ")
def highest_bidder(bid_dict):
    max_bid=0
    winner=""
    for bidder in bid_dict:
        if bidder["bid"]>max_bid:
            max_bid=bidder["bid"]
            winner=bidder["name"]
    print(f"Highest bidder is {bidder['name']}")
print(bid_dict)
highest_bidder(bid_dict)

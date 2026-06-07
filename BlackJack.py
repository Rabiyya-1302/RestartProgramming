import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw_card():
    return random.choice(cards)


def calculate_score(hand):
    score = sum(hand)

    while score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)

    return score


def check_blackjack(player_score, dealer_score):
    if player_score == 21 and dealer_score == 21:
        print("Draw!")
        return True

    elif player_score == 21:
        print("Blackjack! You win!")
        return True

    elif dealer_score == 21:
        print("Dealer has Blackjack. You lose!")
        return True

    return False


def player_turn(player):
    while True:
        score = calculate_score(player)

        if score > 21:
            print(f"Your cards: {player}")
            print("Busted! Dealer wins.")
            return False

        move = input("Hit or Stand? ").lower()

        if move == "hit":
            card = draw_card()
            player.append(card)

            print(f"You drew: {card}")
            print(f"Your cards: {player}")
            print(f"Your score: {calculate_score(player)}")

        elif move == "stand":
            return True


def dealer_turn(dealer):
    print(f"\nDealer reveals hand: {dealer}")

    while calculate_score(dealer) < 17:
        card = draw_card()
        dealer.append(card)

        print(f"Dealer drew: {card}")

    return calculate_score(dealer)


def determine_winner(player_score, dealer_score):
    print(f"\nFinal Player Score: {player_score}")
    print(f"Final Dealer Score: {dealer_score}")

    if dealer_score > 21:
        print("Dealer busted! You win!")

    elif player_score > dealer_score:
        print("Congratulations! You win!")

    elif player_score < dealer_score:
        print("Dealer wins!")

    else:
        print("It's a draw!")


def main():
    player = []
    dealer = []

    for _ in range(2):
        player.append(draw_card())
        dealer.append(draw_card())

    player_score = calculate_score(player)
    dealer_score = calculate_score(dealer)

    print(f"Your cards: {player}")
    print(f"Dealer's first card: {dealer[0]}")

    if check_blackjack(player_score, dealer_score):
        return

    if not player_turn(player):
        return

    dealer_score = dealer_turn(dealer)

    player_score = calculate_score(player)

    print(f"\nFinal Player Hand: {player}")
    print(f"Final Dealer Hand: {dealer}")

    determine_winner(player_score, dealer_score)


start = input("Let's start game (Y/N): ").upper()

if start == "Y":
    main()
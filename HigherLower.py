import random

movies = [
    {
        "title": "Titanic",
        "description": "Titanic is a romantic disaster film directed by James Cameron.",
        "searches": 1200000
    },
    {
        "title": "Avatar",
        "description": "Avatar is an epic science-fiction film directed by James Cameron.",
        "searches": 1800000
    },
    {
        "title": "The Dark Knight",
        "description": "The Dark Knight is a superhero film directed by Christopher Nolan.",
        "searches": 950000
    },
    {
        "title": "Jurassic Park",
        "description": "Jurassic Park is a science-fiction adventure film directed by Steven Spielberg.",
        "searches": 450000
    },
    {
        "title": "Pulp Fiction",
        "description": "Pulp Fiction is a crime film directed by Quentin Tarantino.",
        "searches": 650000
    },
    {
        "title": "The Godfather",
        "description": "The Godfather is a crime drama film directed by Francis Ford Coppola.",
        "searches": 800000
    },
    {
        "title": "Parasite",
        "description": "Parasite is a dark comedy thriller directed by Bong Joon-ho.",
        "searches": 550000
    },
    {
        "title": "Spirited Away",
        "description": "Spirited Away is an animated fantasy film directed by Hayao Miyazaki.",
        "searches": 400000
    },
    {
        "title": "Mad Max: Fury Road",
        "description": "Mad Max: Fury Road is an action film directed by George Miller.",
        "searches": 350000
    },
    {
        "title": "The Grand Budapest Hotel",
        "description": "The Grand Budapest Hotel is a comedy-drama film directed by Wes Anderson.",
        "searches": 250000
    }
]


def play_game():
    score = 0

    print("Welcome to Higher/Lower Guessing Game")

    while True:
        A, B = random.sample(movies, 2)

        print(f"\nA: {A['description']}")
        print("VS")
        print(f"B: {B['description']}")

        while True:
            user_guess = input(
                "Which option has more Google searches? (A/B): "
            ).lower()

            if user_guess in ["a", "b"]:
                break

            print("Please enter A or B only.")

        if A["searches"] > B["searches"]:
            correct_answer = "a"
        else:
            correct_answer = "b"

        if user_guess == correct_answer:
            score += 1
            print(f"Correct! Current score: {score}")
        else:
            print(f"Wrong! Final score: {score}")
            return score


while True:
    final_score = play_game()

    choice = input("\nReplay? (Y/N): ").lower()

    if choice != "y":
        print("Thanks for playing!")
        break
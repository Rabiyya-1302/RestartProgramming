import random
def play_game(attempts):
    num_to_be_guessed=random.randint(1,100)
    remaining_attempts=attempts

    while remaining_attempts>0:
            try:
             guess=int(input("Enter your guess:"))
            except ValueError:
                  print("Enter a number!!Wrong Format") 
                  continue
            remaining_attempts=-1
            if guess==num_to_be_guessed:
                print("CONGRATULATIONS!CORRECT GUESS")
                return
            elif guess>num_to_be_guessed:
                print(f"Too High.Remaining attempts:{remaining_attempts}")
            else:
                print(f"Too Low.Remaining attempts:{remaining_attempts}")
           
    print(f"You Lose!The Number was: {num_to_be_guessed}")
def main():
    print("WELCOME TO NUMBER GUESSING GAME")
    mode=input("Enter mode for your game(EASY or HARD):").lower()
    if mode=="easy":
       play_game(10)
    elif mode=="hard":
        play_game(5)
    else:
        print("Wrong Mode")
main()
while True:
    
      choice=input("Replay:(Y/N)").lower()
      if choice!="y":
          break
      else:
          main()

    

            
        
    

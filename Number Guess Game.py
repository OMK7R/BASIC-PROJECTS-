import random

attempts=7

def display_rules():
    print("Welcome to Number Guessing Game !\n")
    print("I have Selected a Number Between 1 and 100.")
    print("You have 7 Attempts to guess it.\n")
    
def play_game(number,attempt=1):
    if attempt>attempts:
        print("\nGame Over")
        print("The Correct Number was :",number)
        return 
        
    guess=input(f"Attempt {attempt}/7---Enter Your Guess :")
    
    try:
        guess=int(guess)
    except ValueError:
        print("Please Enter a valid number.\n")
        return play_game(number,attempt)
        
    if guess <1 or guess>100:
        print("Please Enter a valid Number Between 1 and 100 .\n")
        return play_game(number,attempt)
        
    check_guess=lambda x,y : "Correct" if x==y else ("low" if x<y else "high")
     
    result=check_guess(guess,number)
     
    if result=="correct":
        print("\nCongratulations ! You Guessed The Correct Number !")
        print("You guessed it in ",attempt,"attempts")
        return
        
    if result=="low":
        print("It is Too low ! ,Try a higher Number.\n")
    else:
        print("It is Too high !, Try a lower Number.\n")
        
    play_game(number,attempt+1)

display_rules()

random_number=random.randint(1,100)

play_game(random_number)

        
        
    
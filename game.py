import random

def play_game():
    option = ['rock', 'paper', 'scissors']
    score = {'Player': 0, 'computer': 0}
    
    while True:
        user= input("Enter your choice (rock/paper/scissors): ")
        computer = random.choice(option)
        
        print("You chose:", user)
        print("Computer chose:", computer)
        
        if user == computer:
            print("It's a tie!")
        elif (user == 'rock' and computer == 'scissors') or (user == 'paper' and computer == 'rock') or (user == 'scissors' and computer == 'paper'):
            print("You win Yayaya ")
            score['Player'] += 1
        else:
            print("Computer wins Yayaya")
            score['computer'] += 1
            
        print("Score - Player:", score['Player'], "Computer:", score['computer'])
        
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

play_game()




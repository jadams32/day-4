# Welcome to the 4th day of the 100 days of code challenge. For this day I
# create a rock, paper, scissors game that the user can play against the
# computer. Give it a go and see if you can win!

import random

rock = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Initalize a play state so the game will loop if the player wants to play again
play_state = True
while play_state == True:

    # Create a list to make things easier.
    choice_list = [rock, paper, scissors]

    # Ask the player for their choice, then save it to be displayed.
    player_choice = int(input('What would you like to choose? Type "0" for rock, "1" for paper, and "2" for scissors.\n'))
    player_choice_displayed = choice_list[player_choice]

    # Show the player what they have chosen.
    print(f"You chose {player_choice_displayed}")

    # Have the computer pick a random choice, then save it to be displayed.
    computer_choice = random.randint(0,2)
    computer_choice_display = choice_list[computer_choice]

    # Logic for if the computer wins or if the player wins.
    if player_choice == computer_choice:
        print(f"Computer chooses {computer_choice_display} Draw! Please play again!")
    elif player_choice == 0 and computer_choice == 1:
        print(f"Computer chooses {computer_choice_display} You lose.")
    elif player_choice == 1 and computer_choice == 2:
        print(f"Computer chooses {computer_choice_display} You lose.")
    elif player_choice == 2  and computer_choice == 0:
        print(f"Computer chooses {computer_choice_display} You lose")
    elif player_choice == 1 and computer_choice == 0:
        print(f"Computer chooses {computer_choice_display} You Win!")
    elif player_choice == 2 and computer_choice == 1:
        print(f"Computer chooses {computer_choice_display} You win!")
    elif player_choice == 0  and computer_choice == 2:
        print(f"Computer chooses {computer_choice_display} You win!")


    # Ask the player if they want to play again
    play_again = input("Would you like to play again? Y or N\n")

    # Logic for play again
    if play_again == "N":
        play_state = False

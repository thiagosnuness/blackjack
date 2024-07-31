"""
main.py

Entry point for the Blackjack game.

This module initializes the game and manages the game loop.
It prompts the user to play a game of Blackjack and continues
to run until the user decides to quit.
"""

from replit import clear

from art import logo
from game import Game


def main():
    """
    Run the Blackjack game.

    Clears the console, displays the game logo, and prompts the user
    to start a new game. The user can play multiple rounds of Blackjack
    until they choose to exit.
    """
    clear()
    print(logo)

    while True:
        play = input(
            "\nDo you want to play a game of Blackjack? Type 'y' or 'n': "
        ).lower()
        while play not in ('y', 'n'):
            print("\nInvalid input. Please enter 'y' or 'n'.")
            play = input(
                "\nDo you want to play a game of Blackjack? Type 'y' or 'n': "
            ).lower()
        if play == 'y':
            Game().play()
        elif play == 'n':
            print("\nThanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()

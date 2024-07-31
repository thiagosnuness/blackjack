"""Main script to run the BlackJack game"""

from replit import clear

from art import logo
from game import Game


def main():
    """Run the BlackJack game"""
    clear()
    print(logo)
    play = input(
        "\nDo you want to play a game of Blackjack? Type 'y' or 'n': "
    )
    while play == "y":
        Game().play()
        play = input(
            "\nDo you want to play a game of Blackjack? Type 'y' or 'n': "
        )


if __name__ == "__main__":
    main()

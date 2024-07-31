"""
game.py

This module defines the Game class, which represents a game of Blackjack.
The Game class manages the overall game logic, including dealing cards,
calculating scores, and determining the winner.
"""

from replit import clear

from player import Player
from deck import Deck
from art import logo


class Game:
    """
    Represents a game of Blackjack.

    Attributes:
        __deck (Deck): The deck of cards used in the game.
        __player1 (Player): The first player in the game.
        __player2 (Player): The second player in the game.
    """

    def __init__(self, player1="user", player2="computer"):
        """
        Initialize the game with two players and a deck.

        Args:
            player1 (str): The name of player 1. Default is "user".
            player2 (str): The name of player 2. Default is "computer".
        """
        self.__deck = Deck()
        self.__player1 = Player(player1)
        self.__player2 = Player(player2)

    def deal_initial_cards(self):
        """Deal two initial cards to each player."""
        for _ in range(2):
            self.__player1.add_card(self.__deck.draw_card())
            self.__player2.add_card(self.__deck.draw_card())

    def play(self):
        """
        Start and play the game.

        Clears the screen, displays the game logo, deals initial cards,
        and manages the game loop where players draw cards and the
        winner is determined.
        """
        clear()
        print(logo)
        self.deal_initial_cards()
        self.show_scores()
        while self.__player1.get_score() < 21:
            user_input = input(
                "\nType 'y' to get another card, 'n' to pass: ").lower()
            while user_input not in ('y', 'n'):
                print("\nInvalid input. Please enter 'y' or 'n'.")
                user_input = input(
                    "\nType 'y' to get another card, 'n' to pass: ").lower()
            if user_input == 'y':
                self.__player1.add_card(self.__deck.draw_card())
                self.show_scores()
            elif user_input == 'n':
                break
        if self.__player1.get_score() <= 21:
            while self.__player2.get_score() < 17:
                self.__player2.add_card(self.__deck.draw_card())
        if self.__player1.get_score() > 21 or self.__player1.get_score() == 21:
            self.determine_winner()
            return
        self.show_scores()
        self.determine_winner()

    def show_scores(self):
        """Display the current scores and cards of both players."""
        print(
            f"\nYour cards: {self.__player1.get_cards()}, "
            f"current score: {self.__player1.get_score()}"
            )
        print(f"Computer's cards: {self.__player2.get_cards()}, "
              f"current score: {self.__player2.get_score()}"
              )

    def determine_winner(self):
        """
        Determine and display the winner of the game based on
        the current scores.
        """
        player_score = self.__player1.get_score()
        computer_score = self.__player2.get_score()
        if player_score > 21:
            print("\nYou went over. You lose 😭")
        elif computer_score > 21:
            print("\nOpponent went over. You win 😁")
        elif player_score > computer_score:
            print("\nYou win 😁")
        elif computer_score > player_score:
            print("\nYou lose 😭")
        else:
            print("\nDraw 🙃")

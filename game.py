"""The BlackJack Game module"""

from replit import clear

from art import logo
from deck import Deck


class Game(Deck):
    """The BlackJack Game"""
    def __init__(self, player1="user", player2="computer"):
        """Initialize attributes to describe a game."""
        super().__init__(player1, player2)
        self.__game_card = self.players_card()
        self.__cards_player1 = self.__game_card[self.name_player1()]
        self.__cards_player2 = self.__game_card[self.name_player2()]
        self.__final_player1 = self.calculate_score(self.__cards_player1)
        self.__final_player2 = self.calculate_score(self.__cards_player2)

    def calculate_score(self, cards):
        """
        Calculate the score for the given cards, handling Aces as 1 or 11.
        """
        score = sum(cards)
        if 11 in cards and score > 21:
            score -= 10  # Adjust for Ace
        return score

    def score(self):
        """Return the score"""
        print(
            f"\n\tYour cards: {self.__cards_player1}, "
            f"current score: {self.__final_player1}"
        )
        print(
            f"\tComputer's cards: {self.__cards_player2}, "
            f"current score: {self.__final_player2}"
        )

    def winner(self):
        """Return Blackjack winning player"""
        if self.__final_player1 > 21:
            print("\nYou went over. You lose 😭")
        elif self.__final_player2 > 21:
            print("\nOpponent went over. You win 😁")
        elif self.__final_player1 > self.__final_player2:
            print("\nYou win 😁")
        elif self.__final_player2 > self.__final_player1:
            print("\nYou lose 😭")
        else:
            print("\nDraw 🙃")

    def play(self):
        """Play BlackJack"""
        clear()
        print(logo)
        self.score()
        another_card = input(
            "\nType 'y' to get another card, type 'n' to pass: "
        )
        while another_card == "y":
            self.__cards_player1.append(self.choose_card())
            self.__final_player1 = self.calculate_score(self.__cards_player1)
            if self.__final_player1 > 21:
                break
            self.score()
            another_card = input(
                "\nType 'y' to get another card, type 'n' to pass: "
            )
        else:
            while self.__final_player2 < 17:
                self.__cards_player2.append(self.choose_card())
                self.__final_player2 = self.calculate_score(
                    self.__cards_player2
                )
        self.score()
        self.winner()

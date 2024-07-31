"""
player.py

This module defines the Player class used in the Blackjack game.
The Player class handles player-related information and actions,
such as storing player names and their respective cards.
"""


class Player:
    """Represents a player in the game."""

    def __init__(self, name):
        """
        Initialize attributes to describe a player.

        Args:
            name (str): The name of the player.
        """
        self.__name = name.lower()
        self.__cards = []

    def add_card(self, card):
        """
        Add a card to the player's hand.

        Args:
            card (int): The card to be added.
        """
        self.__cards.append(card)

    def get_score(self):
        """
        Calculate and return the player's current score.

        Returns:
            int: The player's current score.
        """
        score = sum(self.__cards)
        if 11 in self.__cards and score > 21:
            score -= 10
        return score

    def get_cards(self):
        """
        Get the player's current cards.

        Returns:
            list: The player's current cards.
        """
        return self.__cards

    def get_name(self):
        """
        Get the player's name.

        Returns:
            str: The player's name.
        """
        return self.__name

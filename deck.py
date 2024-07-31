"""
deck.py

This module defines the Deck class used in the Blackjack game.
The Deck class handles the creation of the deck, shuffling,
and drawing of cards. It also integrates player information through
composition with the Player class.
"""

import random


class Deck:
    """Represents a deck of cards."""

    def __init__(self):
        """Initialize the deck with a set of cards."""
        self.__cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def draw_card(self):
        """
        Draw a random card from the deck.

        Returns:
            int: The drawn card.
        """
        return random.choice(self.__cards)

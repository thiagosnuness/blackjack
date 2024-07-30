"""Module used to represent the deck."""

import random


class Player:
    """A dictionary of information about players"""
    def __init__(self, player1="user", player2="computer"):
        """Initialize attributes to describe a player."""
        self.__player1 = player1.lower()
        self.__player2 = player2.lower()
        self.__players_info = {self.__player1: [], self.__player2: []}

    def name_player1(self):
        """Return player1's name"""
        return self.__player1

    def name_player2(self):
        """Return player2's name"""
        return self.__player2

    def players(self):
        """Return a dictionary of information about players."""
        return self.__players_info


class Deck(Player):
    """Represents a deck of cards."""
    def __init__(self, player1="user", player2="computer"):
        """
        Initialize attributes to describe a deck.
        K, Q, J value 10 and Ace values 1 or 11.
        """
        super().__init__(player1, player2)
        self.__cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.__deck_player = self.players()

    def choose_card(self):
        """Return a random card from the deck."""
        return random.choice(self.__cards)

    def players_card(self):
        """Return a dictionary of information about players and deck."""
        for key in self.__deck_player:
            self.__deck_player[key] = [self.choose_card(), self.choose_card()]
        return self.__deck_player

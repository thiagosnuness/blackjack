# BlackJack

import random
from replit import clear
from art import logo


def deck():
    """Return random card from deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    chosen_card = random.choice(cards)
    return chosen_card


def players():
    """Return a dictionary of information about players."""
    players_info = {"user": [deck(), deck()], "computer": [deck()]}
    return players_info


def winner(user, computer):
    """Return Blackjack winning player"""
    if user > 21:
        print(f"You went over. You lose 😭")
    elif computer > 21:
        print(f"Opponent went over. You win 😁")
    elif user > computer:
        print(f"You win 😁")
    elif computer > user:
        print(f"You lose 😭")
    elif user == computer:
        print(f"Draw 🙃")


def blackjack():
    """Play BlackJack"""
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    player = players()
    if play == "y":
        stop = False
        clear()
        print(logo)
        while not stop:
            user_card = player["user"]
            computer_card = player["computer"]
            final_user = sum(user_card)
            print(f"\tYour cards: {user_card}, current score: {final_user}")
            print(f"\tComputer's first card: {computer_card}")
            another_card = input("Type 'y' to get another card, \
type 'n'to pass: ")
            if another_card == "y":
                user_card.append(deck())
                final_user = sum(user_card)
                if final_user > 21:
                    stop = True
                else:
                    continue
            elif another_card == "n":
                while sum(computer_card) < 17:
                    computer_card.append(deck())
                final_computer = sum(computer_card)
                break

        print(f"Your final hand: {user_card}, final score: {sum(user_card)}")
        final_computer = sum(computer_card)
        print(f"Computer's final hand: {computer_card}, \
final score: {final_computer}")
        winner(final_user, final_computer)
        blackjack()
    else:
        quit()


clear()
blackjack()

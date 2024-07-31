# Blackjack Game

Blackjack is a classic casino game, and this project is an implementation of the game in Python. The game allows a user to play against the computer.

## Project Structure

The project is organized into several files:

- **`player.py`**: Defines the `Player` class, which manages player information and tracks the cards dealt to each player.
- **`deck.py`**: Defines the `Deck` class, which represents the deck of cards and handles card dealing.
- **`game.py`**: Contains the `Game` class with the main logic for the Blackjack game.
- **`main.py`**: The entry point that initializes and runs the game.
- **`art.py`**: Contains the game's logo and other ASCII art.

## How to Run

### Requirements

- Python 3.x

### Steps

1. Clone the repository:
    ```sh
    git clone https://github.com/thiagosnuness/blackjack.git
    cd blackjack-game
    ```

2. Run the main script:
    ```sh
    python main.py
    ```

3. Follow the on-screen instructions to play.

## Code Overview

### `player.py`

This file contains the `Player` class:

- **`Player`**: Manages player information, including player names and the cards dealt to each player. Provides methods to retrieve player names and update the list of cards held by each player. Also includes methods to calculate the score of the player's hand.

### `deck.py`

This file contains the `Deck` class:

- **`Deck`**: Represents a deck of cards. Manages card values and the dealing of cards. Provides methods to draw cards from the deck and deal them to players.

### `game.py`

This file defines the `Game` class, which handles the main logic of the Blackjack game:

- Deals initial cards to players
- Calculates and updates scores based on cards drawn
- Determines the winner based on the scores
- Manages user inputs for drawing additional cards or passing

### `main.py`

This script is the entry point for the game. It initializes and runs the game loop, allowing the user to play multiple rounds of Blackjack until they choose to exit.

### `art.py`

Contains ASCII art for the Blackjack logo and any other graphical elements used in the game.

## Contributing

1. Fork the repository.
2. Create a branch for your feature (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

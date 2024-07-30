# Blackjack Game

Blackjack is a classic casino game, and this project is an implementation of the game in Python. The game allows a user to play against the computer.

## Project Structure

The project is organized into several files:

- **`deck.py`**: Defines the `Player` and `Deck` classes, which represent the players and the deck of cards.
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

### `deck.py`

This file contains the `Player` and `Deck` classes:

- **`Player`**: Manages player information and names.
- **`Deck`**: Manages the deck of cards and card dealing.

### `game.py`

This file defines the `Game` class, which manages the game flow, including:

- Dealing cards to players
- Calculating scores
- Determining the winner
- Handling user inputs

### `main.py`

This script is the entry point for the game. It runs the game and handles user interactions.

### `art.py`

Contains ASCII art for the Blackjack logo.

## Contributing

1. Fork the repository.
2. Create a branch for your feature (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

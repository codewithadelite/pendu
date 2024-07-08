# PENDU: Console Word Guessing Game

Welcome to PENDU, a fun and challenging console word guessing game! This documentation will guide you through the installation and usage of the game.

## Table of Contents

1. [Installation](#installation)
2. [Running the Game](#running-the-game)
3. [Gameplay Instructions](#gameplay-instructions)
4. [License](#license)

## Installation

To get started with PENDU, you need to install the required dependencies. Follow these steps:

1. **Clone the Repository** (if applicable):

   ```bash
   git clone https://github.com/codewithadelite/pendu.git
   cd pendu
   ```

2. **Install Dependencies**:
   Make sure you have Python installed on your system. Then, install the required packages using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Game

Once you have installed the necessary dependencies, you can start the game by running `pendu.py`:

```bash
python pendu.py
```

## Gameplay Instructions

1. **Objective**:
   The goal of the game is to guess the hidden word by suggesting letters within a certain number of attempts.

2. **How to Play**:

   - The game will display a series of underscores representing the hidden word.
   - You will be prompted to guess a letter.
   - If the letter is in the word, the game will reveal its position(s).
   - If the letter is not in the word, you lose an attempt.
   - The game continues until you either guess the word correctly or run out of attempts.

3. **Commands**:

   - Enter a single letter to guess.

4. **Winning and Losing**:
   - You win if you guess the word before running out of attempts.
   - You lose if you run out of attempts without guessing the word.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Enjoy playing PENDU!

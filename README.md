# Speed Typing Game - README

## Overview
The **Speed Typing Game** challenges players to type random phrases correctly within a time limit. It's a fun way to test typing speed and accuracy while competing for high scores.

---

## Features
- **Randomized Challenges**: Words and phrases are selected randomly from customizable difficulty levels.
- **Time-Based Gameplay**: Players must type the exact words displayed within a set time.
- **Dynamic Scoring System**: Feedback and levels based on performance.
- **Difficulty Modes**: Includes easy, medium, hard, and master levels for varying word complexities.
- **Pause/Start Functionality**: Players can pause or restart the game when needed.

---

## How to Play
1. Launch the game by running `python speed_typing_game.py`.
2. Follow the on-screen instructions:
   - You'll see a phrase and a time limit.
   - Type the phrase exactly as displayed before the timer runs out.
3. Your score and performance level will be displayed at the end.
4. Try to beat your high score!

---

## Files
- **`speed_typing_game.py`**: Main game logic.
- **`word_bank.py`**: Contains word lists categorized by difficulty.

---

## Functions

### Main Functions
- **`play_round(words, seconds)`**: Executes a single round and verifies if the player succeeded.
- **`pick_random_words(num_words, word_length)`**: Generates a random phrase of specified word count and length.
- **`get_random_word(mode)`**: Fetches a random word from the appropriate difficulty category in `word_bank.py`.
- **`level_message(score)`**: Displays motivational messages based on the player's score.

### Utility Functions
- **`display_instructions()`**: Prints the game instructions.
- **`pause_game()`**: Pauses the game.
- **`start_game()`**: Starts the game after an initial prompt.

---

## Scoring System
- **Score: 0** - "You only got a zero? Try harder."
- **Score: 1–3** - "Sad.... Try harder."
- **Score: 4–6** - "Try harder, I see potential..."
- **Score: 7–9** - "You might be a prodigy. Try again."
- **Score: 10–12** - "I'm shocked you made it this far! Go for the grand prize!"
- **Score: 13+** - "GOAT!!!"

---

## Customization
- **Modify Time Limits**: Adjust the `seconds` parameter in the `play_round()` function.
- **Add Words**: Update the word lists in `word_bank.py` for new challenges.

---

## Prerequisites
- Python 3.x
- A terminal or IDE to run the script.

---

## How to Run
1. Clone the repository or download the script files.
2. Place `speed_typing_game.py` and `word_bank.py` in the same directory.
3. Run the game:
   ```bash
   python speed_typing_game.py
   ```

---

## Contributing
Feel free to fork the repository and submit pull requests to add new features, word banks, or gameplay improvements!

---

## License
This project is open-source. Use and modify it as you wish! 🎉

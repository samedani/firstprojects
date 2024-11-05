"""Plays a game where the user types random words within a time limit."""

import random
import time
import word_bank


def play_round(words, seconds):
    """Returns True if the user successfully completed the round."""
    # Run a stopwatch for the time it takes the user to respond.
    start = time.time()
    response = input("(" + str(seconds) + " seconds...) " + words + "\n")
    stop = time.time()

    # Fail the round if a word is mispelled or if time runs out.
    within_time_limit = stop - start < seconds
    return response == words and within_time_limit


def pick_random_words(num_words, word_length):
    """Returns a random phrase containing the given number of words."""
    words = ""
    for word in range(num_words):
        word = get_random_word(word_length)
        words = words + " " + word

    return words.strip()


def get_random_word(mode):
    """Returns a random word with a word length based on the given mode."""
    if mode == "hard":
        words = word_bank.hard_words
    elif mode == "medium":
        words = word_bank.medium_words
    elif mode == "master":
        words = word_bank.master_words
    else:
        words = word_bank.easy_words

    return random.choice(words)


def level_message(score):
    if score == 0:
        print("Score: 0")
        print("You only got a zero?. Try harder")
    elif score <= 3:
        print(f"Score: {score}")
        print("Sad....Try harder")
    elif score <= 6:
        print(f"Score: {score}")
        print("Try harder, I see potential..")
    elif score <= 9:
        print(f"Score: {score}")
        print("You might be a prodigy, try again")
    elif score <= 12:
        print(f"Score: {score}")
        print("I'm shocked you made it this far")
        print("Why not try for the grandest prize?")
    else:
        print(f"Score: {score}")
        print("GOAT!!!")


def display_instructions():
    """
    Displays the instructions for the game.
    """
    print("\nWelcome to the Speed Typing Game!")
    print("Instructions:")
    print("1. You will be shown a set of words.")
    print("2. Type the words exactly as shown and press Enter.")
    print("3. Complete each round within the given time limit.")
    print("Good luck and have fun!\n")
    print("Hahaha! Your time has started")
    print("Hahaha! jk")


def pause_game():
    input("\nGame paused. Press Enter to continue...\n")


def start_game():
    input("\nGame paused. Press Enter to start...\n")









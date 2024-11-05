import typer

print("Type the words and hit enter within the time limit!")

score = 0  # Initialize score
typer.display_instructions()
typer.start_game()

# Play Level 1 (Easy)
for round in range(1, 4):
    print(f"Round {round}")

    words_to_type = typer.pick_random_words(round, "easy")
    passed = typer.play_round(words_to_type, 15)
    if not passed:
        typer.level_message(score)
        break
    else:
        score += 1

# Level 2 (Medium)
if score == 3:
    typer.pause_game()
    print("Level 2 awaits you!")
    for round in range(1, 4):
        print(f"Round {round}")

        words_to_type = typer.pick_random_words(round, "medium")
        passed = typer.play_round(words_to_type, 15)
        if not passed:
            typer.level_message(score)
            break
        else:
            score += 1

# Level 3 (Hard)
if score == 6:
    typer.pause_game()
    print("Persevere, tenacity is what makes men great!")
    for round in range(1, 4):
        print(f"Round {round}")

        words_to_type = typer.pick_random_words(round, "hard")
        passed = typer.play_round(words_to_type, 20)
        if not passed:
            typer.level_message(score)
            break
        else:
            score += 1

# Level 4 (Another Hard Level)
if score == 9:
    typer.pause_game()
    print("Another hard level, is it in you?!")
    for round in range(1, 4):
        print(f"Round {round}")

        words_to_type = typer.pick_random_words(round, "hard")
        passed = typer.play_round(words_to_type, 20)
        if not passed:
            typer.level_message(score)
            break
        else:
            score += 1

# Master Level
if score == 12:
    typer.pause_game()
    print("Master level!!!")
    for round in range(1, 4):
        print(f"Round {round}")

        words_to_type = typer.pick_random_words(round, "master")
        passed = typer.play_round(words_to_type, 25)
        if not passed:
            typer.level_message(score)
            break
        else:
            score += 1
            typer.level_message(score)


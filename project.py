import random
from pyfiglet import Figlet
from tabulate import tabulate
import sys


figlet = Figlet(font="slant")
green = "\033[92m"
yellow = "\033[93m"
red = "\033[91m"
reset = "\033[0m"


def main():
    # word = get_random_word("./words.txt")
    try:
        word = get_random_word("./words.txt")
    except (FileNotFoundError, ValueError):
        sys.exit("Text file does not exist or is empty. ")


    print(figlet.renderText("WORDLE"))
    print("    🌟 HOW TO PLAY 🌟\n"
          "- Guess the Wordle in 6 tries.\n"
          "- Each guess must be a valid 5-letter word.\n"
          f"- The {red}letters{reset} will {yellow}change{reset} color to give you {green}clues{reset}.\n"
          f"{green}💚 Green: The letter is correct and in the correct position.{reset}\n"
          f"{yellow}💛 Yellow: The letter is correct but in the wrong position.{reset}\n"
          f"{red}❤  Red: The letter is not in the word at all.{reset}\n"
          "- Press CTRL + C to exit.\n")

    attempts = []
    max_attempts = 6

    while len(attempts) < max_attempts:
        guess = input("Enter word: ").strip().upper()

        if len(guess) != 5 or not guess.isalpha():
            print("Please enter a valid 5-letter word.")
            continue

        attempts.append(guess)
        print_results(attempts, word)

        if check_guess(word, guess) == False and len(attempts) < max_attempts:
            print("Try again!")
            continue
        else:
            break

    if guess != word:
        print(f"Game over! The correct word was: {green}{word}{reset}")
    else:
        print("You guessed the word! 🎉")


def get_random_word(path):
    try:
        with open(path, "r") as file:
            words = file.readlines()
            if len(words) == 0:
                raise ValueError
            random_word = random.choice(words).strip().upper()
            return random_word
    except FileNotFoundError:
        raise FileNotFoundError


def check_guess(word, guess):

    return guess == word


def print_results(attempts, word):
    results = [list(guess) for guess in attempts]

    for i in range(len(results)):
        for x in range(len(results[i])):

            current_letter = results[i][x]
            if current_letter == word[x]:
                results[i][x] = f"{green}{results[i][x]}{reset}"
            elif current_letter in word:
                results[i][x] = f"{yellow}{results[i][x]}{reset}"
            elif current_letter not in word:
                results[i][x] = f"{red}{results[i][x]}{reset}"


    print(tabulate(results, tablefmt="fancy_grid"))


if __name__ == "__main__":
    main()

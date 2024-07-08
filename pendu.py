import requests
import os
import random

from tabulate import tabulate
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

RANDOM_WORD_API_URL = "https://random-word-api.p.rapidapi.com"
MAX_TRY = 10

# For statisctics
fail_track = 0
incorrect_inputed_letters = []

headers = {
    "x-rapidapi-key": "4ea47ae308msh6002b71eece04d2p149ba1jsn27e2e5e7390d",
    "x-rapidapi-host": "random-word-api.p.rapidapi.com",
}

word = ""
guessed_word = []
choosed_words = []
difficulty_level = 0
is_success = False


def display_statistics(incorrect_inputed_letters):
    attempts = ["Attempts"] + [i for i in range(1, 11)]
    data_template = ["_"] * 10

    for i, value in enumerate(incorrect_inputed_letters):
        if i < 4:
            data_template[i] = Fore.GREEN + value + Style.RESET_ALL
        elif i < 7:
            data_template[i] = Fore.YELLOW + value + Style.RESET_ALL
        else:
            data_template[i] = Fore.RED + value + Style.RESET_ALL
    data = ["Letter"] + data_template
    table = [attempts, data]
    print(tabulate(table, tablefmt="grid"))


def display_menu():
    print("MENU:\n", "1: FACILE \n", "2: MOYENE \n", "3: DIFFICILE \n")


def generate_word_and_assign_to_choosen_words(choosed_words, level):
    global word

    word_length = random.randint(5, 6)  # Facile

    if level == 2:
        word_length = random.randint(8, 10)  # Moyene

    if level == 3:
        word_length = random.randint(10, 13)  # Moyene

    word = requests.get(
        f"{RANDOM_WORD_API_URL}/LS/{word_length}/fru", headers=headers
    ).json()["word"]

    while word in choosed_words:
        word = requests.get(
            f"{RANDOM_WORD_API_URL}/LS/{word_length}/fru", headers=headers
        ).json()["word"]
    choosed_words.append(word)


def choose_level_difficulty():
    global difficulty_level

    difficulty_level = int(input("Choose difficulty level:"))

    while difficulty_level not in [1, 2, 3]:
        print("Invalid input:")
        difficulty_level = int(input("Choose difficulty level:"))


def display_guessed_word():
    concat_word = ""
    for letter in guessed_word:
        concat_word += letter + " "
    print("\n" + concat_word + "\n")


def generate_guessed_word_template(word):
    for _ in word:
        guessed_word.append("_")


def is_letter_in_word(letter, word):
    for l in word:
        if l.lower() == letter.lower():
            return True
    return False


def get_indexes_of_letter_in_word(letter, word):
    indexes = []
    for i, value in enumerate(word):
        if letter.lower() == value.lower():
            indexes.append(i)
    return indexes


def change_guessed_word(indexes, letter):
    for index in indexes:
        guessed_word[index] = letter


def word_complted(word: list):
    return "_" not in word


def guess():
    global fail_track
    global is_success
    global incorrect_inputed_letters
    global guessed_word

    while fail_track < MAX_TRY and not is_success:
        display_guessed_word()

        inputed_letter = ""

        while True:

            inputed_letter = str(input("Guess a letter: "))

            if inputed_letter.isnumeric():
                print("Invalid input. Cant enter numbers")
                continue
            if inputed_letter in guessed_word:
                print("You already guessed that letter")
                continue
            break

        if not is_letter_in_word(inputed_letter, word):
            fail_track += 1
            incorrect_inputed_letters.append(inputed_letter)
        else:
            indexes_of_letter = get_indexes_of_letter_in_word(inputed_letter, word)
            change_guessed_word(indexes_of_letter, inputed_letter)

            if word_complted(guessed_word):
                is_success = True
                break

        display_statistics(incorrect_inputed_letters)

    if is_success:
        print(Fore.GREEN + "Gagne!!" + Style.RESET_ALL)

    if fail_track == MAX_TRY:
        print(Fore.RED + "Perdu!!! Mots est:", word, Style.RESET_ALL)

    fail_track = 0  # Reset to zero
    guessed_word = []
    incorrect_inputed_letters = (
        []
    )  # Reset to empty. Incase user decides to replay it will start as empty


def start_game():
    display_menu()
    choose_level_difficulty()
    generate_word_and_assign_to_choosen_words(choosed_words, difficulty_level)
    generate_guessed_word_template(word)
    guess()


user_still_want_to_play = True

while user_still_want_to_play:
    start_game()

    choice = input("Voulez-vous rejouer ? true/false")

    while choice not in ["true", "false"]:
        print(
            Fore.CYAN
            + "Reponse incorrecte : true ou force uniquement"
            + Style.RESET_ALL
        )
        choice = input("Voulez-vous rejouer ? true/false: ")

    if choice == "false":
        break

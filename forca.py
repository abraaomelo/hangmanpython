import random

def play():
    print_welcome()
    secret_word = load_secret_word()

    correct_letters = load_correct_letters(secret_word)
    print(correct_letters)

    hanged = False
    won = False
    errors = 0
    guess_list = []

    while(not hanged and not won):

        guess = ask_guess()


        if(guess in guess_list):
            print("Letter already told, try a different one !\n")
        elif(guess in secret_word):
            set_correct_guess(guess, correct_letters, secret_word)
        else:
            errors += 1
            draw_hang(errors)

        guess_list.append(guess)
        hanged = errors == 7
        won = "_" not in correct_letters

        print(correct_letters)
        print("Guess list: {}".format(guess_list))

    if(won):
        won_message()
    else:
        lose_message(secret_word)


def draw_hang(errors):
    print("  _______     ")
    print(" |/      |    ")

    if(errors == 1):
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")

    if(errors == 2):
        print (" |      (_)   ")
        print (" |      \     ")
        print (" |            ")
        print (" |            ")

    if(errors == 3):
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |            ")
        print (" |            ")

    if(errors == 4):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |            ")
        print (" |            ")

    if(errors == 5):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    if(errors == 6):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    if (errors == 7):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def won_message():
    print("YOU  WIN !!!!!")
    print("Congratulations :)")


def lose_message(secret_word):
    print("You were hanged ! XXXX")
    print("Word was:  {}".format(secret_word))


def set_correct_guess(guess, correct_letters, secret_word):
    index = 0
    for letter in secret_word:
        if (guess == letter):
            correct_letters[index] = letter
        index += 1

def ask_guess():
    guess = input("Type a letter: ")
    guess = guess.strip().upper()
    return guess

def load_correct_letters(word):
    return ["_" for letter in word]

def print_welcome():
    print("*********************************")
    print("***Welcome  to  hangman  game!***")
    print("*********************************")

def load_secret_word():
    file = open("words.txt", "r")
    words = []

    for row in file:
        row = row.strip()
        words.append(row)

    file.close()

    num = random.randrange(0, len(words))
    secret_word = words[num].upper()
    return secret_word


if(__name__ == "__main__"):
    play()
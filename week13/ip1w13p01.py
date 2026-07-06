"""Week 13 project 1: guess the computer's number."""

import random


def getYesNo(prompt):
    while True:
        answer = input(prompt + " (yes/no): ")
        answer = answer.lower().strip()

        # y, ye, yes みたいな途中までの入力もyesとして受け取る。
        if answer != "" and "yes".startswith(answer):
            return True
        if answer != "" and "no".startswith(answer):
            return False

        print("Please answer yes or no.")


def getGuess():
    while True:
        answer = input("Your guess: ")
        try:
            return int(answer)
        except ValueError:
            # 数字でない入力は、回数に入れずにもう一度聞く。
            print("Please type a whole number.")


def playGame():
    number = random.randint(1, 100)
    count = 0

    print("I have thought of a number between 1 and 100.")
    print("Try to guess the number.")

    while True:
        guess = getGuess()
        count = count + 1

        if guess < number:
            print("Too low.")
            continue
        if guess > number:
            print("Too high.")
            continue

        print("You guessed the number in", count, "attempts.")
        break


if __name__ == "__main__":
    playing = True
    while playing:
        playGame()
        playing = getYesNo("Play again")

"""Week 13 project 2: the computer guesses your number."""


def getYesNo(prompt):
    while True:
        answer = input(prompt + " (yes/no): ")
        answer = answer.lower().strip()

        # 大文字小文字は気にしない。yやnだけでも分かるようにしている。
        if answer != "" and "yes".startswith(answer):
            return True
        if answer != "" and "no".startswith(answer):
            return False

        print("Please answer yes or no.")


def getHighLowCorrect(prompt):
    while True:
        answer = input(prompt + ": ")
        answer = answer.lower().strip()

        # h, l, c だけでも答えられるように、単語の先頭一致で見る。
        if answer != "" and "high".startswith(answer):
            return "high"
        if answer != "" and "low".startswith(answer):
            return "low"
        if answer != "" and "correct".startswith(answer):
            return "correct"

        print("Please answer high, low, or correct.")


def playGame():
    low = 1
    high = 100
    count = 0

    print("Think of a number between 1 and 100.")
    print("I will try to guess it.")
    print("Each time I guess, tell me if I am HIGH, LOW, or CORRECT.")

    while low <= high:
        # 範囲の真ん中を選ぶので、毎回候補がだいたい半分になる。
        guess = (low + high) // 2
        count = count + 1

        print("My guess is:", guess)
        answer = getHighLowCorrect("Am I HIGH, LOW, or CORRECT")

        if answer == "correct":
            print("I got it in", count, "attempts.")
            return
        if answer == "high":
            high = guess - 1
        if answer == "low":
            low = guess + 1

    # lowとhighが逆転したら、どこかの返事が矛盾している。
    print("That cannot be right; your answers do not fit one number.")


if __name__ == "__main__":
    playing = True
    while playing:
        playGame()
        playing = getYesNo("Play again")

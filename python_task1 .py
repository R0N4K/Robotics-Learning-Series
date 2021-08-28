import random

def compare_number(number, user_guess):
    Positive_marks = [0, 0, 0, 0]
    for i in range(len(number)):
        if number[i] == user_guess[i]:
           Positive_marks[i] += 1
    return Positive_marks


if __name__ == "__main__":
    playing = True
    number = str(random.randint(1000, 10000))
    guesses = 0
    print([number])


while playing:
    user_guess = input("GUESS THE FOUR DIGIT NUMBER: ")
    if user_guess.lower() == "exit":
        break
    positivenegative_count = compare_number(number, user_guess)
    guesses += 1
    correct = sum(positivenegative_count)
    wrong = len(number) - correct
    print(f"You Have {correct} +5, And {wrong} -2.")

    if correct == 4:
        playing = False
        print(f"You Win The Game After {guesses} Guess(es)!")
        break
    else:
        print(f"Your Guess Isn't Quite Right, Try Again!.")
        if correct >= 1:
            print(str([user_guess[i] for i, x in enumerate(positivenegative_count) if x == 1]) + " was correct!")

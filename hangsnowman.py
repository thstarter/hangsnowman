import random
words = ["cat", "boo", "scary", "massacre", "halloween"]
random = random.choice(words)

def hangsnowman(word):
    wrong = 0
    stages = ["",
              "_______   ",
              "|         ",
              "|    |    ",
              "|    O    ",
              "|   -O-   ",
              "|    O    ",
              "|         "
              ]
    letters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        print(wrong)
        guess = input("Guess a letter")
        if guess in letters:
            c = letters.index(guess)
            board[c] = guess
            letters[c] = '$'
        else:
            wrong += 1
        print("".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "__" not in board:
            print("You win! It was {}.".format(word))
            win = True
            break
    if not win:
        print("\n".join(stages[0:e]))
        print("You lose! It was {}.".format(word))

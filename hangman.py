def hangman(word):
    wrong = 1
    stages = ["",
              "__________          ",
              "|         |         ",
              "|         |         ",
              "|         |         ",
              "|         O         ",
              "|        /|\        ",
              "|        / \        ",
              "|                   ",
              ]
    answer = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to the 'Hangman!!'.")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a character: "
        char = input(msg)
        if char in answer:
            cind = answer.index(char)
            board[cind] = char
            answer[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You lost. The answer is {}.".format(word))

hangman("Eminem")

def hangman(word):
    wrong = 0
    stages = ["",
              "____   ",

              "|      ",
              
              "|   |   ",

              "|   0   ",

              "| : | :    ",

              "|  : :   ",

              "|      "
             ]
    #↓正解の文字を一文字づつ分割する↓
    rletters = list(word)
    board = "_" * len(word)
    win = False
    print("welcometohangman")
    while wrong < len(stages) -1:
        print("\n")
        msg = "Expect one character"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'

        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        win = True
        break
    if not win :
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け!正解は {}." .format(word))
    
    
        

hangman("c")

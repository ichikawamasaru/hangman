def hangman(word):
    wrong = 0
    result = list(word)
    youser_input = input("文字を入力してください。")
    ans = list(youser_input)
    print(ans)
    stages = ["",
              "____   ",

              "|      ",
              
              "|   |   ",

              "|   0   ",

              "| / | \     ",

              "|      ",

              "|      "
             
             ]


hangman("cat")

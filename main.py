from game import ZeroSquaresGame


def main():

    board1 = [
        ["X", "X", "X", "X", "X"],
        ["X", ".", "R", ".", "X"],
        ["X", ".", ".", ".", "X"],
        ["X", ".", ".", ".", "X"],
        ["X", "X", "X", "X", "X"],
    ]

    board2 = [
        ["X", "X", "X", "X", "X", "X", "X"],
        ["X", "GB", "X", "GY", "X", "GR", "X"],
        ["X", ".", ".", ".", ".", ".", "X"],
        ["X", "Y", ".", ".", ".", ".", "X"],
        ["X", "X", ".", ".", ".", ".", "X"],
        ["X", "X", ".", "R", ".", "B", "X"],
        ["X", "X", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "X", "X"],
    ]

    board3 = [
        ["X", "X", "X", "X", "X", "X", "X", "X"],
        ["X", ".", ".", ".", ".", "GR", "X", "X"],
        ["X", "R", ".", "GB", ".", ".", "X", "X"],
        ["X", ".", ".", ".", ".", ".", ".", "X"],
        ["X", "GY", ".", ".", "Y", ".", ".", "X"],
        ["X", "X", ".", ".", ".", ".", ".", "X"],
        ["X", "X", "B", ".", "X", "X", ".", "X"],
        ["X", "X", "X", "X", "X", "X", "X", "X"],
    ]
    board4 = [
        ["X", "X", "X", "X", "X", "X", "X", "X", "X"],
        ["X", ".", ".", ".", ".", ".", ".", "GY", "X"],
        ["X", "R", ".", "X", ".", "B", ".", ".", "X"],
        ["X", ".", ".", ".", "GR", ".", ".", "Y", "X"],
        ["X", ".", ".", "GB", ".", ".", ".", ".", "X"],
        ["X", ".", ".", ".", ".", ".", "GY", ".", "X"],
        ["X", ".", "Y", ".", "X", ".", ".", ".", "X"],
        ["X", ".", ".", ".", ".", ".", ".", ".", "X"],
        ["X", "X", "X", "X", "X", "X", "X", "X", "X"],
    ]
    board5 = [
        ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
        ["X", "GR", ".", ".", ".", "GY", ".", ".", ".", "X"],
        ["X", ".", ".", ".", ".", ".", ".", ".", ".", "X"],
        ["X", "R", ".", "GB", ".", "Y", ".", ".", "B", "X"],
        ["X", ".", ".", ".", ".", ".", ".", ".", ".", "X"],
        ["X", ".", ".", ".", "X", "R", ".", ".", ".", "X"],
        ["X", ".", ".", ".", ".", ".", ".", "GY", ".", "X"],
        ["X", ".", "B", ".", ".", ".", ".", ".", ".", "X"],
        ["X", ".", ".", ".", ".", ".", ".", ".", ".", "X"],
        ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
    ]
    board6 = [
        ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
        ["X", ".", ".", ".", "GR", ".", ".", ".", ".", ".", "X"],
        ["X", ".", ".", ".", ".", ".", ".", ".", ".", ".", "X"],
        ["X", ".", "GY", ".", ".", ".", "B", ".", ".", ".", "X"],
        ["X", ".", ".", ".", "GB", ".", ".", ".", ".", ".", "X"],
        ["X", ".", ".", ".", ".", ".", ".", ".", ".", ".", "X"],
        ["X", ".", ".", ".", ".", ".", ".", ".", ".", "Y", "X"],
        ["X", ".", ".", ".", ".", ".", ".", ".", ".", ".", "X"],
        ["X", "R", ".", ".", ".", ".", ".", ".", ".", ".", "X"],
        ["X", ".", ".", ".", ".", ".", ".", ".", ".", ".", "X"],
        ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
    ]

    choose = input("Choose The Board You prefer To Play (1/2/3/4/5/6): ")
    if choose == "1":
        game = ZeroSquaresGame(10, board1)

        game.play()
    elif choose == "2":
        game = ZeroSquaresGame(7, board2)

        game.next_step
        game.play()
    elif choose == "3":
        game = ZeroSquaresGame(11, board3)
        game.play()
    elif choose == "4":
        game = ZeroSquaresGame(9, board4)
        game.play()
    elif choose == "5":
        game = ZeroSquaresGame(10, board5)
        game.play()
    elif choose == "6":
        game = ZeroSquaresGame(11, board6)
        game.play()
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()

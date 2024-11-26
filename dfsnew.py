class DFS_R:
    def __init__(self, initial_board):
        self.initial_board = initial_board
        self.visited_boards = set()
        self.successful_paths = []
        self.path = []

    def DFS_new(self, current_board, path=None):
        if path is None:
            path = []

        if current_board.win():
            self.successful_paths.append(path + [current_board])
            return

        board_tuple = tuple(map(tuple, current_board.board))

        if board_tuple in self.visited_boards:
            return

        self.visited_boards.add(board_tuple)

        for next_game in current_board.next_step():
            if tuple(map(tuple, next_game.board)) not in self.visited_boards:

                self.DFS_new(next_game, path + [current_board])

    def all_wining_state(self):

        if self.successful_paths:
            print("winning paths!")

            for i, path in enumerate(self.successful_paths):
                print(f"Winning Path {i + 1}:")
                for step, game in enumerate(path):
                    print(f"Step {step}:")
                    game.printtheboard()
            return True
        else:
            print("Game over.")

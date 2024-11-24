class DFS:
    def init(self, initial_board):
        self.initial_board = initial_board
        self.visited_boards = set()
        self.successful_paths = []

    def dfs(self, current_board, path):
        if current_board.win():
            self.successful_paths.append(path + [current_board])
            return

        board_tuple = tuple(map(tuple, current_board.board))

        if board_tuple in self.visited_boards:
            return

        self.visited_boards.add(board_tuple)

        for next_game in current_board.next_step():
            if tuple(map(tuple, next_game.board)) not in self.visited_boards:
                self.dfs(next_game, path + [current_board])

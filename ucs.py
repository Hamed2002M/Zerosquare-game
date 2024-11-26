import heapq


class UCS_class:
    def __init__(self, initial_board):
        self.initial_board = initial_board
        self.visited_boards = set()
        self.priority_queue = []
        self.successful_paths = []

    def ucs(self):

        heapq.heappush(
            self.priority_queue, (0, id(self.initial_board), self.initial_board, [])
        )

        while self.priority_queue:
            cost, _, current_board, path = heapq.heappop(self.priority_queue)

            board_tuple = tuple(map(tuple, current_board.board))

            if board_tuple in self.visited_boards:
                continue

            self.visited_boards.add(board_tuple)

            if current_board.win():
                self.successful_paths.append(path + [current_board])

            for next_game, weight in self.nextstep_with_costs(current_board):

                if tuple(map(tuple, next_game.board)) not in self.visited_boards:

                    heapq.heappush(
                        self.priority_queue,
                        (
                            cost + weight,
                            id(next_game),
                            next_game,
                            path + [current_board],
                        ),
                    )

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

    def nextstep_with_costs(self, current_board):

        nextsteps = []
        for next_board in current_board.next_step():
            weight = self.add_cost()
            nextsteps.append((next_board, weight))
        return nextsteps

    def add_cost(self):
        return 1

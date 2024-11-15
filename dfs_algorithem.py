from collections import deque


class Solver:

    def __init__(self, initial_game):
        self.initial_game = initial_game
        self.visited_boards = set()

    def solveDFS(self):
        stack = [(self.initial_game, [])]
        winning_paths = []

        while stack:
            current_game, path = stack.pop()

            if current_game.win():
                winning_paths.append(path + [current_game])
                continue

            board_tuple = tuple(map(tuple, current_game.board))
            if board_tuple in self.visited_boards:
                continue

            self.visited_boards.add(board_tuple)

            for next_game in current_game.next_step():
                next_board_tuple = tuple(map(tuple, next_game.board))
                if next_board_tuple not in self.visited_boards:
                    stack.append((next_game, path + [current_game]))

        if winning_paths:
            print("Found multiple winning paths!")
            for i, path in enumerate(winning_paths):
                print(f"Winning Path {i + 1}:")
                for step, game in enumerate(path):
                    print(f"Step {step}:")
                    game.printtheboard()
            return True
        else:
            print("No solution found.")
            return False

    def solveBFS(self):
        queue = deque([(self.initial_game, [])])
        winning_paths = []

        while queue:
            current_game, path = queue.popleft()

            if current_game.win():
                winning_paths.append(path + [current_game])
                continue

            board_tuple = tuple(map(tuple, current_game.board))
            if board_tuple in self.visited_boards:
                continue
            self.visited_boards.add(board_tuple)

            for next_game in current_game.next_step():
                next_board_tuple = tuple(map(tuple, next_game.board))
                if next_board_tuple not in self.visited_boards:
                    queue.append((next_game, path + [current_game]))

        if winning_paths:
            print("I found the paths")
            for i, path in enumerate(winning_paths):
                print(f"Winning Path {i + 1}:")
                for step, game in enumerate(path):
                    print(f"Step {step}:")
                    game.printtheboard()
            return True

        print("No solution found.")
        return False

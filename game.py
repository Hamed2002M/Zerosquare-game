import copy
from astar import AStar
from dfs_algorithem import Solver
from dfsnew import DFS_R
from ucs import UCS_class


class ZeroSquaresGame:
    previous_boards = []

    def __init__(self, n, board):
        self.n = n
        self.board = board

    def printtheboard(self):
        for row in self.board:
            print(" ".join(row))
        print()

    def is_valid_move(self, x, y, dx, dy):
        if 0 <= x + dx < self.n and 0 <= y + dy < self.n:
            return self.board[x + dx][y + dy] in {".", "GY", "GR", "GB", "GC"}
        return False

    def can_move_right(self, x, y):
        return self.is_valid_move(x, y, 0, 1)

    def can_move_left(self, x, y):
        return self.is_valid_move(x, y, 0, -1)

    def can_move_up(self, x, y):
        return self.is_valid_move(x, y, -1, 0)

    def can_move_down(self, x, y):
        return self.is_valid_move(x, y, 1, 0)

    def move(self, dx, dy):
        new_board = self.board
        new_board = copy.deepcopy(self.board)  # عمل نسخة عميقة من اللوحة
        ZeroSquaresGame.previous_boards.append(copy.deepcopy(self.board))
        ZeroSquaresGame.previous_boards.append(self.board)
        for x in range(self.n):
            for y in range(self.n):
                if self.board[x][y] not in {"X", "GR", "GB", "GY", "GC", "."}:
                    nx, ny = x, y
                    while self.is_valid_move(nx, ny, dx, dy):
                        nx += dx
                        ny += dy
                        if new_board[x][y] == "Y" and self.board[nx][ny] == "GY":
                            new_board[x][y] = "."
                            new_board[nx][ny] = "."

                        if new_board[x][y] == "R" and self.board[nx][ny] == "GR":
                            new_board[x][y] = "."
                            new_board[nx][ny] = "."

                        if new_board[x][y] == "B" and self.board[nx][ny] == "GB":
                            new_board[x][y] = "."
                            new_board[nx][ny] = "."

                        if new_board[x][y] == "C" and self.board[nx][ny] == "GC":
                            new_board[x][y] = "."
                            new_board[nx][ny] = "."

                    while (
                        new_board[nx][ny] == "." and new_board[nx + dx][ny + dy] == "."
                    ):
                        nx += dx
                        ny += dy

                    if new_board[nx][ny] == "." and new_board[x][y] == "Y":
                        new_board[x][y], new_board[nx][ny] = ".", "Y"

                    if new_board[nx][ny] == "." and new_board[x][y] == "R":
                        new_board[x][y], new_board[nx][ny] = ".", "R"

                    if new_board[nx][ny] == "." and new_board[x][y] == "B":
                        new_board[x][y], new_board[nx][ny] = ".", "B"

                    if new_board[nx][ny] == "." and new_board[x][y] == "C":
                        new_board[x][y], new_board[nx][ny] = ".", "C"

                    if new_board[nx][ny] == "GY" and new_board[x][y] == "R":
                        new_board[x][y], new_board[nx][ny] = ".", "GY,R"

                    if new_board[nx][ny] == "GY" and new_board[x][y] == "B":
                        new_board[x][y], new_board[nx][ny] = ".", "GY,B"

                    if new_board[nx][ny] == "GY" and new_board[x][y] == "C":
                        new_board[x][y], new_board[nx][ny] = ".", "GY,C"

                    if new_board[nx][ny] == "GB" and new_board[x][y] == "Y":
                        new_board[x][y], new_board[nx][ny] = ".", "GB,Y"

                    if new_board[nx][ny] == "GB" and new_board[x][y] == "R":
                        new_board[x][y], new_board[nx][ny] = ".", "GB,R"

                    if new_board[nx][ny] == "GB" and new_board[x][y] == "C":
                        new_board[x][y], new_board[nx][ny] = ".", "GB,C"

                    if new_board[nx][ny] == "GR" and new_board[x][y] == "B":
                        new_board[x][y], new_board[nx][ny] = ".", "GR,B"

                    if new_board[nx][ny] == "GR" and new_board[x][y] == "Y":
                        new_board[x][y], new_board[nx][ny] = ".", "GR,Y"

                    if new_board[nx][ny] == "GR" and new_board[x][y] == "C":
                        new_board[x][y], new_board[nx][ny] = ".", "GR,C"

                    if new_board[nx][ny] == "GC" and new_board[x][y] == "B":
                        new_board[x][y], new_board[nx][ny] = ".", "GC,B"

                    if new_board[nx][ny] == "GC" and new_board[x][y] == "Y":
                        new_board[x][y], new_board[nx][ny] = ".", "GC,Y"

                    if new_board[nx][ny] == "GC" and new_board[x][y] == "R":
                        new_board[x][y], new_board[nx][ny] = ".", "GC,R"

                    if new_board[nx][ny] == "." and new_board[x][y] == "GY,R":
                        new_board[x][y], new_board[nx][ny] = "GY", "R"

                    if new_board[nx][ny] == "." and new_board[x][y] == "GY,B":
                        new_board[x][y], new_board[nx][ny] = "GY", "B"

                    if new_board[nx][ny] == "." and new_board[x][y] == "GY,C":
                        new_board[x][y], new_board[nx][ny] = "GY", "C"

                    if new_board[nx][ny] == "." and new_board[x][y] == "GR,Y":
                        new_board[x][y], new_board[nx][ny] = "GR", "Y"

                    if new_board[nx][ny] == "." and new_board[x][y] == "GR,B":
                        new_board[x][y], new_board[nx][ny] = "GR", "B"

                    if new_board[nx][ny] == "." and new_board[x][y] == "GR,C":
                        new_board[x][y], new_board[nx][ny] = "GR", "C"

                    if new_board[nx][ny] == "." and new_board[x][y] == "GB,Y":
                        new_board[x][y], new_board[nx][ny] = "GB", "Y"

                    if new_board[nx][ny] == "." and new_board[x][y] == "GB,R":
                        new_board[x][y], new_board[nx][ny] = "GB", "R"

                    if new_board[nx][ny] == "." and new_board[x][y] == "GB,C":
                        new_board[x][y], new_board[nx][ny] = "GB", "C"

                    if new_board[nx][ny] == "." and new_board[x][y] == "GC,B":
                        new_board[x][y], new_board[nx][ny] = "GC", "B"

                    if new_board[nx][ny] == "." and new_board[x][y] == "GC,R":
                        new_board[x][y], new_board[nx][ny] = "GC", "R"

                    if new_board[nx][ny] == "." and new_board[x][y] == "GC,Y":
                        new_board[x][y], new_board[nx][ny] = "GC", "Y"

        return ZeroSquaresGame(self.n, new_board)

    def win(self):

        for row in self.board:
            for cell in row:
                if cell in {
                    "GY",
                    "GR",
                    "GB",
                    "GC",
                    "GR,Y",
                    "GY,R",
                    "GY,B",
                    "GY,C",
                    "GR,C",
                    "GR,B",
                    "GB,Y",
                    "GB,R",
                    "GB,C",
                }:
                    return False
        return True

    def play(self):
        self.printtheboard()
        while True:
            if self.win():
                print("Congratulations! You are the winner!")
                break
            move = input(
                "Enter move (w/a/s/d) or enter (h) to view the next state or DFS ,BFS,DFS_R,UCS: "
            )
            if move == "w":
                self = self.move(-1, 0)
            elif move == "s":
                self = self.move(1, 0)
            elif move == "a":
                self = self.move(0, -1)
            elif move == "d":
                self = self.move(0, 1)
            elif move == "h":
                self.next_step()
                continue
            elif move == "DFS":
                solver = Solver(self)
                if solver.solveDFS():
                    print("DFS found a solution!")
                    break
            elif move == "DFS_R":
                dfs_r = DFS_R(self)
                if dfs_r.DFS_new(self):
                    break
                if dfs_r.all_wining_state():
                    break
            elif move == "BFS":
                solver = Solver(self)
                if solver.solveBFS():
                    break
            elif move == "UCS":
                ucs = UCS_class(self)
                if ucs.ucs():
                    break
            elif move == "a*":
                ucs = AStar(self)
                if ucs.a_star_algorithm():
                    break
            else:
                print("Invalid move")
                continue

            self.printtheboard()

    def next_step(self):
        print("Your valid next steps are:")
        next_steps = []
        zzz = []

        for x in range(self.n):
            for y in range(self.n):
                if self.board[x][y] not in {"X", "GR", "GB", "GY", "GC", "."}:
                    zzz.append([x, y])

        for i in zzz:
            if self.can_move_up(i[0], i[1]):
                new_game = self.move(-1, 0)
                if tuple(map(tuple, new_game.board)):
                    next_steps.append(new_game)

            if self.can_move_down(i[0], i[1]):
                new_game = self.move(1, 0)
                if tuple(map(tuple, new_game.board)):
                    next_steps.append(new_game)

            if self.can_move_right(i[0], i[1]):
                new_game = self.move(0, 1)
                if tuple(map(tuple, new_game.board)):
                    next_steps.append(new_game)

            if self.can_move_left(i[0], i[1]):
                new_game = self.move(0, -1)
                if tuple(map(tuple, new_game.board)):
                    next_steps.append(new_game)
        print(len(next_steps))
        return next_steps

    def remaining_steps_to_win(self):
        goals = {"GY", "GR", "GB", "GC"}
        colored_squares = {"Y", "R", "B", "C"}
        total_distance = 0

        for x in range(self.n):
            for y in range(self.n):
                if self.board[x][y] in colored_squares:
                    closest_goal_distance = float("inf")
                    for i in range(self.n):
                        for j in range(self.n):
                            if self.board[i][j] in goals:
                                distance = abs(x - i) + abs(y - j)
                                closest_goal_distance = min(
                                    closest_goal_distance, distance
                                )
                    total_distance += closest_goal_distance

        return total_distance

import tkinter as tk

class NQueenCSPGUI:
    def __init__(self, size):
        self.size = size
        self.board = [[0] * size for _ in range(size)]

        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, width=500, height=500)
        self.canvas.pack()

        self.draw_board()
        self.solve_n_queen_csp()

        self.window.mainloop()

    def draw_board(self):
        square_size = 500 // self.size

        for row in range(self.size):
            for col in range(self.size):
                x1, y1 = col * square_size, row * square_size
                x2, y2 = x1 + square_size, y1 + square_size

                color = "white" if (row + col) % 2 == 0 else "gray"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def is_safe(self, row, col):
        for i in range(col):
            if self.board[row][i] == 1:
                return False
            for j in range(self.size):
                if self.board[j][i] == 1 and abs(row - j) == abs(col - i):
                    return False
        return True

    def solve_util(self, col):
        if col >= self.size:
            return True

        for row in range(self.size):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                if self.solve_util(col + 1):
                    return True
                self.board[row][col] = 0

        return False

    def solve_n_queen_csp(self):
        if not self.solve_util(0):
            print("No solution exists.")
            return

        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == 1:
                    x, y = col * (500 // self.size), row * (500 // self.size)
                    self.canvas.create_text(x + 15, y + 15, text="♛", font=("Arial", 20))

if __name__ == "__main__":
    size = 6  # Change this value to customize the board size
    NQueenCSPGUI(size)

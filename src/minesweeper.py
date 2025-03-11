import random

class Minesweeper:
    def __init__(self, rows: int, cols: int, num_mines: int):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.board = [["" for _ in range(cols)] for _ in range(rows)]
        self.mines = set()
        self.revealed = set()
        self.place_mines()

    def place_mines(self):
        """ Place aléatoirement des mines sur le plateau """
        while len(self.mines) < self.num_mines:
            r, c = random.randint(0, self.rows - 1), random.randint(0, self.cols - 1)
            if (r, c) not in self.mines:
                self.mines.add((r, c))
                self.board[r][c] = '💣'
        
        for r, c in self.mines:
            for i in range(r-1, r+2):
                for j in range(c-1, c+2):
                    if 0 <= i < self.rows and 0 <= j < self.cols and self.board[i][j] != '💣':
                        if self.board[i][j] == '':
                            self.board[i][j] = 1
                        else:
                            self.board[i][j] += 1
    
    def reveal(self, row: int, col: int) -> str:
        """ Révèle une case sur le plateau """
        pass
    
    def get_board(self) -> list:
        """ Retourne l'état actuel du plateau """
        pass
    
    def is_winner(self) -> bool:
        """ Vérifie si le joueur a gagné """
        pass
    
    def restart(self) -> None:
        """ Redémarre le jeu avec les mêmes paramètres """
        self.__init__(self.rows, self.cols, self.num_mines)
        
def test_place_mines():
    game = minesweeper.Minesweeper(3, 3, 2)
    game.place_mines()
    assert len(game.mines) == 2
        
    
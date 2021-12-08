from tkinter import *
from tkinter import messagebox
import random   
class Board:
    bg_color = {

        '2': '#eee4da',
        '4': '#ede0c8',
        '8': '#edc850',
        '16': '#ff9900',
        '32': '#f67c5f',
        '64': '#f65e3b',
        '128': '#edcf72',
        '256': '#edcc61',
        '512': '#f2b179',
        '1024': '#f59563',
        '2048': '#edc22e',
    }
    color = {
        '2': '#776e65',
        '4': '#f9f6f2',
        '8': '#f9f6f2',
        '16': '#f9f6f2',
        '32': '#f9f6f2',
        '64': '#f9f6f2',
        '128': '#f9f6f2',
        '256': '#f9f6f2',
        '512': '#776e65',
        '1024': '#f9f6f2',
        '2048': '#f9f6f2',
    }
    def __init__(self):
        self.n = 4
        self.game_panel = Tk()
        self.game_panel.title('2048 Game using Tkinter')
        self.GameZone = Frame(self.game_panel, bg='azure3')
        self.gridCell = [[0] * 4 for i in range(4)]
        self.board = []
        for i in range(4):
            rows = []
            for j in range(4):
                l = Label(self.GameZone, text='', bg='azure4',
                          font=('arial', 22, 'bold'), width=4, height=2)
                l.grid(row=i, column=j, padx=7, pady=7)
                rows.append(l)
            self.board.append(rows)
        self.GameZone.grid()
    def Shift_Opposite(self):
        for ind in range(4):
            i = 0
            j = 3
            while (i < j):
                (self.gridCell[ind][i], self.gridCell[ind][j]) =( self.gridCell[ind][j], self.gridCell[ind][i])
                i += 1
                j -= 1    
    def Grid_Compress(self):
        temp = [[0] * 4 for i in range(4)]
        for i in range(4):
            cnt = 0
            for j in range(4):
                if self.gridCell[i][j] != 0:
                    temp[i][cnt] = self.gridCell[i][j]
                    cnt += 1
        self.gridCell = temp
    def Grid_Merge(self):
        for i in range(4):
            for j in range(4 - 1):
                if self.gridCell[i][j] == self.gridCell[i][j + 1] and self.gridCell[i][j] != 0:
                    self.gridCell[i][j] *= 2
                    self.gridCell[i][j + 1] = 0
                    self.score += self.gridCell[i][j]
                    

class Game:
    def __init__(self, gameWindow):
        self.gameWindow = gameWindow
        self.end = False
        self.won = False
    #

    def start(self):
        # self.gameWindow.random_cell()
        # self.gameWindow.random_cell()
        # self.gameWindow.grid_paint()
        self.gameWindow.game_panel.bind('<Key>', True)
        self.gameWindow.game_panel.mainloop()   

gameWindow = Board()
game2048 = Game(gameWindow)
game2048.start()     
    

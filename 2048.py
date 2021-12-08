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
        self.board = []
        self.gridCell = [[0] * 4 for i in range(4)]
        self.compress = False
        self.merge = False
        self.moved = False
        self.score = 0

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

    def transpose(self):
        self.gridCell = [list(t) for t in zip(*self.gridCell)]

    def Grid_Compress(self):
        self.compress = False
        temp = [[0] * 4 for i in range(4)]
        for i in range(4):
            cnt = 0
            for j in range(4):
                if self.gridCell[i][j] != 0:
                    temp[i][cnt] = self.gridCell[i][j]
                    if cnt != j:
                        self.compress = True
                    cnt += 1
        self.gridCell = temp

    def Grid_Merge(self):
        self.merge = False
        for i in range(4):
            for j in range(4 - 1):
                if self.gridCell[i][j] == self.gridCell[i][j + 1] and self.gridCell[i][j] != 0:
                    self.gridCell[i][j] *= 2
                    self.gridCell[i][j + 1] = 0
                    self.score += self.gridCell[i][j]
                    self.merge = True

    def random_cell(self):
        cells = []
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j] == 0:
                    cells.append((i, j))
        curr = random.choice(cells)
        i = curr[0]
        j = curr[1]
        lst = [2, 4]
        self.gridCell[i][j] = random.choice(lst)

    def can_merge(self):
        for i in range(4):
            for j in range(3):
                if self.gridCell[i][j] == self.gridCell[i][j + 1]:
                    return True

        for i in range(3):
            for j in range(4):
                if self.gridCell[i + 1][j] == self.gridCell[i][j]:
                    return True
        return False

    def grid_paint(self):
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j] == 0:
                    self.board[i][j].config(text='', bg='azure4')
                else:
                    self.board[i][j].config(text=str(self.gridCell[i][j]),
                                            bg=self.bg_color.get(str(self.gridCell[i][j])),
                                            fg=self.color.get(str(self.gridCell[i][j])))
    def quit(self):
        self.game_panel.destroy()

class Game:
    def __init__(self, gameWindow):
        self.gameWindow = gameWindow
        self.end = False
        self.won = False
    #

    def start(self):
        self.gameWindow.random_cell()
        self.gameWindow.random_cell()
        self.gameWindow.grid_paint()
        self.gameWindow.game_panel.bind('<Key>', self.link_keys)
        self.gameWindow.game_panel.mainloop()

    def link_keys(self, event):
        if self.end or self.won:
            return

        self.gameWindow.compress = False
        self.gameWindow.merge = False
        self.gameWindow.moved = False

        presed_key = event.keysym

        if presed_key == 'Up' or presed_key == '3' or presed_key == 'w'  :
            self.gameWindow.transpose()
            self.gameWindow.Grid_Compress()
            self.gameWindow.Grid_Merge()
            self.gameWindow.moved = self.gameWindow.compress or self.gameWindow.merge
            self.gameWindow.Grid_Compress()
            self.gameWindow.transpose()

        elif presed_key == 'Down' or presed_key == '4' or presed_key == 's':
            self.gameWindow.transpose()
            self.gameWindow.Shift_Opposite()
            self.gameWindow.Grid_Compress()
            self.gameWindow.Grid_Merge()
            self.gameWindow.moved = self.gameWindow.compress or self.gameWindow.merge
            self.gameWindow.Grid_Compress()
            self.gameWindow.Shift_Opposite()
            self.gameWindow.transpose()

        elif presed_key == 'Left'or presed_key == '1' or presed_key == 'a' :
            self.gameWindow.Grid_Compress()
            self.gameWindow.Grid_Merge()
            self.gameWindow.moved = self.gameWindow.compress or self.gameWindow.merge
            self.gameWindow.Grid_Compress()

        elif presed_key == 'Right'or presed_key == '2' or presed_key == 'd':
            self.gameWindow.Shift_Opposite()
            self.gameWindow.Grid_Compress()
            self.gameWindow.Grid_Merge()
            self.gameWindow.moved = self.gameWindow.compress or self.gameWindow.merge
            self.gameWindow.Grid_Compress()
            self.gameWindow.Shift_Opposite()
        # elif presed_key=='q':
        #     self.end = True
        #     txt = "Game Over \n  your score {}"
        #     score = gameWindow.score
        #     messagebox.showinfo('2048', txt.format(score))
        #     gameWindow.quit()


        else:
            pass

        self.gameWindow.grid_paint()
        print(self.gameWindow.score)

        flag = 0
        for i in range(4):
            for j in range(4):
                if (self.gameWindow.gridCell[i][j] == 2048):
                    flag = 1
                    break

        if (flag == 1):  # found 2048
            self.won = True
            messagebox.showinfo('2048', message='Congratulation You Wonnn!!')
            print("You won")
            return

        for i in range(4):
            for j in range(4):
                if self.gameWindow.gridCell[i][j] == 0:
                    flag = 1
                    break

        if not (flag or self.gameWindow.can_merge()):
            self.end = True
            txt="Game Over \n  your score {}"
            score=gameWindow.score
            messagebox.showinfo('2048', txt.format(score))


            print("Over")

        if self.gameWindow.moved:
            self.gameWindow.random_cell()

        self.gameWindow.grid_paint()


gameWindow = Board()
game2048 = Game(gameWindow)
game2048.start()
    

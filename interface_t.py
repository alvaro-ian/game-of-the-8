from tkinter import *
from search import *
from game import *
import time

class Application:
    def __init__(self, master=None):
        fonte_p = ("Century Gothic", "15", "bold")
        fonte_b = ("Century Gothic", "10", "bold")
        n = 5
        background_a = "grey70"
        background_b = "grey20"
        foreground_a = "grey5"
        foreground_b = "grey99"
        butt = "grey35"
        jog = [[1, 2, 3], [4, 5, 6], [7, 8, ]]
        self.widget1 = Frame(master)
        self.widget1["pady"] = 20
        self.widget1["bg"] = background_b
        self.widget1.pack()

        self.widget2 = Frame(master)
        self.widget2["bg"] = background_b
        self.widget2.pack()

        self.widget3 = Frame(master)
        self.widget3["bg"] = background_b
        self.widget3.pack()

        self.widget4 = Frame(master)
        self.widget4["bg"] = background_b
        self.widget4.pack()

        self.text = Label(self.widget1,text="Jogo dos 8", font=fonte_p)
        self.text["bg"] = background_b
        self.text["fg"] = foreground_b
        self.text.grid(row=4, column=6)

        self.m00 = Entry(self.widget2, justify='center', width= n)
        self.m00["bg"] = background_a
        self.m00["fg"] = foreground_a

        self.m01 = Entry(self.widget2, justify='center', width= n)
        self.m01["bg"] = background_a
        self.m01["fg"] = foreground_a

        self.m02 = Entry(self.widget2, justify='center', width= n)
        self.m02["bg"] = background_a
        self.m02["fg"] = foreground_a

        self.m10 = Entry(self.widget3, justify='center', width= n)
        self.m10["bg"] = background_a
        self.m10["fg"] = foreground_a

        self.m11 = Entry(self.widget3, justify='center', width= n)
        self.m11["bg"] = background_a
        self.m11["fg"] = foreground_a

        self.m12 = Entry(self.widget3, justify='center', width= n)
        self.m12["bg"] = background_a
        self.m12["fg"] = foreground_a

        self.m20 = Entry(self.widget4, justify='center', width= n)
        self.m20["bg"] = background_a
        self.m20["fg"] = foreground_a

        self.m21 = Entry(self.widget4, justify='center', width= n)
        self.m21["bg"] = background_a
        self.m21["fg"] = foreground_a

        self.m22 = Entry(self.widget4, justify='center', width= n)
        self.m22["bg"] = background_a
        self.m22["fg"] = foreground_a

        self.m00.grid(row=5, column=5)
        self.m01.grid(row=5, column=6)
        self.m02.grid(row=5, column=7)
        self.m10.grid(row=6, column=5)
        self.m11.grid(row=6, column=6)
        self.m12.grid(row=6, column=7)
        self.m20.grid(row=7, column=5)
        self.m21.grid(row=7, column=6)
        self.m22.grid(row=7, column=7)

        self.depth_label = Label(text="Profundidade: ")
        self.depth_label['bg'] = background_b
        self.depth_label['fg'] = foreground_b
        self.depth_label.place(relx=0.5, rely=0.45, anchor=CENTER)

        self.bprof = Button()
        self.bprof["text"] = "Busca Profundidade"
        self.bprof["font"] = fonte_b
        self.bprof["bg"] = butt
        self.bprof["width"] = 17
        self.bprof["command"] = self.BuscaProfundidade
        self.bprof.place(relx=0.5, rely=0.55, anchor=CENTER)

        self.blargura = Button()
        self.blargura["text"] = "Busca Largura"
        self.blargura["font"] = fonte_b
        self.blargura["bg"] = butt
        self.blargura["width"] = 17
        self.blargura["command"] = self.BuscaLargura
        self.blargura.place(relx=0.5, rely=0.65, anchor=CENTER)

        self.bgulosa = Button()
        self.bgulosa["text"] = "Busca Gulosa"
        self.bgulosa["font"] = fonte_b
        self.bgulosa["bg"] = butt
        self.bgulosa["width"] = 17
        self.bgulosa["command"] = self.BuscaGulosa
        self.bgulosa.place(relx=0.5, rely=0.75, anchor=CENTER)

        self.bprof = Button()
        self.bprof["text"] = "Busca A*"
        self.bprof["font"] = fonte_b
        self.bprof["bg"] = butt
        self.bprof["activebackground"] = "grey10"
        self.bprof["width"] = 17
        self.bprof["command"] = self.BuscaAEstrela
        self.bprof.place(relx=0.5, rely=0.85, anchor=CENTER)

    def get_table(self):
        table = [[], [], []]
        x = self.m00.get()
        if x == '':
            x = 'b'
        else:
            x = int(x)
        table[0].append(x)
        x = self.m01.get()
        if x == '':
            x = 'b'
        else:
            x = int(x)
        table[0].append(x)
        x = self.m02.get()
        if x == '':
            x = 'b'
        else:
            x = int(x)
        table[0].append(x)
        x = self.m10.get()
        if x == '':
            x = 'b'
        else:
            x = int(x)
        table[1].append(x)
        x = self.m11.get()
        if x == '':
            x = 'b'
        else:
            x = int(x)
        table[1].append(x)
        x = self.m12.get()
        if x == '':
            x = 'b'
        else:
            x = int(x)
        table[1].append(x)
        x = self.m20.get()
        if x == '':
            x = 'b'
        else:
            x = int(x)
        table[2].append(x)
        x = self.m21.get()
        if x == '':
            x = 'b'
        else:
            x = int(x)
        table[2].append(x)
        x = self.m22.get()
        if x == '':
            x = 'b'
        else:
            x = int(x)
        table[2].append(x)
        return table

    def set_table(self, table):
        self.m00.delete(0, 'end')
        self.m00.insert(INSERT, str(table[0][0]))
        self.m01.delete(0, 'end')
        self.m01.insert(INSERT, str(table[0][1]))
        self.m02.delete(0, 'end')
        self.m02.insert(INSERT, str(table[0][2]))
        self.m10.delete(0, 'end')
        self.m10.insert(INSERT, str(table[1][0]))
        self.m11.delete(0, 'end')
        self.m11.insert(INSERT, str(table[1][1]))
        self.m12.delete(0, 'end')
        self.m12.insert(INSERT, str(table[1][2]))
        self.m20.delete(0, 'end')
        self.m20.insert(INSERT, str(table[2][0]))
        self.m21.delete(0, 'end')
        self.m21.insert(INSERT, str(table[2][1]))
        self.m22.delete(0, 'end')
        self.m22.insert(INSERT, str(table[2][2]))
        root.update()

    def BuscaProfundidade(self):
        table = self.get_table()
        print(table)
        initial_state = StateNode(Game8(table), None, None, 0, 0)
        path = depth_first_search(initial_state)
        for state in path:
            self.depth_label['text'] = 'Profundidade: ' + str(state.depth)
            b = state.game.get_b_position()
            state.game.table[b[0]][b[1]] = ''
            self.set_table(state.game.table)
            state.game.show_table()
            time.sleep(1)

    def BuscaLargura(self):
        table = self.get_table()
        print(table)
        initial_state = StateNode(Game8(table), None, None, 0, 0)
        path = breadth_first_search(initial_state)
        for state in path:
            self.depth_label['text'] = 'Profundidade: ' + str(state.depth)
            b = state.game.get_b_position()
            state.game.table[b[0]][b[1]] = ''
            self.set_table(state.game.table)
            state.game.show_table()
            time.sleep(1)

    def BuscaGulosa(self):
        table = self.get_table()
        print(table)
        initial_state = StateNode(Game8(table), None, None, 0, 0)
        path = greedy_search(initial_state)
        for state in path:
            self.depth_label['text'] = 'Profundidade: ' + str(state.depth)
            b = state.game.get_b_position()
            state.game.table[b[0]][b[1]] = ''
            self.set_table(state.game.table)
            state.game.show_table()
            time.sleep(1)

    def BuscaAEstrela(self):
        table = self.get_table()
        print(table)
        initial_state = StateNode(Game8(table), None, None, 0, 0)
        path = a_star_search(initial_state)
        for state in path:
            self.depth_label['text'] = 'Profundidade: ' + str(state.depth)
            b = state.game.get_b_position()
            state.game.table[b[0]][b[1]] = ''
            self.set_table(state.game.table)
            state.game.show_table()
            time.sleep(1)


root = Tk()
root["background"] = "grey20"
root.geometry("200x350")
Application(root)
root.mainloop()
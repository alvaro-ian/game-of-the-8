from tkinter import *

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
        self.m00.insert(END, jog[0][0])

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

        self.blargura = Button()
        self.blargura["text"] = "Busca Largura"
        self.blargura["font"] = fonte_b
        self.blargura["bg"] = butt
        self.blargura["width"] = 15
        self.blargura["command"] = self.BuscaLargura
        self.blargura.place(relx=0.5, rely=0.65, anchor=CENTER)

        self.bprof = Button()
        self.bprof["text"] = "Busca Profundidade"
        self.bprof["font"] = fonte_b
        self.bprof["bg"] = butt
        self.bprof["activebackground"] = "grey10"
        self.bprof["width"] = 17
        self.bprof["command"] = self.BuscaProfundidade
        self.bprof.place(relx=0.5, rely=0.75, anchor=CENTER)


    def BuscaLargura(self):
        self.m00.delete(0, 'end')
        self.m00.insert(INSERT, "OPA")
        root.update()
        self.m00.after(700, self.m00.delete(0, 'end'))

    def BuscaProfundidade(self):
        w = int(self.m00.get())
        self.m00.delete(0, 'end')
        w+=1
        self.m01.insert(INSERT, w)
        root.update()
        #self.m00.after(700, self.m00.delete(0, 'end'))


root = Tk()
root["background"] = "grey20"
root.geometry("200x350")
Application(root)
root.mainloop()
from tkinter import *
import tkinter.ttk as t
from tkinter.ttk import Button

import matplotlib as mp
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.animation as anim
from matplotlib import style as st
from matplotlib.figure import Figure

MAX_WIDTH = 1200
MAX_HEIGHT = 600

mp.use("TkAgg")
st.use("ggplot")


def fonts():

    return {"LARGE_FONT": ("Verdana", 12), "SMALL_FONT": ("Verdana", 9),"TINY_FONT":('Roboto',7)}


coordinates = [[], []]

f = Figure(figsize=(4.5, 4.5), dpi=100)
a = f.add_subplot(111)


def add_coordinate(X, Y):
    coordinates[0].append(X)
    coordinates[1].append(Y)


def animate_point_scatter(i):
    a.clear()
    a.scatter(coordinates[0], coordinates[1])


def CBB_change(event, cbb, cbb_index, fun, cur):
    fun.show_frame(cbb_index[cbb.current()])
    cbb.current(cur)


class MarkoGebra(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        Tk.wm_title(self, "MarkoGebra")
        Tk.minsize(self, width=MAX_WIDTH, height=MAX_HEIGHT)
        Tk.maxsize(self, width=MAX_WIDTH, height=MAX_HEIGHT)
        container = Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Begin, StatsPieInputPage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Begin)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="MarkoGebra", font=fonts()["LARGE_FONT"])
        label.pack(pady=10, padx=10)
        Begin = t.Button(self, text="Začít",
                         command=lambda: controller.show_frame(Begin))

        Begin.place(bordermode=OUTSIDE, width=MAX_WIDTH - MAX_WIDTH * 0.80, height=MAX_HEIGHT - MAX_HEIGHT * 0.90,
                    x=MAX_WIDTH - MAX_WIDTH * 0.99, y=MAX_HEIGHT - MAX_HEIGHT * 0.93)
        Settings = t.Button(self, text="Nastavení",
                            command=lambda: print("settingss"))

        Settings.place(bordermode=OUTSIDE, width=MAX_WIDTH - MAX_WIDTH * 0.80, height=MAX_HEIGHT - MAX_HEIGHT * 0.90,
                       x=MAX_WIDTH - MAX_WIDTH * 0.99, y=MAX_HEIGHT - MAX_HEIGHT * 0.83)

        combo = t.Combobox(self, values=["jo", "ne", "test"], state="readonly")
        combo.current(0)
        combo.place(x=600, y=300)


class Begin(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="MarkoGebra - Matematické", font=fonts()["LARGE_FONT"])
        label.pack(pady=10, padx=10)
        self.controller = controller
        self.CBB_INDEXES = [Begin, StatsPieInputPage]
        # Graf
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().place(bordermode=OUTSIDE, x=MAX_WIDTH - 470, y=MAX_HEIGHT - 470)
        # Combobox - 1
        self.CBB1 = t.Combobox(self, values=["Matematické Grafování", "Statistické Grafování", "Náhodný Šum"],
                               state="readonly")

        self.CBB1.place(bordermode=OUTSIDE, width=MAX_WIDTH * .15, height=MAX_HEIGHT * .05,
                        x=MAX_WIDTH * .01, y=MAX_HEIGHT * .15)

        self.CBB1.bind('<<ComboboxSelected>>',
                       lambda event, cbb=self.CBB1, cbb_index=self.CBB_INDEXES, fun=controller, cur=0: CBB_change(event,
                                                                                                                  cbb,
                                                                                                                  cbb_index,
                                                                                                                  fun,
                                                                                                                  cur))
        self.CBB1.current(0)
        #Combobox - 2
        self.CBB2 = t.Combobox(self, values=["1", "2", "3"],
                               state="readonly")
        self.CBB2.current(0)
        self.CBB2.place(bordermode=OUTSIDE, width=MAX_WIDTH * .15, height=MAX_HEIGHT * .05,
                        x=MAX_WIDTH * .01, y=MAX_HEIGHT * .2)
        #TODO input frames
        self.container = Frame(self,width=MAX_WIDTH*.4,height=MAX_HEIGHT*.2,bg="red")
        self.container.place(x=MAX_WIDTH*.01,y=MAX_HEIGHT*.25)

        self.input_frames = {}

        for F in [PointMathInputs,FunctionMathInputs]:
            frame = F(self.container, self)

            self.input_frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_inputs(PointMathInputs)

        #TODO tabulka
        self.Table = Frame(self,bg="blue",width=200,height=200)
        self.Table.place(bordermode=OUTSIDE,x=20,y=300)
        #objekty tabulky
        self.Table.Button = t.Button(self.Table,text="test")
        self.Table.Button.place(bordermode=OUTSIDE,x=10,y=10)
        #TODO konec tabulky

        # zpět, nápověda
        Back = t.Button(self, text="Zpět",
                        command=lambda: controller.show_frame(StartPage))
        Back.place(bordermode=OUTSIDE, width=MAX_WIDTH * 0.08, height=MAX_HEIGHT * 0.05,
                   x=MAX_WIDTH * 0.84, y=0)
        Hint = t.Button(self, text="Nápověda",
                        command=lambda: print("Nápověda"))
        Hint.place(bordermode=OUTSIDE, width=MAX_WIDTH * 0.08, height=MAX_HEIGHT * 0.05,
                   x=MAX_WIDTH * 0.92, y=0)


    def show_inputs(self,cont):
        frame = self.input_frames[cont]
        frame.tkraise()



class PointMathInputs(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self, parent,bg="red")



        # Combobox - 2
        self.CBB2 = t.Combobox(self, values=["1", "2", "3"],
                               state="readonly")
        self.CBB2.current(0)
        self.CBB2.place(bordermode=OUTSIDE, width=MAX_WIDTH * .15, height=MAX_HEIGHT * .05,
                        x=MAX_WIDTH * .01, y=MAX_HEIGHT * .2)
        # TODO Uživatelský vstup

        # labely
        self.labelX = t.Label(self, text="X:", font=fonts()["SMALL_FONT"])
        self.labelY = t.Label(self, text="Y:", font=fonts()["SMALL_FONT"])
        self.labelX.place(bordermode=OUTSIDE, x=MAX_WIDTH * .01, y=MAX_HEIGHT * .3, height=MAX_HEIGHT * .05)
        self.labelY.place(bordermode=OUTSIDE, x=MAX_WIDTH * .16, y=MAX_HEIGHT * .3, height=MAX_HEIGHT * .05)

        # entryes
        self.EntryX = t.Entry(self, justify="center")
        self.EntryY = t.Entry(self, justify="center")
        self.EntryX.place(bordermode=OUTSIDE, x=MAX_WIDTH * .025, y=MAX_HEIGHT * .3,
                          width=MAX_WIDTH * .135, height=MAX_HEIGHT * .05)
        self.EntryY.place(bordermode=OUTSIDE, x=MAX_WIDTH * .175, y=MAX_HEIGHT * .3,
                          width=MAX_WIDTH * .135, height=MAX_HEIGHT * .05)
        # place button
        self.placeButton = t.Button(self, text="Vložit",
                                    command=lambda: add_coordinate(int(self.EntryX.get()), int(self.EntryY.get())))
        self.placeButton.place(bordermode=OUTSIDE, x=MAX_WIDTH * .31, y=MAX_HEIGHT * .3,
                               width=MAX_WIDTH * .1, height=MAX_HEIGHT * .05)
        # TODO Konec uživatelského vstupu


class FunctionMathInputs(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self, parent)



        # Combobox - 2
        self.CBB2 = t.Combobox(self, values=["1", "2", "3"],
                               state="readonly")
        self.CBB2.current(0)
        self.CBB2.place(bordermode=OUTSIDE, width=MAX_WIDTH * .15, height=MAX_HEIGHT * .05,
                        x=MAX_WIDTH * .01, y=MAX_HEIGHT * .2)
        # TODO Uživatelský vstup

        # labely
        self.labelX = t.Label(self, text="X:", font=fonts()["SMALL_FONT"])
        self.labelY = t.Label(self, text="Y:", font=fonts()["SMALL_FONT"])
        self.labelX.place(bordermode=OUTSIDE, x=MAX_WIDTH * .01, y=MAX_HEIGHT * .3, height=MAX_HEIGHT * .05)
        self.labelY.place(bordermode=OUTSIDE, x=MAX_WIDTH * .16, y=MAX_HEIGHT * .3, height=MAX_HEIGHT * .05)

        # entryes
        self.EntryX = t.Entry(self, justify="center")
        self.EntryY = t.Entry(self, justify="center")
        self.EntryX.place(bordermode=OUTSIDE, x=MAX_WIDTH * .025, y=MAX_HEIGHT * .3,
                          width=MAX_WIDTH * .135, height=MAX_HEIGHT * .05)
        self.EntryY.place(bordermode=OUTSIDE, x=MAX_WIDTH * .175, y=MAX_HEIGHT * .3,
                          width=MAX_WIDTH * .135, height=MAX_HEIGHT * .05)
        # place button
        self.placeButton = t.Button(self, text="Vložit",
                                    command=lambda: add_coordinate(int(self.EntryX.get()), int(self.EntryY.get())))
        self.placeButton.place(bordermode=OUTSIDE, x=MAX_WIDTH * .31, y=MAX_HEIGHT * .3,
                               width=MAX_WIDTH * .1, height=MAX_HEIGHT * .05)

        # TODO Konec uživatelského vstupu





class StatsPieInputPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="MarkoGebra - Statistické", font=fonts()["LARGE_FONT"])
        label.pack(pady=10, padx=10)
        self.CBB_INDEXES = [Begin, StatsPieInputPage]
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().place(bordermode=OUTSIDE, x=MAX_WIDTH - 470, y=MAX_HEIGHT - 470)

        self.CBB1 = t.Combobox(self, values=["Matematické Grafování", "Statistické Grafování", "Náhodný Šum"],
                               state="readonly")

        self.CBB1.place(bordermode=OUTSIDE, width=MAX_WIDTH * .15, height=MAX_HEIGHT * .05,
                        x=MAX_WIDTH * .01, y=MAX_HEIGHT * .15)

        self.CBB1.bind('<<ComboboxSelected>>',
                       lambda event, cbb=self.CBB1, cbb_index=self.CBB_INDEXES, fun=controller, cur=1: CBB_change(event,
                                                                                                                  cbb,
                                                                                                                  cbb_index,
                                                                                                                  fun,
                                                                                                                  cur))
        self.CBB1.current(1)

        self.CBB2 = t.Combobox(self, values=["1", "2", "3"],
                               state="readonly")
        self.CBB2.current(0)
        self.CBB2.place(bordermode=OUTSIDE, width=MAX_WIDTH * .15, height=MAX_HEIGHT * .05,
                        x=MAX_WIDTH * .01, y=MAX_HEIGHT * .2)

        self.x_text = Label(self, text="Hodnota x", font=fonts()["SMALL_FONT"])
        self.y_text = Label(self, text="Hodnota y", font=fonts()["SMALL_FONT"])

        self.x_text.place(bordermode=OUTSIDE, height=MAX_HEIGHT * 0.05, width=MAX_WIDTH * 0.1,
                          x=MAX_WIDTH * 0.01, y=MAX_HEIGHT * 0.35)
        self.y_text.place(bordermode=OUTSIDE, height=MAX_HEIGHT * 0.05, width=MAX_WIDTH * 0.1,
                          x=MAX_WIDTH * 0.11, y=MAX_HEIGHT * 0.35)

        self.x_entry = t.Entry(self, justify="center")
        self.y_entry = t.Entry(self, justify="center")

        self.x_entry.place(bordermode=OUTSIDE, height=MAX_HEIGHT * 0.05, width=MAX_WIDTH * 0.1,
                           x=MAX_WIDTH * 0.01, y=MAX_HEIGHT * 0.4)

        self.y_entry.place(bordermode=OUTSIDE, height=MAX_HEIGHT * 0.05, width=MAX_WIDTH * 0.1,
                           x=MAX_WIDTH * 0.11, y=MAX_HEIGHT * 0.4)

        self.add_coord = t.Button(self, text="Přidat bod",
                                  command=lambda: add_coordinate(int(self.x_entry.get()), int(self.y_entry.get())))
        self.add_coord.place(bordermode=OUTSIDE, height=MAX_HEIGHT * 0.05, width=MAX_WIDTH * 0.1,
                             x=MAX_WIDTH * 0.21, y=MAX_HEIGHT * 0.4)

        Back = t.Button(self, text="Zpět",
                        command=lambda: controller.show_frame(StartPage))
        Back.place(bordermode=OUTSIDE, width=MAX_WIDTH * 0.08, height=MAX_HEIGHT * 0.05,
                   x=MAX_WIDTH * 0.84, y=0)
        Hint = t.Button(self, text="Nápověda",
                        command=lambda: print("Nápověda"))
        Hint.place(bordermode=OUTSIDE, width=MAX_WIDTH * 0.08, height=MAX_HEIGHT * 0.05,
                   x=MAX_WIDTH * 0.92, y=0)


app = MarkoGebra()

ani = anim.FuncAnimation(f, animate_point_scatter, interval=1000)
app.mainloop()

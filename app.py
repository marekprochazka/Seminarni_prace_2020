from tkinter import *
import tkinter.ttk as t
from tkinter.ttk import Button

import matplotlib as mp
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.animation as anim
from matplotlib import style as st
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

MAX_WIDTH = 1200
MAX_HEIGHT = 600

mp.use("TkAgg")
st.use("ggplot")
import numpy as np


def fonts():
    return {"LARGE_FONT": ("Verdana", 12), "SMALL_FONT": ("Verdana", 9), "TINY_FONT": ('Roboto', 7)}


coordinates_scatter = []
coordinates_plot = []
coordinates_all_list = []

# f = plt.figure(figsize=(4.5, 4.5), dpi=100)
f = Figure(figsize=(4.5, 4.5), dpi=100)
a = f.add_subplot(111)
a.axis("equal")
a.set_aspect("equal")

a.set_ylim(-20, 20)


def animate_graphs(i):
    a.clear()
    for coord in coordinates_scatter:
        a.scatter(coord[0], coord[1])
    for coord in coordinates_plot:
        x = coord[0]
        y = eval(coord[1])

        for limit in range(len(y)):
            if y[limit] > 30 or y[limit] < -30:
                y[limit] = None
        a.plot(x, y)


class MarkoGebra(Tk):
    def __init__(self):
        Tk.__init__(self)
        Tk.wm_title(self, "MarkoGebra")
        Tk.minsize(self, width=MAX_WIDTH, height=MAX_HEIGHT)
        Tk.maxsize(self, width=MAX_WIDTH, height=MAX_HEIGHT)

        self.input_frames = (ScatterFrame, FuncFrame)

        self.SetupContainer = t.Frame(self, width=MAX_WIDTH * .4, height=MAX_HEIGHT)

        self.SetupContainer.pack(side="top", fill="both", expand=True)

        self.SetupContainer.grid_rowconfigure(0, weight=1)
        self.SetupContainer.grid_columnconfigure(0, weight=1)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().place(bordermode=OUTSIDE, x=MAX_WIDTH - 470, y=MAX_HEIGHT - 470)

        # Combobox - 1

        self.CBB1 = t.Combobox(self, values=["Matematické Grafování", "Statistické Grafování", "Náhodný Šum"],
                               state="readonly")

        self.CBB1.place(bordermode=OUTSIDE, width=MAX_WIDTH * .15, height=MAX_HEIGHT * .05,
                        x=MAX_WIDTH * .01, y=MAX_HEIGHT * .15)

        # self.CBB1.bind('<<ComboboxSelected>>',lambda event: self.show_Setup_Frame(self.pages_tuple[self.CBB1.current()]))

        self.CBB1.current(0)
        # Combobox - 2
        self.CBB2 = t.Combobox(self, values=["1", "2", "3"],
                               state="readonly")
        self.CBB2.bind('<<ComboboxSelected>>',
                       lambda event: self.show_Setup_Frame(self.input_frames[self.CBB2.current()]))
        self.CBB2.current(0)
        self.CBB2.place(bordermode=OUTSIDE, width=MAX_WIDTH * .15, height=MAX_HEIGHT * .05,
                        x=MAX_WIDTH * .01, y=MAX_HEIGHT * .2)

        """
        {{ relative input part }}
        """

        # TODO scrollable table part
        self.Table_container = t.Frame(self)
        self.canvas = Canvas(self.Table_container)
        self.scrollbar = t.Scrollbar(self.Table_container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = t.Frame(self.canvas)
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.update_table()
        for i in range(5):
            Frame(self.scrollable_frame).pack()

        self.Table_container.place(bordermode=OUTSIDE, x=MAX_WIDTH * .01, y=MAX_HEIGHT * .6, width=MAX_WIDTH * .4,
                                   height=MAX_HEIGHT * .3)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # open console button
        self.console =  t.Button(self, text="Konzole", command=lambda: self.console_controller())
        self.console.place(bordermode=OUTSIDE,x=MAX_WIDTH*.01,y=MAX_HEIGHT*.95,height=MAX_HEIGHT*.05,width=MAX_WIDTH*.4)

        # Frame-changing part 😉

        self.SetupFrames = {}

        self._frame = None
        self.show_Setup_Frame(ScatterFrame)

    def show_Setup_Frame(self, cont):

        new_frame = cont(self.SetupContainer, self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def add_point_scatter(self, x, y):
        global coordinates_scatter, coordinates_all_list
        if [x, y] not in coordinates_scatter:
            coordinates_scatter.append([x, y])
            coordinates_all_list.append(f"{x}:{y}")
            self.update_table()

    def add_plot_from_function(self, function):
        global coordinates_plot, coordinates_all_list
        x = np.arange(-20, 20, 0.0001)
        y = function



        checnk = True
        if len(coordinates_plot) >= 1:
            for val in coordinates_plot:
                if val[1] == y:
                    checnk = False
        if checnk:
            coordinates_plot.append([x, y])
            coordinates_all_list.append(f"f(x):{function}")

        self.update_table()

    def update_table(self):
        global coordinates_all_list

        for child in self.scrollable_frame.winfo_children():
            for child_of_child in child.winfo_children():
                child_of_child.destroy()
        counter = 0
        for index, parent in enumerate(self.scrollable_frame.winfo_children()):
            try:
                t.Button(parent, text=f"{coordinates_all_list[index]}, {counter}",
                         command=lambda: self.destroy_value(counter)).pack(side=LEFT)
                counter += 1
            except IndexError:
                pass

    def console_controller(self):
        global coordinates_all_list,coordinates_scatter,coordinates_plot
        top = Toplevel()
        top.config(background="black")
        top.wm_geometry("800x500")
        top.maxsize(width=800,height=500)
        top.minsize(width=800,height=500)
        top.title("Konzole")
        types = t.Entry(top)
        types.place(bordermode=OUTSIDE,width=700,height=20,x=0,y=480)

        #TODO Ošetřit uživatelský vstup
        def delete_value(index):
            try:
                int(coordinates_all_list[index][0])
                coordinates_scatter.remove(list(map(int, list(coordinates_all_list[index].split(":")))))
                del coordinates_all_list[index]
                self.update_table()
            except ValueError:
                for val in coordinates_plot:
                    if val[1] == coordinates_all_list[index].split(":")[1]:
                        coordinates_plot.remove(val)
                        del coordinates_all_list[index]
                        self.update_table()


        test_but = t.Button(top,text="poof",command=lambda: delete_value(0))
        test_but.pack()


class ScatterFrame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        # labely
        self.labelX = t.Label(text="X:", font=fonts()["SMALL_FONT"])
        self.labelY = t.Label(text="Y:", font=fonts()["SMALL_FONT"])
        self.labelX.place(bordermode=OUTSIDE, x=MAX_WIDTH * .01, y=MAX_HEIGHT * .3, height=MAX_HEIGHT * .05)
        self.labelY.place(bordermode=OUTSIDE, x=MAX_WIDTH * .16, y=MAX_HEIGHT * .3, height=MAX_HEIGHT * .05)

        # entryes
        self.EntryX = t.Entry(justify="center")

        self.EntryY = t.Entry(justify="center")

        self.EntryX.place(bordermode=OUTSIDE, x=MAX_WIDTH * .025, y=MAX_HEIGHT * .3,
                          width=MAX_WIDTH * .135, height=MAX_HEIGHT * .05)
        self.EntryY.place(bordermode=OUTSIDE, x=MAX_WIDTH * .175, y=MAX_HEIGHT * .3,
                          width=MAX_WIDTH * .135, height=MAX_HEIGHT * .05)
        # place button
        self.placeButton = t.Button(text="Vložit",
                                    command=lambda: controller.add_point_scatter(int(self.EntryX.get()),
                                                                                 int(self.EntryY.get())))
        self.placeButton.place(bordermode=OUTSIDE, x=MAX_WIDTH * .31, y=MAX_HEIGHT * .3,
                               width=MAX_WIDTH * .1, height=MAX_HEIGHT * .05)


class FuncFrame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        # labely
        self.labelFun = t.Label(text="f(x):", font=fonts()["SMALL_FONT"])
        self.labelFun.place(bordermode=OUTSIDE, x=MAX_WIDTH * .01, y=MAX_HEIGHT * .3, height=MAX_HEIGHT * .05)

        # entryes
        self.EntryFun = t.Entry(justify="center")

        self.EntryFun.place(bordermode=OUTSIDE, x=MAX_WIDTH * .035, y=MAX_HEIGHT * .3,
                            width=MAX_WIDTH * .275, height=MAX_HEIGHT * .05)

        # place button
        self.placeButton = t.Button(text="Odložit",
                                    command=lambda: controller.add_plot_from_function(self.EntryFun.get()))

        self.placeButton.place(bordermode=OUTSIDE, x=MAX_WIDTH * .31, y=MAX_HEIGHT * .3,
                               width=MAX_WIDTH * .1, height=MAX_HEIGHT * .05)


app = MarkoGebra()
ani = anim.FuncAnimation(f, animate_graphs, interval=1000, blit=False)
app.mainloop()

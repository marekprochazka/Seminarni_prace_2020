from tkinter import *
import tkinter.ttk as t
from tkinter.ttk import Button
import tkinter.colorchooser as col

import matplotlib as mp
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.animation as anim
from matplotlib import style as st
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

MAX_WIDTH = 1200
MAX_HEIGHT = 600

POINT_MARKERS = ['.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3', '4', '8', 's', 'p', 'P', '*', 'h', 'H', '+', 'x',
                 'X', 'D', 'd', '|', '_']
EXTRA_POINT_MARKERS = ['0 (TICKLEFT)', '1 (TICKRIGHT)', '2 (TICKUP)', '3 (TICKDOWN)', '4 (CARETLEFT)',
                       '5 (CARETRIGHT)', '6 (CARETUP)', '7 (CARETDOWN)', '8 (CARETLEFTBASE)', '9 (CARETRIGHTBASE)',
                       '10 (CARETUPBASE)', '11 (CARETDOWNBASE)', 'None', '$TEXT$']
LINE_MARKERS = ['-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted']

AVALIBLE_STYLES = ['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic', 'dark_background', 'fast',
                   'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind',
                   'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted',
                   'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk',
                   'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']

GRAPHING_METHOD = {
    "matematical": 1,
    "pie": 2,
    "bar": 3,
    "noise": 4
}

TO_ANIMATE = GRAPHING_METHOD["matematical"]

mp.use("TkAgg")
print(len(st.available))
with open("graphstyle.txt", "r") as style:
    st.use(style)

# st.use('ggplot')

import numpy as np


def fonts():
    return {"LARGE_FONT": ("Verdana", 12), "SMALL_FONT": ("Verdana", 9), "TINY_FONT": ('Roboto', 7),
            "ITALIC_SMALL": ("Verdana", 9, "italic")}


coordinates_scatter = []
coordinates_plot = []
coordinates_all_list = []

slices = [3,2,12]
cols = ["r","b","pink"]
activities = ["sleep","eat","coding"]

# f = plt.figure(figsize=(4.5, 4.5), dpi=100)
f = Figure(figsize=(4.5, 4.5), dpi=100)
a = f.add_subplot(111)
a.axis("equal")

a.set_aspect("equal")

a.set_ylim(-10, 10)

lim1 = 30
lim2 = -30




class GraphAnimation:
    def Go(self,i):
        if TO_ANIMATE == 1:
            self.animate_graphs()
        elif TO_ANIMATE ==2:
            self.animate_pie()

    def animate_graphs(i):
        a.clear()
        for coord in coordinates_scatter:
            a.scatter(coord[0], coord[1], marker=coord[2], color=coord[3], linewidths=float(coord[4]))
        for coord in coordinates_plot:
            x = coord[0]
            y = eval(coord[1])

            for limit in range(len(y)):
                if y[limit] > lim1 or y[limit] < lim2:
                    y[limit] = None
            a.plot(x, y, linestyle=coord[2], color=coord[3], linewidth=float(coord[4]))

    def animate_pie(i):
        a.clear()
        a.pie(slices, labels=activities, colors=cols)


class MarkoGebra(Tk):
    def __init__(self):
        Tk.__init__(self)
        Tk.wm_title(self, "MarkoGebra")
        Tk.minsize(self, width=MAX_WIDTH, height=MAX_HEIGHT)
        Tk.maxsize(self, width=MAX_WIDTH, height=MAX_HEIGHT)

        self.input_frames = (Mathematical, Pie, Bar, Noise)

        self.SetupContainer = t.Frame(self, width=MAX_WIDTH * .4, height=MAX_HEIGHT)

        self.SetupContainer.pack(side="top", fill="both", expand=True)

        self.SetupContainer.grid_rowconfigure(0, weight=1)
        self.SetupContainer.grid_columnconfigure(0, weight=1)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().place(bordermode=OUTSIDE, x=MAX_WIDTH - 470, y=MAX_HEIGHT - 470)

        # Combobox - 2
        self.CBB2 = t.Combobox(self, values=["Matematické", "Koláč", "Sloupcový", "Náhodný šum"],
                               state="readonly")
        self.CBB2.bind('<<ComboboxSelected>>',
                       lambda event: self.show_Setup_Frame(self.input_frames[self.CBB2.current()]))
        self.CBB2.current(0)
        self.CBB2.place(bordermode=OUTSIDE, width=MAX_WIDTH * .15, height=MAX_HEIGHT * .05,
                        x=MAX_WIDTH * .01, y=MAX_HEIGHT * .05)

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
        for i in range(50):
            Frame(self.scrollable_frame).pack()

        self.Table_container.place(bordermode=OUTSIDE, x=MAX_WIDTH * .01, y=MAX_HEIGHT * .6, width=MAX_WIDTH * .4,
                                   height=MAX_HEIGHT * .3)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # open console button
        self.console = t.Button(self, text="Konzole", command=lambda: self.console_controller())
        self.console.place(bordermode=OUTSIDE, x=MAX_WIDTH * .01, y=MAX_HEIGHT * .95, height=MAX_HEIGHT * .05,
                           width=MAX_WIDTH * .4)

        # Frame-changing part 😉

        self.SetupFrames = {}

        self._frame = None
        self.show_Setup_Frame(Mathematical)

    def show_Setup_Frame(self, cont):
        global coordinates_all_list, coordinates_scatter, coordinates_plot, TO_ANIMATE


        new_frame = cont(self.SetupContainer, self)
        TO_ANIMATE = GRAPHING_METHOD[new_frame.type]
        print(new_frame.type)

        if self._frame is not None:
            for child in self._frame.winfo_children():
                child.destroy()
            self._frame.destroy()
        self._frame = new_frame
        self._frame.place(x=MAX_WIDTH * .01, y=MAX_HEIGHT * .15, height=MAX_HEIGHT * 45, width=MAX_WIDTH * .40)
        coordinates_plot = []
        coordinates_scatter = []
        coordinates_all_list = []
        self.update_table()

    def add_point_scatter(self, x, y):
        global coordinates_scatter, coordinates_all_list, lim1, lim2
        if x > lim1:
            lim1 = x
        if x < lim2:
            lim2 = x
        if y > lim1:
            lim1 = y
        if y < lim2:
            lim2 = y
        if [x, y] not in coordinates_scatter:
            coordinates_scatter.append([x, y, "v", "blue", "1"])
            coordinates_all_list.append(f"{x}:{y}")
            self.update_table()

    def add_plot_from_function(self, function):
        global coordinates_plot, coordinates_all_list
        x = np.arange(lim2, lim1, 0.0001)
        y = function

        checnk = True
        if len(coordinates_plot) >= 1:
            for val in coordinates_plot:
                if val[1] == y:
                    checnk = False
        if checnk:
            coordinates_plot.append([x, y, "dotted", "blue", "1", function])
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
        global coordinates_all_list, coordinates_scatter, coordinates_plot
        top = Toplevel()
        top.config(background="black")
        top.wm_geometry("800x500")
        top.maxsize(width=800, height=500)
        top.minsize(width=800, height=500)
        top.title("Konzole")
        types = t.Entry(top)
        types.place(bordermode=OUTSIDE, width=700, height=20, x=0, y=480)
        types.focus()
        send_command = t.Button(top, text="odeslat", command=lambda: self.command_entered(types, scrollable_Frame))
        send_command.place(bordermode=OUTSIDE, width=100, height=20, x=700, y=480)

        table_container = t.Frame(top)
        canvas = Canvas(table_container)
        canvas.configure(bg="black")
        scrollbar = t.Scrollbar(table_container, orient="vertical", command=canvas.yview)
        scrollable_Frame = Frame(canvas)
        scrollable_Frame.configure(bg="black")
        scrollable_Frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=self.canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_Frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        table_container.place(bordermode=OUTSIDE, x=0, y=0, width=800,
                              height=480)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        top.bind("<Return>", lambda event: self.command_entered(types, scrollable_Frame))

    def command_entered(self, entry, frame):
        command = entry.get().split(" ")
        if command[0] == "del":
            try:
                if int(command[1]) <= len(coordinates_all_list):
                    self.delete_value(int(command[1]))
                    Label(frame, text=f"{' '.join(command)}", bg="black", fg="yellow", font=fonts()["SMALL_FONT"],
                          anchor="w").pack(fill=BOTH)
                    Label(frame, text=f"Souřadnice indexu {command[1]} odstraněna!", bg="black", fg="green",
                          font=fonts()["SMALL_FONT"], anchor="w").pack(fill=BOTH)
                    entry.delete(0, END)
                else:
                    Label(frame, text="Neplatný index!", bg="black", fg="red", font=fonts()["SMALL_FONT"],
                          anchor="w").pack(
                        fill=BOTH)
                    entry.delete(0, END)
            except IndexError:
                Label(frame, text="Neplatný index!", bg="black", fg="red", font=fonts()["SMALL_FONT"], anchor="w").pack(
                    fill=BOTH)
                entry.delete(0, END)
            except ValueError:
                Label(frame, text="Neplatný index!", bg="black", fg="red", font=fonts()["SMALL_FONT"], anchor="w").pack(
                    fill=BOTH)
                entry.delete(0, END)


        elif command[0] == "col":
            try:
                if int(command[1]) <= len(coordinates_all_list):
                    self.changeColor(int(command[1]))
                    Label(frame, text=f"{' '.join(command)}", bg="black", fg="yellow", font=fonts()["SMALL_FONT"],
                          anchor="w").pack(fill=BOTH)
                    Label(frame, text=f"Barva indexu {command[1]} změněna!", bg="black", fg="green",
                          font=fonts()["SMALL_FONT"], anchor="w").pack(fill=BOTH)

                    entry.delete(0, END)
                else:
                    Label(frame, text="Neplatný index!", bg="black", fg="red", font=fonts()["SMALL_FONT"],
                          anchor="w").pack(
                        fill=BOTH)
                    entry.delete(0, END)

            except IndexError:
                Label(frame, text="Neplatný index!", bg="black", fg="red", font=fonts()["SMALL_FONT"], anchor="w").pack(
                    fill=BOTH)
                entry.delete(0, END)
            except ValueError:
                Label(frame, text="Neplatný index!", bg="black", fg="red", font=fonts()["SMALL_FONT"], anchor="w").pack(
                    fill=BOTH)
                entry.delete(0, END)


        elif command[0] == "size":
            try:
                if int(command[1]) <= len(coordinates_all_list):
                    self.changeSize(int(command[1]), command[2])
                    Label(frame, text=f"{' '.join(command)}", bg="black", fg="yellow", font=fonts()["SMALL_FONT"],
                          anchor="w").pack(fill=BOTH)
                    Label(frame, text=f"Tloušťka indexu {command[1]} změněna!", bg="black", fg="green",
                          font=fonts()["SMALL_FONT"], anchor="w").pack(fill=BOTH)

                    entry.delete(0, END)
                else:
                    Label(frame, text="Neplatný index!", bg="black", fg="red", font=fonts()["SMALL_FONT"],
                          anchor="w").pack(
                        fill=BOTH)
                    entry.delete(0, END)

            except IndexError:
                Label(frame, text="Neplatný index!", bg="black", fg="red", font=fonts()["SMALL_FONT"], anchor="w").pack(
                    fill=BOTH)
                entry.delete(0, END)
            except ValueError:
                Label(frame, text="Neplatný index!", bg="black", fg="red", font=fonts()["SMALL_FONT"], anchor="w").pack(
                    fill=BOTH)
                entry.delete(0, END)

        elif command[0] == "mktype":
            try:
                if int(command[1]) <= len(coordinates_all_list):
                    self.changeLine(int(command[1]), command[2])
                    Label(frame, text=f"{' '.join(command)}", bg="black", fg="yellow", font=fonts()["SMALL_FONT"],
                          anchor="w").pack(fill=BOTH)
                    Label(frame, text=f"Značkování indexu {command[1]} upraveno!", bg="black", fg="green",
                          font=fonts()["SMALL_FONT"], anchor="w").pack(fill=BOTH)
                    entry.delete(0, END)
                else:
                    Label(frame, text="Neplatný index!", bg="black", fg="red", font=fonts()["SMALL_FONT"],
                          anchor="w").pack(
                        fill=BOTH)
                    entry.delete(0, END)
            except IndexError:
                Label(frame, text="Neplatný index!", bg="black", fg="red", font=fonts()["SMALL_FONT"], anchor="w").pack(
                    fill=BOTH)
                entry.delete(0, END)
            except ValueError:
                Label(frame, text="Neplatný index!", bg="black", fg="red", font=fonts()["SMALL_FONT"], anchor="w").pack(
                    fill=BOTH)
                entry.delete(0, END)
            except SyntaxError:
                Label(frame, text="Neplatná značka!", bg="black", fg="red", font=fonts()["SMALL_FONT"],
                      anchor="w").pack(
                    fill=BOTH)
                Label(frame, text="Použij 'markers' pro zobrazení dostupných značek", bg="black", fg="red",
                      font=fonts()["SMALL_FONT"],
                      anchor="w").pack(
                    fill=BOTH)
                entry.delete(0, END)

        elif command[0] == "GPstyle":
            try:
                self.changeGraphStyle(command[1])
                Label(frame, text=f"{' '.join(command)}", bg="black", fg="yellow", font=fonts()["SMALL_FONT"],
                      anchor="w").pack(fill=BOTH)
                Label(frame, text=f"Styl grafu úspěšně změněn na {command[1]}!", bg="black", fg="green",
                      font=fonts()["SMALL_FONT"], anchor="w").pack(fill=BOTH)
                Label(frame, text=f"Změny na grafu se projeví po restartu aplikace", bg="black", fg="aqua",
                      font=fonts()["ITALIC_SMALL"], anchor="w").pack(fill=BOTH)
                entry.delete(0, END)
            except SyntaxError:
                Label(frame, text="Neplatný styl!", bg="black", fg="red", font=fonts()["SMALL_FONT"],
                      anchor="w").pack(
                    fill=BOTH)
                Label(frame, text="Použij 'ShowMeStyles' pro zobrazení dostupných stylů", bg="black", fg="aqua",
                      font=fonts()["ITALIC_SMALL"],
                      anchor="w").pack(
                    fill=BOTH)
                entry.delete(0, END)

        elif command == ["ShowMeStyles"]:
            Label(frame, text=f"{', '.join(AVALIBLE_STYLES[0:10])},", bg="black", fg="green",
                  font=fonts()["SMALL_FONT"],
                  anchor="w").pack(
                fill=BOTH)
            Label(frame, text=f"{', '.join(AVALIBLE_STYLES[10:16])},", bg="black", fg="green",
                  font=fonts()["SMALL_FONT"],
                  anchor="w").pack(
                fill=BOTH)
            Label(frame, text=f"{', '.join(AVALIBLE_STYLES[16:23])},", bg="black", fg="green",
                  font=fonts()["SMALL_FONT"],
                  anchor="w").pack(
                fill=BOTH)
            Label(frame, text=f"{', '.join(AVALIBLE_STYLES[23:27])}", bg="black", fg="green",
                  font=fonts()["SMALL_FONT"],
                  anchor="w").pack(
                fill=BOTH)
            entry.delete(0, END)

        elif command == ["markers"]:
            Label(frame, text="Dostupné značky: ", bg="black", fg="green", font=fonts()["SMALL_FONT"], anchor="w").pack(
                fill=BOTH)
            Label(frame, text=f"Body: {'; '.join(POINT_MARKERS)}", bg="black", fg="green", font=fonts()["SMALL_FONT"],
                  anchor="w").pack(
                fill=BOTH)
            Label(frame, text=f"Body Extra: {'; '.join(EXTRA_POINT_MARKERS[0:7])},", bg="black", fg="green",
                  font=fonts()["SMALL_FONT"],
                  anchor="w").pack(
                fill=BOTH)
            Label(frame, text=f"{'; '.join(EXTRA_POINT_MARKERS[7:13])};", bg="black", fg="green",
                  font=fonts()["SMALL_FONT"],
                  anchor="w").pack(
                fill=BOTH)
            Label(frame, text=f"{'; '.join(EXTRA_POINT_MARKERS[13:])}; ", bg="black", fg="green",
                  font=fonts()["SMALL_FONT"],
                  anchor="w").pack(
                fill=BOTH)
            Label(frame, text=f"Funkce: {'; '.join(LINE_MARKERS)} ", bg="black", fg="green", font=fonts()["SMALL_FONT"],
                  anchor="w").pack(
                fill=BOTH)
            entry.delete(0, END)



        elif command == ["clear"]:
            for child in frame.winfo_children():
                child.destroy()
            entry.delete(0, END)


        elif command == ["?"] or command == ["help"]:
            Label(frame, text="Dostupné příkazy", bg="black", fg="green", font=fonts()["SMALL_FONT"], anchor="w").pack(
                fill=BOTH)
            Label(frame, text="del [index] - pro odstranění konkrétního vstupu", bg="black", fg="green",
                  font=fonts()["SMALL_FONT"], anchor="w").pack(
                fill=BOTH)
            Label(frame, text="mktype [index] [marker] - pro změnu značkování vstupu", bg="black", fg="green",
                  font=fonts()["SMALL_FONT"], anchor="w").pack(
                fill=BOTH)
            Label(frame, text="markers - pro vypsání značek", bg="black", fg="green",
                  font=fonts()["SMALL_FONT"], anchor="w").pack(
                fill=BOTH)
            Label(frame, text="clear - pro vyčištění konzole", bg="black", fg="green",
                  font=fonts()["SMALL_FONT"], anchor="w").pack(
                fill=BOTH)
            Label(frame, text="col [index] - pro změnu barvy indexu", bg="black", fg="green",
                  font=fonts()["SMALL_FONT"], anchor="w").pack(
                fill=BOTH)
            Label(frame, text="size [index] [size] - pro vyčištění konzole", bg="black", fg="green",
                  font=fonts()["SMALL_FONT"], anchor="w").pack(
                fill=BOTH)

            entry.delete(0, END)





        else:
            Label(frame, text="Neplatný příkaz!", bg="black", fg="red", font=fonts()["SMALL_FONT"], anchor="w").pack(
                fill=BOTH)
            entry.delete(0, END)

    def delete_value(self, index):
        try:
            int(coordinates_all_list[index][0])
            for coord in coordinates_scatter:
                pep = list(map(int, list(coordinates_all_list[index].split(":"))))
                if coord[0:2] == pep:
                    coordinates_scatter.remove(coord)
            del coordinates_all_list[index]
            self.update_table()
        except ValueError:
            for val in coordinates_plot:
                if val[1] == coordinates_all_list[index].split(":")[1]:
                    coordinates_plot.remove(val)
                    del coordinates_all_list[index]
                    self.update_table()

    # TODO prohodit try a if
    def changeLine(self, index, linetype: str):
        if (linetype in LINE_MARKERS + EXTRA_POINT_MARKERS + POINT_MARKERS) or ((linetype[0] and linetype[-1]) == "$"):
            try:
                int(coordinates_all_list[index][0])
                for indx, val in enumerate(coordinates_scatter):
                    if val[0] == int(coordinates_all_list[index].split(":")[0]) and val[1] == int(
                            coordinates_all_list[index].split(":")[1]):
                        coordinates_scatter[indx][2] = linetype
                self.update_table()
            except ValueError:

                for indx, val in enumerate(coordinates_plot):
                    if val[1] == coordinates_all_list[index].split(":")[1]:
                        coordinates_plot[indx][2] = linetype
                        self.update_table()


        else:
            raise SyntaxError

    def changeColor(self, index):
        try:
            int(coordinates_all_list[index][0])
            for indx, val in enumerate(coordinates_scatter):
                if val[0] == int(coordinates_all_list[index].split(":")[0]) and val[1] == int(
                        coordinates_all_list[index].split(":")[1]):
                    color = col.askcolor()
                    coordinates_scatter[indx][3] = color[1]
            self.update_table()
        except ValueError:
            for indx, val in enumerate(coordinates_plot):
                if val[1] == coordinates_all_list[index].split(":")[1]:
                    color = col.askcolor()

                    coordinates_plot[indx][3] = color[1]
                    self.update_table()

    def changeSize(self, index, size):
        try:
            int(coordinates_all_list[index][0])
            for indx, val in enumerate(coordinates_scatter):
                if val[0] == int(coordinates_all_list[index].split(":")[0]) and val[1] == int(
                        coordinates_all_list[index].split(":")[1]):
                    coordinates_scatter[indx][4] = size
            self.update_table()
        except ValueError:
            for indx, val in enumerate(coordinates_plot):
                if val[1] == coordinates_all_list[index].split(":")[1]:
                    coordinates_plot[indx][4] = size
                    self.update_table()

    def changeGraphStyle(self, style):
        if style in AVALIBLE_STYLES:
            with open("graphstyle.txt", "w") as stl:
                stl.truncate()
            with open("graphstyle.txt", "w") as stl:
                stl.write(style)
        else:
            raise SyntaxError


class Mathematical(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.type = "matematical"
        # Scatter
        # labely
        self.labelX = t.Label(self, text="X:", font=fonts()["SMALL_FONT"])
        self.labelY = t.Label(self, text="Y:", font=fonts()["SMALL_FONT"])

        self.labelX.grid(row=0, column=0)
        self.labelY.grid(row=0, column=2)

        # entryes
        self.EntryX = t.Entry(self, justify="center")
        self.EntryY = t.Entry(self, justify="center")

        self.EntryX.grid(row=0, column=1, sticky="we")
        self.EntryY.grid(row=0, column=3, sticky="we")
        # place button
        self.placeButtonScatter = t.Button(self, text="Vložit",
                                           command=lambda: controller.add_point_scatter(int(self.EntryX.get()),
                                                                                        int(self.EntryY.get())))
        self.placeButtonScatter.grid(row=0, column=4, sticky="we")

        # Funkce
        # labely
        self.labelFun = t.Label(self, text="f(x):", font=fonts()["SMALL_FONT"])
        self.labelFun.grid(row=1, column=0)

        # entryes
        self.EntryFun = t.Entry(self, justify="center")

        self.EntryFun.grid(row=1, column=1, columnspan=3, sticky="we")

        # place button
        self.placeButtonPlot = t.Button(self, text="Odložit",
                                        command=lambda: controller.add_plot_from_function(self.EntryFun.get()))

        self.placeButtonPlot.grid(row=1, column=4, sticky="we", pady=20)

        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(3, weight=3)
        self.grid_columnconfigure(4, weight=2)


class Pie(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.type = "pie"
        jo = t.Label(self, text="Koláč")
        jo.grid(row=0, column=0)


class Bar(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.type = "bar"
        jo = t.Label(self, text="Sloup").pack()


class Noise(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.type = "noise"
        jo = t.Label(self, text="Šum").pack()


aniObj = GraphAnimation()
aniFun = aniObj.Go

app = MarkoGebra()

ani = anim.FuncAnimation(f, aniFun, interval=1000, blit=False)


app.mainloop()

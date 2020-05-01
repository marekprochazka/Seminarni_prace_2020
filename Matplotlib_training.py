import matplotlib as mpl
import matplotlib.pyplot as plt
import random

coords = []
# classic
"""
coords.append([[2, 4, 6, 8, 10],[6, 7, 5, 2, 6]])
coords.append([[1,3,5,7,9],[random.randrange(10) for x in range(5)]])

plt.plot(coords[0][0], coords[0][1], label="bar1",color="c")
plt.plot(coords[1][0], coords[1][1], label="bar2",color="k")

plt.xlabel("osa x")
plt.ylabel("osa y")
plt.title("zajímavej graf\nČekni to")
plt.legend()
plt.show()"""

# histogram
"""population_ages = [x for x in range(99)]
value = [random.randrange(1,100) for _ in range(len(population_ages))]

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(population_ages,bins,histtype="bar",rwidth=0.8)

plt.xlabel("osa x")
plt.ylabel("osa y")
plt.title("zajímavej graf\nČekni to")
plt.legend()
plt.show()"""

# scatter
"""coords.append([[random.randrange(15) for _ in range(20)], [random.randrange(15) for _ in range(20)]])
coords.append([[random.randrange(15) for _ in range(20)], [random.randrange(15) for _ in range(20)]])

plt.scatter(coords[0][0], coords[0][1], label="skitscat", color="k",marker="*",s=100)
plt.scatter(coords[1][0], coords[1][1], label="skitscat2", color="r",marker="o",s=100)"""
# stack

"""days = [1, 2, 3, 4, 5, 6]

sleeping = [random.randrange(8) for _ in range(len(days))]
eating = [random.randrange(8) for _ in range(len(days))]
working = [random.randrange(8) for _ in range(len(days))]
playing = [random.randrange(8) for _ in range(len(days))]

plt.stackplot(days, sleeping, eating, working, playing, colors=["k", "r", "c", "b"],labels=["sl","eat","work","play"])

plt.xlabel("osa x")
plt.ylabel("osa y")
plt.title("zajímavej graf\nČekni to")
plt.legend()
plt.show()"""

# pie

"""slices = [7, 2, 2, 13]

activities = ["sleeping", "eating", "working", "playing"]
cols = ["b","r","pink","c"]

plt.pie(slices,labels=activities,colors=cols,startangle=90,explode=(0,0.1,0,0),autopct="%1.1f%%")
# TODO explode u pie koláče vypadá dobře, procenta taky

plt.xlabel("osa x")
plt.ylabel("osa y")
plt.title("zajímavej graf\nČekni to")
#plt.legend()
plt.show()

# loading from files
# v1"""
"""x=[]
y=[]
import csv

with open("sample.txt","r") as csvfile:
    plots = csv.reader(csvfile, delimiter=",")
    for row in plots:
        x.append(row[0])
        y.append(row[1])



plt.plot(x,y,label="From file")
plt.xlabel("osa x")
plt.ylabel("osa y")
plt.title("zajímavej graf\nČekni to")
plt.legend()
plt.show()"""
# v2
import numpy as np

"""x, y = np.loadtxt("sample.txt", delimiter=",", unpack=True)

plt.plot(x,y,label="From file")

plt.xlabel("osa x")
plt.ylabel("osa y")
plt.title("zajímavej graf\nČekni to")
plt.legend()
plt.show()"""

# data from internet

"""import urllib
import matplotlib.dates as mdates

def graph_data(stock):
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    stock_data = []

    split_source = source_code.split("\n")
    
    for line in split_source:
        split_line = line.split(",")
        if len(split_line) == 6:
            if "values" not in line:
                stock_data.append(line)
                
    date, closep, highp,lowp,openp,volume = np.loadtxt(stock_data,delimiter=",",unpack=True
                                                       converters={0: bytespdate2num("")})

graph_data("TSLA")"""
# nejde

# figura
# TODO rotace labelů, další modifikace

"""fig = plt.figure()
ax1 = plt.subplot2grid((1, 1), (0, 0))

coords.append([[2, 4, 6, 8, 10], [6, 7, 5, 2, 6]])
coords.append([[1, 3, 5, 7, 9], [random.randrange(10) for x in range(5)]])

coords.append([[1, 3, 5, 7, 9], [random.randrange(40) for x in range(5)]])

ax1.plot(coords[0][0], coords[0][1], label="plot1", color="c")
ax1.plot(coords[1][0], coords[1][1], label="plot2", color="k")
ax1.axhline(2, color="c", bdth=2)
# ax1.fill_between(coords[2][0], coords[2][1], coords[2][1][0], label="fill", color="r",
#                 alpha=0.3)  # TODO zajímavá možnost *alpha průsvitnost**třetí hodnota značí kde začíná fill

for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(45)

ax1.grid(True, color="c", linestyle="--")
ax1.xaxis.label.set_color("r")
ax1.yaxis.label.set_color("b")
ax1.set_yticks([0, 5, 10, 15])  # TODO bude potřeba pro uživatele

ax1.spines["left"].set_color("r")  # okraje
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)
ax1.spines["left"].set_linewidth(3)

ax1.tick_params(axis="x", colors="#f06215")

plt.xlabel("osa x")
plt.ylabel("osa y")
plt.title("zajímavej graf\nČekni to")
plt.legend()
plt.subplots_adjust(left=0.09, bottom=0.16, right=0.94, top=0.9, wspace=0.2,
                    hspace=0)  # ""space je jako padding subplotů
plt.show()"""
"""slices = [7, 2, 2, 13]
cols = ["b","r","pink","c"]
activities = ["sleeping", "eating", "working", "playing"]"""

"""values=[110,220,180]
names = ["jo","ne","ach"]

f = plt.figure()
a = plt.subplot2grid((1,1),(0,0))
a.bar(names[0],values[0],color="k")
a.bar(names[1],values[1],color="r")
a.bar(names[2],values[2],color="y")
"""


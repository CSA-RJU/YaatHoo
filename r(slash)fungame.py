#Riley
#Comp Prog
#10/15/18

from tkinter import ttk
from tkinter import *
#from PIL import ImageTk #This is for the images.
import tkinter as tk
import random

ones=(0) #On/off values.
twos=(0)
threes=(0)
fours=(0)
fives=(0)
sixes=(0)
pick_ones=(0)
pick_twos=(0)
pick_threes=(0)
pick_fours=(0)
pick_fives=(0)
pick_sixes=(0)
pick_die1=(0)
pick_die2=(0)
pick_die3=(0)
pick_die4=(0)
pick_die5=(0)

root = tk.Tk() #Extra values.
five_count = (1, 2 ,3 ,4 ,5)
rolls_left = (3)
total_value = (0)
onestotal = (0)
twostotal = (0)
threestotal = (0)
fourstotal = (0)
fivestotal = (0)
sixestotal = (0)
combovar=StringVar()
spinvar=StringVar()
resultsContents=StringVar()
onesvar=StringVar(value=ones)
twosvar=StringVar(value=twos)
threesvar=StringVar(value=threes)
foursvar=StringVar(value=fours)
fivesvar=StringVar(value=fives)
sixesvar=StringVar(value=sixes)
all_comboboxes=[]

#die1 = ImageTk.PhotoImage(file="die1.png") #These define the the images used for the dice.
#die2 = ImageTk.PhotoImage(file="die2.png")
#die3 = ImageTk.PhotoImage(file="die3.png")
#die4 = ImageTk.PhotoImage(file="die4.png")
#die5 = ImageTk.PhotoImage(file="die5.png")
#die6 = ImageTk.PhotoImage(file="die6.png")

def about(): #Makes a new box that shows what this program does and general info.
    EX=Toplevel(root)
    aboL=Label(EX, text='''This program was made by Riley
Underwood as a project for his school.

The purpose of this program in to
write to a file the choices about
where and how the user traveled.

Version: 1.0.1''') #Creates a label that says what's in the ".
    aboL.grid(column=1, row=1, sticky="NSEW")
    EX.grid_columnconfigure(1,weight=1)
    EX.grid_rowconfigure(1,weight=1)

def QUIT(): #Quits.
   quit()

def report(*args): #Opens a bug report toplevel.
    global notT
    EX = Toplevel(root)
    notL=Label(EX, text="Bug(s):")  # Creates a label that says what's in the ".
    notL.grid(column=10, row=9, columnspan=20, sticky="NSEW")
    notT=Text(EX, width=5, height=5) #This is where to write the bug.
    notT.grid(column=10, row=10, columnspan=20, sticky="NSEW")
    canB=ttk.Button(EX, text="Quit", command=QUIT)  # Creates a "Quit" button.
    canB.grid(column=10, row=20, sticky="NSEW")
    subB=ttk.Button(EX, text="Submit", command=report_submit)  # Creates a "Submit" button.
    subB.grid(column=20, row=20, sticky="NSEW")
    EX.grid_columnconfigure(10, weight=1)
    EX.grid_columnconfigure(20, weight=1)
    EX.grid_rowconfigure(9, weight=1)
    EX.grid_rowconfigure(10, weight=1)
    EX.grid_rowconfigure(20, weight=1)
    EX.tk.call('wm', 'iconphoto', EX._w, tk.PhotoImage(file='hi-res-icon.png'))

def report_submit(): #Submits the reported bug to a file.
    global notT
    ledcheck = open("trip_ledge.txt", "a")
    ledcheck.write("Bug:" + str(notT.get(1.0, END)))  # Shows all applied data.
    ledcheck.write("\n====================================================================================\n")  # For organising.
    ledcheck.close()

def start(*args): #Decides which function to trigger based on the amount of players.
    if spinvar.get() == "1":
        start1()
    elif spinvar.get() == "2":
        print("Coming soon...")
    else:
        print("Uh oh! An error was discovered!")

def lock_ones(*args):
    global oneB, rolls_left, pick_ones
    pick_ones=1
    rolls_left = 3
    oneB.configure(state=DISABLED)
    update()

def lock_twos(*args):
    global twoB, rolls_left, pick_twos
    pick_twos=1
    rolls_left = 3
    twoB.configure(state=DISABLED)
    update()

def lock_threes(*args):
    global thrB, rolls_left, pick_threes
    pick_threes=1
    rolls_left = 3
    thrB.configure(state=DISABLED)
    update()

def lock_fours(*args):
    global fouB, rolls_left, pick_fours
    pick_fours=1
    rolls_left = 3
    fouB.configure(state=DISABLED)
    update()

def lock_fives(*args):
    global fivB, rolls_left, pick_fives
    pick_fives=1
    rolls_left = 3
    fivB.configure(state=DISABLED)
    update()

def lock_sixes(*args):
    global sixB, rolls_left, pick_sixes
    pick_sixes=1
    rolls_left = 3
    sixB.configure(state=DISABLED)
    update()

def lock_die1(*args):
    global dieB1, pick_die1
    pick_die1=1
    dieB1.configure(state=DISABLED)

def lock_die2(*args):
    global dieB2, pick_die2
    pick_die2=1
    dieB2.configure(state=DISABLED)

def lock_die3(*args):
    global dieB3, pick_die3
    pick_die3=1
    dieB3.configure(state=DISABLED)

def lock_die4(*args):
    global dieB4, pick_die4
    pick_die4=1
    dieB4.configure(state=DISABLED)

def lock_die5(*args):
    global dieB5, pick_die5
    pick_die5=1
    dieB5.configure(state=DISABLED)

def finish(*args):
    rolB.configure(state=DISABLED)
    gamL.config(text="WINNER WINNER CHICKEN DINNER!")

def roll():
    global ones, twos, threes, fours, fives, sixes, pick_die1, pick_die2, pick_die3, pick_die4, pick_die5, die1_val, die2_val, die3_val, die4_val, die5_val, rolls_left, onestotal, twostotal, threestotal, fourstotal, fivestotal, sixestotal, total_value, rolB
    if rolls_left == 3:
        dieB1.config(state=NORMAL)
        dieB2.config(state=NORMAL)
        dieB3.config(state=NORMAL)
        dieB4.config(state=NORMAL)
        dieB5.config(state=NORMAL)
        pick_die1 = 0
        pick_die2 = 0
        pick_die3 = 0
        pick_die4 = 0
        pick_die5 = 0
    if rolls_left >= 1:
        rolls_left = rolls_left - 1
    else:
        rolls_left = 3
    if rolls_left == 0:
        rolB.configure(state=DISABLED)
    if rolls_left ==0:
        dieB1.config(state=DISABLED)
        dieB2.config(state=DISABLED)
        dieB3.config(state=DISABLED)
        dieB4.config(state=DISABLED)
        dieB5.config(state=DISABLED)

    total_value = onestotal + twostotal + threestotal + fourstotal + fivestotal+ sixestotal

    for x in five_count:
        if x == 1: #Die 1
            if pick_die1 != 1:
                die1_val = random.randrange(1, 7)
                if die1_val == 1:
                    dieB1.configure(text="1")
                if die1_val == 2:
                    dieB1.configure(text="2")
                if die1_val == 3:
                    dieB1.configure(text="3")
                if die1_val == 4:
                    dieB1.configure(text="4")
                if die1_val == 5:
                    dieB1.configure(text="5")
                if die1_val == 6:
                    dieB1.configure(text="6")
        if x == 2: #Die 2
            if pick_die2 != 1:
                die2_val = random.randrange(1, 7)
                if die2_val == 1:
                    dieB2.configure(text="1")
                if die2_val == 2:
                    dieB2.configure(text="2")
                if die2_val == 3:
                    dieB2.configure(text="3")
                if die2_val == 4:
                    dieB2.configure(text="4")
                if die2_val == 5:
                    dieB2.configure(text="5")
                if die2_val == 6:
                    dieB2.configure(text="6")
        if x == 3: #Die 3
            if pick_die3 != 1:
                die3_val = random.randrange(1, 7)
                if die3_val == 1:
                    dieB3.configure(text="1")
                if die3_val == 2:
                    dieB3.configure(text="2")
                if die3_val == 3:
                    dieB3.configure(text="3")
                if die3_val == 4:
                    dieB3.configure(text="4")
                if die3_val == 5:
                    dieB3.configure(text="5")
                if die3_val == 6:
                    dieB3.configure(text="6")
        if x == 4: #Die 4
            if pick_die4 != 1:
                die4_val = random.randrange(1, 7)
                if die4_val == 1:
                    dieB4.configure(text="1")
                if die4_val == 2:
                    dieB4.configure(text="2")
                if die4_val == 3:
                    dieB4.configure(text="3")
                if die4_val == 4:
                    dieB4.configure(text="4")
                if die4_val == 5:
                    dieB4.configure(text="5")
                if die4_val == 6:
                    dieB4.configure(text="6")
        if x == 5: #Die 5
            if pick_die5 != 1:
                die5_val = random.randrange(1, 7)
                if die5_val == 1:
                    dieB5.configure(text="1")
                if die5_val == 2:
                    dieB5.configure(text="2")
                if die5_val == 3:
                    dieB5.configure(text="3")
                if die5_val == 4:
                    dieB5.configure(text="4")
                if die5_val == 5:
                    dieB5.configure(text="5")
                if die5_val == 6:
                    dieB5.configure(text="6")

                #if die5_val == 1:
                #    dieB5.configure(image=die1)
                #if die5_val == 2:
                #    dieB5.configure(image=die2)
                #if die5_val == 3:
                #    dieB5.configure(image=die3)
                #if die5_val == 4:
                #    dieB5.configure(image=die4)
                #if die5_val == 5:
                #    dieB5.configure(image=die5)
                #if die5_val == 6:
                #    dieB5.configure(image=die6)

    ones = (0)
    if die1_val == 1 or die2_val == 1 or die3_val == 1 or die4_val == 1 or die5_val == 1:
        if die1_val == 1:
            ones = ones + 1
        if die2_val == 1:
            ones = ones + 1
        if die3_val == 1:
            ones = ones + 1
        if die4_val == 1:
            ones = ones + 1
        if die5_val == 1:
            ones = ones + 1
    else:
        ones = (0)

    twos = (0)
    if die1_val == 2 or die2_val == 2 or die3_val == 2 or die4_val == 2 or die5_val == 2:
        if die1_val == 2:
            twos = twos + 2
        if die2_val == 2:
            twos = twos + 2
        if die3_val == 2:
            twos = twos + 2
        if die4_val == 2:
            twos = twos + 2
        if die5_val == 2:
            twos = twos + 2
    else:
        twos = (0)

    threes = (0)
    if die1_val == 3 or die2_val == 3 or die3_val == 3 or die4_val == 3 or die5_val == 3:
        if die1_val == 3:
            threes = threes + 3
        if die2_val == 3:
            threes = threes + 3
        if die3_val == 3:
            threes = threes + 3
        if die4_val == 3:
            threes = threes + 3
        if die5_val == 3:
            threes = threes + 3
    else:
        threes = (0)

    fours = (0)
    if die1_val == 4 or die2_val == 4 or die3_val == 4 or die4_val == 4 or die5_val == 4:
        if die1_val == 4:
            fours = fours + 4
        if die2_val == 4:
            fours = fours + 4
        if die3_val == 4:
            fours = fours + 4
        if die4_val == 4:
            fours = fours + 4
        if die5_val == 4:
            fours = fours + 4
    else:
        fours = (0)

    fives = (0)
    if die1_val == 5 or die2_val == 5 or die3_val == 5 or die4_val == 5 or die5_val == 5:
        if die1_val == 5:
            fives = fives + 5
        if die2_val == 5:
            fives = fives + 5
        if die3_val == 5:
            fives = fives + 5
        if die4_val == 5:
            fives = fives + 5
        if die5_val == 5:
            fives = fives + 5
    else:
        fives = (0)

    sixes = (0)
    if die1_val == 6 or die2_val == 6 or die3_val == 6 or die4_val == 6 or die5_val == 6:
        if die1_val == 6:
            sixes = sixes + 6
        if die2_val == 6:
            sixes = sixes + 6
        if die3_val == 6:
            sixes = sixes + 6
        if die4_val == 6:
            sixes = sixes + 6
        if die5_val == 6:
            sixes = sixes + 6
    else:
        sixes = (0)

    update()

def update(*args):
    global ones, twos, threes, fours, fives, sixes, pick_ones, pick_twos, pick_threes, pick_fours, pick_fives, pick_sixes, onestotal, twostotal, threestotal, fourstotal, fivestotal, sixestotal, total_value
    if pick_ones == 0:
        onestotal = ones
        onesvar = StringVar(value=ones)
        oneE = Entry(G, width=3, state='disabled', textvariable=onesvar) #Updates the ones box
        oneE.grid(column=20, row=10, sticky="NSEW")

    if pick_twos == 0:
        twostotal = twos
        twosvar = StringVar(value=twos)
        twoE = Entry(G, width=3, state='disabled', textvariable=twosvar) #Updates the twos box
        twoE.grid(column=20, row=20, sticky="NSEW")

    if pick_threes == 0:
        threestotal = threes
        threesvar = StringVar(value=threes)
        thrE = Entry(G, width=3, state='disabled', textvariable=threesvar) #Updates the threes box
        thrE.grid(column=20, row=30, sticky="NSEW")

    if pick_fours == 0:
        fourstotal = fours
        foursvar = StringVar(value=fours)
        fouE = Entry(G, width=3, state='disabled', textvariable=foursvar) #Updates the fours box
        fouE.grid(column=20, row=40, sticky="NSEW")

    if pick_fives == 0:
        fivestotal = fives
        fivesvar = StringVar(value=fives)
        fivE = Entry(G, width=3, state='disabled', textvariable=fivesvar) #Updates the fives box
        fivE.grid(column=20, row=50, sticky="NSEW")

    if pick_sixes == 0:
        sixestotal = sixes
        sixesvar = StringVar(value=sixes)
        sixE = Entry(G, width=3, state='disabled', textvariable=sixesvar) #Updates the sixes box
        sixE.grid(column=20, row=60, sticky="NSEW")

    totL1 = Label(G, text=total_value, font=("Times", 12))  # Creates a label that says what's in the ".
    totL1.grid(column=50, row=20, columnspan=20, sticky="NSEW")

    rolL = Label(G, text=rolls_left, font=("Times", 12))  #Updates the roll label
    rolL.grid(column=50, row=50, columnspan=20, sticky="NSEW")

    if rolls_left >=1:
        rolB.config(state='normal') #Makes the roll button clickable

    if pick_ones and pick_twos and pick_threes and pick_fours and pick_fives and pick_sixes:
        finish()

def start1(*args):
    global G, ones, twos, threes, fours, fives, sixes, pick_ones, pick_twos, pick_threes, pick_fours, pick_fives, pick_sixes, pick_die1, pick_die2, pick_die3, pick_die4, pick_die5, gamL, oneB, twoB, thrB, fouB, fivB, sixB, rolB, dieB1, dieB2, dieB3, dieB4, dieB5
    G=Frame(root)
    G.grid(column=20, row=20, sticky="NSEW")
    hmpL.destroy()
    repplaL.destroy()
    repsubL.destroy()
    plaSB.destroy()
    staB.destroy()

    gamL = Label(G, text="Yaathoo", font=("Times", 25)) #Creates a label that says what's in the ".
    gamL.grid(column=10, row=9, columnspan=50, sticky="NSEW")

    oneB = ttk.Button(G, text="Ones", command=lock_ones) #Creates a "Ones" button.
    oneB.grid(column=10, row=10, sticky="NSEW")

    onesvar = StringVar(value=ones)
    oneT = Entry(G, width=3, state='disabled', textvariable=onesvar)
    oneT.grid(column=20, row=10, sticky="NSEW")

    twoB = ttk.Button(G, text="Twos", command=lock_twos) #Creates a "Twos" button.
    twoB.grid(column=10, row=20, sticky="NSEW")

    twosvar = StringVar(value=twos)
    twoT = Entry(G, width=3, state='disabled', textvariable=twosvar)
    twoT.grid(column=20, row=20, sticky="NSEW")

    thrB = ttk.Button(G, text="Threes", command=lock_threes) #Creates a "Threes" button.
    thrB.grid(column=10, row=30, sticky="NSEW")

    threesvar = StringVar(value=threes)
    thrT = Entry(G, width=3, state='disabled', textvariable=threesvar)
    thrT.grid(column=20, row=30, sticky="NSEW")

    fouB = ttk.Button(G, text="Fours", command=lock_fours) #Creates a "Fours" button.
    fouB.grid(column=10, row=40, sticky="NSEW")

    foursvar = StringVar(value=fours)
    fouT = Entry(G, width=3, state='disabled', textvariable=foursvar)
    fouT.grid(column=20, row=40, sticky="NSEW")

    fivB = ttk.Button(G, text="Fives", command=lock_fives) #Creates a "Fives" button.
    fivB.grid(column=10, row=50, sticky="NSEW")

    fivesvar = StringVar(value=fives)
    fivT = Entry(G, width=3, state='disabled', textvariable=fivesvar)
    fivT.grid(column=20, row=50, sticky="NSEW")

    sixB = ttk.Button(G, text="Sixes", command=lock_sixes) #Creates a "Sixes" button.
    sixB.grid(column=10, row=60, sticky="NSEW")

    sixesvar = StringVar(value=sixes)
    sixT = Entry(G, width=3, state='disabled', textvariable=sixesvar)
    sixT.grid(column=20, row=60, sticky="NSEW")

    totL= Label(G, text="Total:", font=("Times", 12))  # Creates a label that says what's in the ".
    totL.grid(column=50, row=10, sticky="NSEW")

    totL1 = Label(G, text=0, font=("Times", 12))  # Creates a label that says what's in the ".
    totL1.grid(column=50, row=20, sticky="NSEW")

    rolL = Label(G, text=rolls_left, font=("Times", 12))  # Creates a label that says what's in the ".
    rolL.grid(column=50, row=50, sticky="NSEW")

    rolB = ttk.Button(G, text="Roll", command=roll)  # Creates a "Sixes" button.
    rolB.grid(column=50, row=60, sticky="NSEW")

    dieB1 = ttk.Button(G, text="1", state=DISABLED, command=lock_die1) #Locks in the selected die.
    dieB1.grid(column=10, row=70, sticky="NSEW")

    dieB2 = ttk.Button(G, text="2", state=DISABLED, command=lock_die2)  # Locks in the selected die.
    dieB2.grid(column=20, row=70, sticky="NSEW")

    dieB3 = ttk.Button(G, text="3", state=DISABLED, command=lock_die3)  # Locks in the selected die.
    dieB3.grid(column=30, row=70, sticky="NSEW")

    dieB4 = ttk.Button(G, text="4", state=DISABLED, command=lock_die4)  # Locks in the selected die.
    dieB4.grid(column=40, row=70, sticky="NSEW")

    dieB5 = ttk.Button(G, text="5", state=DISABLED, command=lock_die5)  # Locks in the selected die.
    dieB5.grid(column=50, row=70, sticky="NSEW")


    G.grid_columnconfigure(10, weight=1)
    G.grid_columnconfigure(20, weight=1)
    G.grid_columnconfigure(30, weight=1)
    G.grid_columnconfigure(40, weight=1)
    G.grid_columnconfigure(50, weight=1)
    G.grid_rowconfigure(9, weight=1)
    G.grid_rowconfigure(10, weight=1)
    G.grid_rowconfigure(20, weight=1)
    G.grid_rowconfigure(30, weight=1)
    G.grid_rowconfigure(40, weight=1)
    G.grid_rowconfigure(50, weight=1)
    G.grid_rowconfigure(60, weight=1)
    G.grid_rowconfigure(70, weight=1)


########################### Widgets ###########################

menubar=Menu(root)
filemenu=Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=QUIT)
menubar.add_cascade(label="File", menu=filemenu) #Create a pulldown menu, and add it to the menu bar.

helpmenu=Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
helpmenu.add_command(label="Report bug", command=report)
menubar.add_cascade(label="Help", menu=helpmenu) #Makes a help dropdown menu.

hmpL=Label(root, text="How many players?", height=2, width=6)
hmpL.grid(column=10, row=10,  sticky="NSEW")
repplaL=Label(root, text="", height=2, width=6)
repplaL.grid(column=10, row=20,  sticky="NSEW")
repsubL=Label(root, text="", height=2, width=6)
repsubL.grid(column=10, row=30,  sticky="NSEW")

plaSB_list=["1", "2"]
plaSB=Spinbox(root, state="readonly", values=plaSB_list, textvariable=spinvar)
plaSB.grid(column=10, row=20, sticky="NSEW")
spinvar.set("1")

staB=ttk.Button(root, text="Start", command=start)  #Creates a "Submit" button.
staB.grid(column=10, row=30, sticky="NSEW")

ttk.Sizegrip().grid(column=999, row=999, sticky=(S, E))

########################Grid#############################

root.grid_columnconfigure(10,weight=1)
root.grid_rowconfigure(10,weight=1)
root.grid_rowconfigure(20,weight=1)
root.grid_rowconfigure(30,weight=1)

root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='hi-res-icon.png'))
root.title("Yaathoo") #Makes the title what is in the "s.
root.config(menu=menubar) #Display the menu.
root.mainloop()
root.destroy()
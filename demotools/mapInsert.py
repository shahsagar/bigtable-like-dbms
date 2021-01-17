import os
import tkinter as tk
from tkinter import simpledialog

JDKPATH = "/library/java/JavaVirtualMachines/jdk-13.0.1.jdk/Contents/Home/bin/java"
CLASSPATH = "/Users/akash/Desktop/cse510-project-sp20-0228-midway/javaminibase/src"

def insertMap():
    RL = e1.get()
    CL = e2.get()
    VAL = e3.get()
    TS = e4.get()
    TYPE = e5.get()
    BIGTABLENAME = e6.get()
    NUMBUF = e7.get()
    insertCommand = "cd {} && {} -classpath {} -cp . app.MapInsert {} {} {} {} {} {} {} >> log_mapinsert".format(CLASSPATH, JDKPATH, CLASSPATH, RL, CL, VAL, TS, TYPE, BIGTABLENAME, NUMBUF)
    os.system(insertCommand)

master = tk.Tk()
tk.Label(master, 
         text="RL").grid(row=0)
tk.Label(master, 
         text="CL").grid(row=1)
tk.Label(master, 
         text="VAL").grid(row=2)
tk.Label(master, 
         text="TS").grid(row=3)
tk.Label(master, 
         text="TYPE").grid(row=4)
tk.Label(master, 
         text="BIGTABLENAME").grid(row=5)
tk.Label(master, 
         text="NUMBUF").grid(row=6)


e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)
e6 = tk.Entry(master)
e7 = tk.Entry(master)


e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)
e7.grid(row=6, column=1)

tk.Button(master, 
          text='Insert Map', command=insertMap).grid(row=7, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.mainloop()

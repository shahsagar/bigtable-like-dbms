import os
import tkinter as tk
from tkinter import simpledialog

JDKPATH = "/library/java/JavaVirtualMachines/jdk-13.0.1.jdk/Contents/Home/bin/java"
CLASSPATH = "/Users/akash/Desktop/cse510-project-sp20-0228-midway/javaminibase/src"


def rowJoin():
    INPUTBIGTABLENAME1 = e1.get()
    INPUTBIGTABLENAME2 = e2.get()
    OUTPUTBIGTABLENAME =  e3.get()
    COLUMNFILTER = e4.get()
    NUMBUF = e5.get()

    joinCommand = "cd {} && {} -classpath {} -cp . app.MainRowJoin {} {} {} >> log_rowjoin".format(CLASSPATH, JDKPATH, CLASSPATH, INPUTBIGTABLENAME1, INPUTBIGTABLENAME2, OUTPUTBIGTABLENAME, COLUMNFILTER, NUMBUF)
    os.system(joinCommand)


master = tk.Tk()
tk.Label(master, 
         text="INPUT BIGTABLENAME1").grid(row=0)
tk.Label(master, 
         text="INPUT BIGTABLENAME2").grid(row=1)
tk.Label(master, 
         text="OUTPUT BIGTABLENAME").grid(row=2)
tk.Label(master, 
         text="COLUMNFILTER").grid(row=3)
tk.Label(master, 
         text="NUMBUF").grid(row=4)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)


tk.Button(master, 
          text='Join', command=rowJoin).grid(row=5, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.mainloop()

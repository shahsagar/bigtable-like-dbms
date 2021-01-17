import os
import tkinter as tk
from tkinter import simpledialog

JDKPATH = "/library/java/JavaVirtualMachines/jdk-13.0.1.jdk/Contents/Home/bin/java"
CLASSPATH = "/Users/akash/Desktop/cse510-project-sp20-0228-midway/javaminibase/src"


def getCounts():
    NUMBUF = e1.get()

    countCommand = "cd {} && {} -classpath {} -cp . app.MainGetCounts {} {} {} >> log_getcounts".format(CLASSPATH, JDKPATH, CLASSPATH, NUMBUF)
    os.system(countCommand)


master = tk.Tk()
tk.Label(master, 
         text="NUMBUF").grid(row=0)

e1 = tk.Entry(master)


e1.grid(row=0, column=1)


tk.Button(master, 
          text='Get Count', command=getCounts).grid(row=2, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.mainloop()

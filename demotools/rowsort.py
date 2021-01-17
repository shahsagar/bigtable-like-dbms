import os
import tkinter as tk
from tkinter import simpledialog

JDKPATH = "/library/java/JavaVirtualMachines/jdk-13.0.1.jdk/Contents/Home/bin/java"
CLASSPATH = "/Users/akash/Desktop/cse510-project-sp20-0228-midway/javaminibase/src"


def rowSort():
    INPUTBIGTABLENAME = e1.get()
    OUTPUTBIGTABLENAME =  e2.get()
    ROWORDER = e3.get()
    COLUMNNAME = e4.get()
    NUMBUF = e5.get()

    sortCommand = "cd {} && {} -classpath {} -cp . app.MainRowSort {} {} {} >> log_rowsort".format(CLASSPATH, JDKPATH, CLASSPATH, INPUTBIGTABLENAME, OUTPUTBIGTABLENAME, ROWORDER, COLUMNNAME, NUMBUF)
    os.system(sortCommand)


master = tk.Tk()
tk.Label(master, 
         text="INPUT BIGTABLENAME").grid(row=0)
tk.Label(master, 
         text="OUTPUT BIGTABLENAME").grid(row=1)
tk.Label(master, 
         text="ROWORDER").grid(row=2)
tk.Label(master, 
         text="COLUMNNAME").grid(row=3)
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
          text='Sort', command=rowSort).grid(row=5, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.mainloop()

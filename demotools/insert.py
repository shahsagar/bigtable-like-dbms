import os
import tkinter as tk
from tkinter import simpledialog

JDKPATH = "/library/java/JavaVirtualMachines/jdk-13.0.1.jdk/Contents/Home/bin/java"
CLASSPATH = "/Users/akash/Desktop/cse510-project-sp20-0228-midway/javaminibase/src"


def batchInsert():
    BIGTABLENAME = e1.get()
    DATAFILENAME =  e2.get()
    TYPE = e3.get()
    insertCommand = "cd {} && {} -classpath {} -cp . app.MainBatchInsert {} {} {} >> log_insertion".format(CLASSPATH, JDKPATH, CLASSPATH, DATAFILENAME, TYPE, BIGTABLENAME)
    os.system(insertCommand)


master = tk.Tk()
tk.Label(master, 
         text="BIGTABLENAME").grid(row=0)
tk.Label(master, 
         text="DATAFILENAME").grid(row=1)

tk.Label(master, 
         text="TYPE").grid(row=2)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)


tk.Button(master, 
          text='Insert', command=batchInsert).grid(row=8, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.mainloop()



  
#query = "cd /Users/akash/Desktop/cse510-project-sp20-0228-midway/javaminibase/src && 
#/library/java/JavaVirtualMachines/jdk-13.0.1.jdk/Contents/Home/bin/java  -classpath 
#/Users/akash/Desktop/cse510-project-sp20-0228-midway/javaminibase/src -cp . app.MainBatchInsert '../../test_data_1a.csv' 1 'demo_table'"

#/library/java/JavaVirtualMachines/jdk-13.0.1.jdk/Contents/Home/bin/java  -classpath 
#/Users/akash/Desktop/cse510-project-sp20-0228-midway/javaminibase/src -cp . app.MainQuery 'demo_table' 1 3 '[Arizona:California]' '*' '*' 2000 >> log_query
import os
import tkinter as tk
from tkinter import simpledialog

JDKPATH = "/library/java/JavaVirtualMachines/jdk-13.0.1.jdk/Contents/Home/bin/java"
CLASSPATH = "/Users/akash/Desktop/cse510-project-sp20-0228-midway/javaminibase/src"

def batchQuery():
    BIGTABLENAME = e1.get()
    TYPE = e2.get()
    ORDERTYPE = e3.get()
    ROWFILTER = e4.get()
    COLUMNFILTER = e5.get()
    VALUEFILTER = e6.get()
    NUMBUF = e7.get()
    queryCommand = "cd {} && {} -classpath {} -cp . app.MainQuery {} {} {} {} {} {} {} >> log_query".format(CLASSPATH, JDKPATH, CLASSPATH, BIGTABLENAME, TYPE, ORDERTYPE, ROWFILTER, COLUMNFILTER, VALUEFILTER, NUMBUF)
    os.system(queryCommand)

master = tk.Tk()
tk.Label(master, 
         text="BIGTABLENAME").grid(row=0)
tk.Label(master, 
         text="TYPE").grid(row=1)
tk.Label(master, 
         text="ORDERTYPE").grid(row=2)
tk.Label(master, 
         text="ROWFILTER").grid(row=3)
tk.Label(master, 
         text="COLUMNFILTER").grid(row=4)
tk.Label(master, 
         text="VALUEFILTER").grid(row=5)
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
          text='Query', command=batchQuery).grid(row=9, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.mainloop()



    

#query = "cd /Users/akash/Desktop/cse510-project-sp20-0228-midway/javaminibase/src && 
#/library/java/JavaVirtualMachines/jdk-13.0.1.jdk/Contents/Home/bin/java  -classpath 
#/Users/akash/Desktop/cse510-project-sp20-0228-midway/javaminibase/src -cp . app.MainBatchInsert '../../test_data_1a.csv' 1 'demo_table'"

#/library/java/JavaVirtualMachines/jdk-13.0.1.jdk/Contents/Home/bin/java  -classpath 
#/Users/akash/Desktop/cse510-project-sp20-0228-midway/javaminibase/src -cp . app.MainQuery 'demo_table' 1 3 '[Arizona:California]' '*' '*' 2000 >> log_query
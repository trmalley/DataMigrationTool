import os
import Tkinter as tk
import ScrolledText
import tkFileDialog
import ttk
import getpass
import datetime
import atexit


'''
Author: Thomas
This program works as a Data Transfer Tool

It takes in two arguments, Source and Destination path folders.
Then it creates a batch file to run robocopy with the variables

robocopy %source% %destination% /e /xj /w:0 /r:0

Once the command finishes the batch file is deleted
The output is logged to a file called batch.log
The log is printed in the GUI and the scrolledtext window will focus
on the end of the log to verify transfer completed. The entire log can be viewed
in the GUI or in ./batch.log
'''

now = datetime.datetime.now()


#Create instance
win = tk.Tk()

#Add  a title
win.title("Data Migration Tool")

#Prevent GUI from being resized
win.resizable(False,False)

uName = getpass.getuser()

#Labels setup
Title = ttk.Label(win, text="Data Migration Tool")
Title.grid(column=0, row=0)
SourceLable = ttk.Label(win, text="")
SourceLable.grid(column=0, row=2)
DestinationLable = ttk.Label(win, text="C:\Users\\" + uName + "\\Desktop\\Backup-"+str(now.strftime("%Y-%m-%d")))
DestinationLable.grid(column=1, row=2)

sourcePath = ""
destinationPath = "C:\Users\\" + uName + "\\Desktop\\Backup-"+str(now.strftime("%Y-%m-%d"))
logPath = 'batch.log'
#Button click even function
def click_me():
    action.configure(text='Hello ' + name.get())
    
def SourceFolder():
    global sourcePath
    sourcePath = tkFileDialog.askdirectory()
    sourcePath = "\"" + sourcePath + "\""
    SourceLable.configure(text=sourcePath)
    run.configure(state='enabled')

def DestinationFolder():
    global destinationPath
    destinationPath = tkFileDialog.askdirectory()
    destinationPath = "\"" + destinationPath + "\""
    DestinationLable.configure(text=destinationPath)

def Run():
    CreateBatch()
    RunBatch()
    DisplayLog()
    run.configure(state='disabled')

#####Functions#####

    #Create batch file
def CreateBatch():
    f = open('batch.bat','w')
    f.write('@echo off\nset LOGFILE=batch.log\n'\
        'call :LOG > %LOGFILE% \n'\
        'exit /B\n\n:LOG\n')
    f.write('\n\n\nrobocopy ' + sourcePath + ' '\
            ''+ destinationPath + ' /e /xj /w:0 /r:0\n')
    f.close()


def RunBatch():
    #Set file path for batch file
    filepath = "batch.bat"

    #Run batch file
    os.system(filepath)
    
    #delete batch file once job has been complete
    #commented out for testing
    os.remove(filepath)
    

#read from log file display in scrolled text then focus to the end of the file
def DisplayLog():
    f = open('batch.log','r')
    message = f.read()
    scr.insert('end',message)
    scr.yview('end')
    f.close()

def exit_handler():
    if os.path.isfile(logPath):
        os.remove(logPath)
    win.destroy()

    
#Adding button
getSource = ttk.Button(win, text="Select Source!", command=SourceFolder)
getSource.grid(column=0, row=1)


getDest = ttk.Button(win, text="Select Destination!", command=DestinationFolder)
getDest.grid(column=1, row=1)

run = ttk.Button(win, text="Run", command=Run)
run.grid(column=3, row=0)
run.configure(state='disabled')

scrol_w = 80
scrol_h = 15
scr = ScrolledText.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, columnspan=4)

'''
TODO

Formatting is okay for now
Need go/start button(Only enabled when both source and Destination is set)

'''

#===================
#=====StartGui======
#===================
win.protocol("WM_DELETE_WINDOW", exit_handler)
win.mainloop()


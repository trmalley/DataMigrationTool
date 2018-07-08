import os
import Tkinter as tk
import tkMessageBox
import ScrolledText
import tkFileDialog
import ttk
import getpass
import datetime
from time import sleep
#import atexit   #imported at some point. not sure if still needed
import subprocess

'''
Author: Thomas GITHUB: trmalley
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

#Set file path for batch file and log file
filePath = "batch.bat"
logPath = "batch.log"

#Create instance
win = tk.Tk()

#Add  a title
win.title("Data Migration Tool")

#Prevent GUI from being resized
win.resizable(False,False)

#Get host username and set default path variable
uName = getpass.getuser()
defaultDest = "C:/Users//" + uName + "//Desktop//Backup-"+str(now.strftime("%Y-%m-%d"))

#initialize Source and Destination path variables
sourcePath = ""
destinationPath = defaultDest

jobFinished = "##########JOB COMPLETE##########"

#Labels setup
Title = ttk.Label(win, text='Data Migration Tool')
Title.grid(column=1, row=0, columnspan=2)
SourceLable = ttk.Label(win, text="")
SourceLable.grid(column=0, row=2)
DestinationLable = ttk.Label(win, text=defaultDest)
DestinationLable.grid(column=1, row=2)


CMDSubprocess =""

#Check and see if 
if not os.path.isfile(logPath):
    log = open(logPath, 'a')
    log.close()

#Button click even functions
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
    run.configure(state='disabled')

#####Functions#####

    #Create batch file
def CreateBatch():
    bat = open(filePath,'w')
    bat.write('@echo off\nset LOGFILE=batch.log\n'\
        'call :LOG > %LOGFILE% \n'\
        'exit /B\n\n:LOG\n')
    bat.write('\n\n\nrobocopy ' + sourcePath + ' '\
            ''+ destinationPath + ' /e /xj /w:0 /r:0\n'\
            'echo ' + jobFinished)
    bat.close()

def RunBatch():
    #Run batch file
    CMDSubprocess = subprocess.Popen(filePath,shell=False, close_fds=True)
    FinishedLable.configure(text='Starting...')
    FinishedLable.configure(foreground='red')
    win.update()
    RunProgressBar()

    #Job Complete

    #Restore Default Destination once job is completed --Not necessary but there anyways
    destinationPath = defaultDest
    destinationLable = defaultDest
    
    #delete batch file once job has been complete and notify user
    os.remove(filePath)
    tkMessageBox.showinfo('Completed!', '***Data transfer has completed, please check for errors.\nOnce program is closed log file will be deleted***')
    

#read from log file display in scrolled text then focus to the end of the file
def DisplayLog():
    f = open('batch.log','r')
    message = f.read()
    scr.insert('end',message)
    scr.yview('end')
    f.close()

def RunProgressBar():
    prog_bar.start(10)
    sleep(10)
    FinishedLable.configure(text='Running...')
    FinishedLable.configure(foreground='yellow')
    with open(logPath,'r') as f:
        line = f.readline()
        while True:
            scr.insert('end',line)
            scr.yview('end')
            win.update()
            line = f.readline()
            if jobFinished in line:
                break
           
        
    prog_bar.stop()
    FinishedLable.configure(text='Finished!')
    FinishedLable.configure(foreground='green')
    sourcePath = ""
    destinationPath = defaultDest

def exit_handler():
    if os.path.isfile(logPath):
        os.remove(logPath)
    win.destroy()

    
#Adding button
getSource = ttk.Button(win, text='Select Source', command=SourceFolder)
getSource.grid(column=0, row=1)


getDest = ttk.Button(win, text='Select Destination', command=DestinationFolder)
getDest.grid(column=1, row=1)

run = ttk.Button(win, text='Run', command=Run)
run.grid(column=3, row=1)
run.configure(state='disabled')

#Scrolled Text
scrol_w = 80
scrol_h = 15
scr = ScrolledText.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, columnspan=4)
scr.insert(tk.INSERT,
'''#############################
#Step 1 - Select Source     #
#Step 2 - Select Destination#
#Step 3 - Run               #
#Step 4 - Verify Result     #
#############################''')

#Progress Bar
FinishedLable = ttk.Label(win, text='Not Started...')
FinishedLable.grid(column=1, row=4)

prog_bar = ttk.Progressbar(orient='horizontal', length=100, mode='indeterminate')
prog_bar.grid(column=0, row=4)


'''
TODO

Formatting is okay for now but could be improved
Add cancel button
Code Optimization
'''

#Exit handler to ensure .bat and .log is deleted
win.protocol("WM_DELETE_WINDOW", exit_handler)
win.mainloop()


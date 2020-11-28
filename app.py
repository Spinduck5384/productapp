import tkinter as tk
from tkinter import filedialog, Text
import os
import sys
import subprocess

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/",title="Select File",
                                            filetypes = (("executables","*.app"),("all files","*.*")))
    apps.append(filename)
    for app in apps:
        label = tk.Label(frame,text=app,fg = 'black')
        label.pack()


def runApps():
    for app in apps:
        if sys.platform == "win32":
            os.startfile(app)
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, app])
        

def quitApps():
    removeWords = ["/System/Applications/", "/Applications/", ".app"]

    for app in apps:
        for word in removeWords:
            app = app.replace(word,'')
    
    for app in apps:
        subprocess.call(['osascript', '-e', f'tell application "{app}" to quit'])



def deleteApps():
    for widget in frame.winfo_children():
        widget.destroy()
    with open('save.txt', 'r+') as f:
        f.truncate(0)
        f.write("Cleared")

        
    

canvas = tk.Canvas(root, height = 700, width = 700, bg = '#263D42')
canvas.pack()

frame = tk.Frame(root, bg = 'white')
frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

openFile = tk.Button(root, text="Open Files",padx=10,
                     pady=5, fg="black", command = addApp)
openFile.pack()

runApp = tk.Button(root, text="Run Apps",padx=10,
                     pady=5, fg="black", command = runApps)
runApp.pack()


quitApp = tk.Button(root, text="Quit Apps", padx=10,
                    pady=5, fg='black', command = quitApps)
quitApp.pack()

deleteAll = tk.Button(root, text="Delete All Apps", padx=10,
                       pady=5, fg='black', command = deleteApps)
deleteAll.pack()

for app in apps:
    label = tk.Label(frame, text = app)
    label.pack()

root.mainloop()

with open('save.txt', 'r+') as f:
    if 'Cleared' in f.read():
        print("True")
        f.truncate(0)
    elif '' in f.read():
        for app in apps:
            f.write(app + ',')



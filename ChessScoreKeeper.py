#Chess Score Keeper by github.com/yeehaoo 26.05.2019

import tkinter as tk

root = tk.Tk()

#define win count, total game count and initialise as 0
#initialise last action as 0 so that undoing a 0/0 score does nothing
winCnt = tk.DoubleVar()
totalCnt = tk.DoubleVar()
winCnt.set(0)
totalCnt.set(0)
lastAction = -1

#updates score when user clicks won, lost or drew
#increments no. of games by one, adds a point for win, 0.5 points for draw and 0 for loss
#keeps track of last action so user is able to undo in case of misclick
def updateScore(arg):
    winCnt.set(winCnt.get()+arg)
    totalCnt.set(totalCnt.get()+1)
    global lastAction
    lastAction = arg

#resets score to 0/0 and last action to -1
def reset():
    winCnt.set(0)
    totalCnt.set(0)
    global lastAction
    lastAction = -1

#if there was a previous action, decrement games by one and subtract points accordingly
def undo():
    if(lastAction != -1):
        winCnt.set(winCnt.get()-lastAction)
        totalCnt.set(totalCnt.get()-1)

#three frames from top to bottom: score, win/lose buttons and undo/reset buttons
topFrame = tk.Frame(root)
topFrame.pack()
southFrame = tk.Frame(root)
southFrame.pack(side=tk.BOTTOM)
bottomFrame = tk.Frame(root)
bottomFrame.pack(side=tk.BOTTOM)

#labels to display score
label1 = tk.Label(topFrame, text="Score: ")
lblWin = tk.Label(topFrame, textvariable=winCnt)
label2 = tk.Label(topFrame, text="/")
lblTotal = tk.Label(topFrame, textvariable=totalCnt)

#first row of buttons to update score
button1 = tk.Button(bottomFrame, text="Won", fg="green", command=lambda:updateScore(1))
button2 = tk.Button(bottomFrame, text="Lost", fg="red", command=lambda:updateScore(0))
button3 = tk.Button(bottomFrame, text="Drew", fg="yellow", command=lambda:updateScore(0.5))

#second row of buttons to reset or undo
btnUndo = tk.Button(southFrame, text="Undo", command=undo)
btnReset = tk.Button(southFrame, text="Reset", command=reset)

#pack
label1.pack(side=tk.LEFT)
lblWin.pack(side=tk.LEFT)
label2.pack(side=tk.LEFT)
lblTotal.pack(side=tk.LEFT)
button1.pack(side=tk.LEFT)
button2.pack(side=tk.LEFT)
button3.pack(side=tk.LEFT)
btnUndo.pack(side=tk.LEFT)
btnReset.pack(side=tk.LEFT)

root.mainloop()

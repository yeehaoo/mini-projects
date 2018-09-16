import tkinter as tk


class Root(tk.Tk):

    xp = 0
    lvl = 1
    xpDifference = 83
    nextLvlXP = 83
    logDictionaryXP = {"Normal" : 40, "Oak" : 60, "Willow" : 90, "Teak" : 105, "Maple" : 135, "Mahogany" : 157.5, "Yew" : 202.5, "Magic" : 303.8, "Redwood" : 350}
    logDictionaryLvl = {"Normal" : 1, "Oak" : 15, "Willow" : 30, "Teak" : 35, "Maple" : 45, "Mahogany" : 50, "Yew" : 60, "Magic" : 75, "Redwood" : 90}
    
    def __init__(self):
        super().__init__()

        self.title = "RS Firemaking Simulator"
        
        frame = tk.Frame(self)
        frame.pack()

        self.log = tk.StringVar(self)
        self.log.set("Normal")
        self.ddl_logs = tk.OptionMenu(frame, self.log, *self.logDictionaryXP.keys())
        self.ddl_logs.grid(row=3,columnspan=2)
        
        self.btnAction = tk.Button(frame, text="Light Log", command=self.action)
        self.btnAction.grid(row=0)

        self.btnQuit = tk.Button(frame, text="Log Off", command=self.destroy)
        self.btnQuit.grid(row=0,column=1)

        self.label_1 = tk.Label(frame, text="XP: ")
        self.label_1.grid(row=1)

        self.lblXP = tk.Label(frame, text=self.xp)
        self.lblXP.grid(row=1,column=1)

        self.label_2 = tk.Label(frame, text="Level: ")
        self.label_2.grid(row=2)

        self.lblLevel = tk.Label(frame, text=self.lvl)
        self.lblLevel.grid(row=2,column=1)

    def action(self):
        self.firemaking()

    def firemaking(self):
        if (self.lvl >= self.logDictionaryLvl.get(self.log.get())):
            self.xp += self.logDictionaryXP.get(self.log.get())
            self.lblXP.configure(text=self.xp)
        
            if (self.xp >= self.nextLvlXP):
                self.levelUp()
        else:
            print("Your level is too low to light this type of log.")
            
    def levelUp(self):
        self.lvl += 1
        #self.xpDifference = int(round(( self.lvl + 300 * 2 ** ( ( self.lvl ) / 7 ) ) / 4))
        self.xpDifference = ( self.lvl + 300 * 2 ** ( ( self.lvl ) / 7 ) ) / 4
        self.nextLvlXP += self.xpDifference
        
        self.lblLevel.configure(text=self.lvl)
        print("Congratulations, you just advanced a Firemaking level. \nYour Firemaking level is now " + str(self.lvl) + ".")
        print("Next level in " + str(round(self.xpDifference)) + " (" + str(round(self.nextLvlXP)) + ").")
        
if __name__ == "__main__":
    root = Root()
    root.mainloop()

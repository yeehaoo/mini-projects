import tkinter as tk


class Root(tk.Tk):

    def __init__(self):
        super().__init__()

        self.balance = 100
        
        self.frame = tk.Frame(self)
        self.frame.pack()
        
        self.label_1 = tk.Label(self.frame,text="Bank Account")
        self.label_1.pack()

        self.lblAmount = tk.Label(self.frame,text=self.balance)
        self.lblAmount.pack()
        
        self.entry = tk.Entry(self.frame)
        self.entry.pack()

        self.btnDeposit = tk.Button(self.frame,text="Deposit",command=self.deposit)
        self.btnDeposit.pack()

        self.btnWithdraw = tk.Button(self.frame,text="Withdraw",command=self.withdraw)
        self.btnWithdraw.pack()

    def deposit(self):
        amount = int(self.entry.get())
        self.balance += amount
        self.lblAmount.configure(text=self.balance)

    def withdraw(self):
        amount = int(self.entry.get())
        self.balance -= amount
        self.lblAmount.configure(text=self.balance)
        
if __name__ == "__main__":
    root = Root()
    root.mainloop()

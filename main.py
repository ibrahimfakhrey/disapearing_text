import tkinter as tk
import random
from tkinter import RAISED, END



class Application(tk.Frame): 

    def __init__(self,master):
        self.master = master
        tk.Frame.__init__(self)

        self.pack()
        var = tk.StringVar()
        msg = tk.Message(self, textvariable=var)
        var.set("Hello, Here if you stop writing you will find that the text disappears within 5 seconds ")
        msg.pack()
        self._after_id = None
        self.entry = tk.Entry(width=50)
        self.entry.place(x = 50,
                         y = 200,
                         height=200)

        # self.entry.pack()
        self.entry.bind('<Key>',self.handle_wait)

    def handle_wait(self,event):
        # cancel the old job
        if self._after_id is not None:
            self.after_cancel(self._after_id)

        # create a new job
        self._after_id = self.after(5000, self.clear_text)

    def clear_text(self):
        self.entry.delete(0, END)



root = tk.Tk()
root.geometry("600x650")
app = Application(root)
app.mainloop()
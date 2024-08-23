import tkinter as tk

class ClickCounterApp:
    def __init__(self, master):
        self.master = master
        master.title("Click Counter")

        self.count = 0
        self.label = tk.Label(master, text="Button clicked: 0 times")
        self.label.pack()

        self.button = tk.Button(master, text="Click me!", command=self.increment_count)
        self.button.pack()

    def increment_count(self):
        self.count += 1
        self.label.config(text=f"Button clicked: {self.count} times")

root = tk.Tk()
app = ClickCounterApp(root)
root.mainloop()
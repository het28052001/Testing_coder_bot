import tkinter as tk

class ClickCounterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Click Counter")
        self.count = 0
        
        self.label = tk.Label(master, text="Button clicks: 0")
        self.label.pack()
        
        self.button = tk.Button(master, text="Click me!", command=self.increment_count)
        self.button.pack()
        
    def increment_count(self):
        self.count += 1
        self.label.config(text=f"Button clicks: {self.count}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ClickCounterApp(root)
    root.mainloop()
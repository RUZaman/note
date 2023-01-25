import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.title("My Tkinter Program")
        self.geometry("600x400")

        # Create a menu bar
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)

        # Create a drop-down menu
        self.menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Menu", menu=self.menu)
        self.menu.add_command(label="Option 1")
        self.menu.add_command(label="Option 2")
        self.menu.add_command(label="Option 3")

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
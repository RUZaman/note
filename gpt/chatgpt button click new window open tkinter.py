#code work
import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.title("My Tkinter Program")
        self.geometry("800x600")

        # Create a button to open a new window
        self.button = tk.Button(self, text="Open Window", command=self.open_window)
        self.button.pack()

    def open_window(self):
        # Create a new window
        window = tk.Toplevel(self)
        window.title("New Window")
        window.geometry("400x300")

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
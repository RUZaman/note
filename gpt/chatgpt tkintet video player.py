import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
import vlc

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.title("My Tkinter Program")
        self.geometry("800x600")

        # Create a video player
        self.vlc_player = vlc.MediaPlayer()
        self.vlc_frame = tk.Frame(self)
        self.vlc_frame.pack(side=tk.TOP, expand=True)
        self.vlc_widget = tk.Frame(self.vlc_frame)
        self.vlc_widget.pack(side=tk.BOTTOM, expand=True)
        self.vlc_player.set_window(self.vlc_widget.winfo_id())

        # Create control buttons
        self.control_frame = tk.Frame(self)
        self.control_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.play_button = tk.Button(self.control_frame, text="Play", command=self.play_video)
        self.play_button.pack(side=tk.LEFT)
        self.pause_button = tk.Button(self.control_frame, text="Pause", command=self.pause_video)
        self.pause_button.pack(side=tk.LEFT)
        self.stop_button = tk.Button(self.control_frame, text="Stop", command=self.stop_video)
        self.stop_button.pack(side=tk.LEFT)

    def play_video(self):
        self.vlc_player.play()

    def pause_video(self):
        self.vlc_player.pause()

    def stop_video(self):
        self.vlc_player.stop()

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
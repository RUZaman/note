import tkinter as tk
import cv2

def show_video():
    ip_address = entry.get()
    # Connect to the CCTV camera's IP address and stream the video
    cap = cv2.VideoCapture(ip_address)
    while True:
        ret, frame = cap.read()
        cv2.imshow('CCTV Camera', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

window = tk.Tk()
window.title('CCTV Camera')

frame = tk.LabelFrame(window, text='CCTV Camera')
frame.pack()

label = tk.Label(frame, text='Enter the IP address of the CCTV camera:')
label.pack()

entry = tk.Entry(frame)
entry.pack()

button = tk.Button(frame, text='Show Video', command=show_video)
button.pack()

window.mainloop()
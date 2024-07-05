import tkinter as tk
from tkinter import *
import cv2
from PIL import Image, ImageTk
import os
import numpy as np
from main import process_video, frame_processor 


global last_frame1  # creating global variable
last_frame1 = np.zeros((480, 640, 3), dtype=np.uint8)
global cap1
cap1 = cv2.VideoCapture("./solidWhiteRight.mp4")

def show_vid():
    global last_frame1
    if not cap1.isOpened():
        print("Cannot open the video file: ./test_video.mp4")
        return
    flag1, frame1 = cap1.read()
    if not flag1:
        print("Cannot read the frame from video file: ./test_video.mp4")
        return
    frame1 = cv2.resize(frame1, (600, 500))
    
    # Process the frame to detect lane lines
    processed_frame = frame_processor(frame1)
    
    last_frame1 = processed_frame.copy()
    pic = cv2.cvtColor(last_frame1, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(pic)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_vid)

if __name__ == '__main__':
    root = tk.Tk()
    img = ImageTk.PhotoImage(Image.open("logo.jpg"))
    heading = Label(root, image=img, text="Lane-Line Detection")
    heading.pack()
    heading2 = Label(root, text="Lane-Line Detection", pady=20, font=('arial', 45, 'bold'))
    heading2.configure(foreground='#364156')
    heading2.pack()
    lmain = tk.Label(master=root)
    lmain2 = tk.Label(master=root)

    lmain.pack(side=LEFT)
    lmain2.pack(side=RIGHT)
    root.title("Lane-line detection")
    root.geometry("1250x900+100+10")

    exitbutton = Button(root, text='Quit', fg="red", command=root.destroy).pack(side=BOTTOM,)
    show_vid()
    root.mainloop()
    cap1.release()
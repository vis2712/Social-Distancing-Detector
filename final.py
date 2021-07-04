import tkinter as tk
from tkinter import filedialog, Text
import os
import subprocess
import ntpath


root = tk.Tk()


def addApps():
	

	filename = filedialog.askopenfilename(initialdir="/",title="Select mp4 File",filetypes=(("Videoes","*.mp4"),("all files","*.*")))
	apps = ntpath.basename(filename)
	x = "python social_distance_detector.py --input "+apps+" --output OUTPUT1.mp4"
	print(os.system(x))

	
	

canvas = tk.Canvas(root, height=500,width=500,bg="#263D42")
canvas.pack()


frame = tk.Frame(root, bg = "white")
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

label =  tk.Label(frame,font = "normal 15 bold",text="Welcome to")
label.pack()

label =  tk.Label(frame,font = "normal 15 bold",text="Social Distancing Detector")
label.pack(pady = 20)

label =  tk.Label(frame,font = "normal 10 bold",text="Select any mp4 video to start")
label.pack()

openFile = tk.Button(frame, text="Select Video",width=40,padx=50,pady=5,fg="white",bg="#263D42", command=addApps)
openFile.pack(pady = 10)

label =  tk.Label(root,font = "normal 15 bold",anchor='ne',padx=50,pady=5,text="by- Vishal Sindhi")
label.pack()




root.mainloop()
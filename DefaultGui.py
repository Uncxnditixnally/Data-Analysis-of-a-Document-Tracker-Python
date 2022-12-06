from tkinter import *
import sys
import os
from Task2 import *
from Task3 import *
from Task4 import *
from Task5 import *

class DefaultGui(object):
	
	def __init__(self, master,file,**kwargs):
		self.file = self.readJson(file)
		self.initUI(master)

	def initUI(self, master):
		self.master = master
		master.title("Industrial Pogramming")
		# The following lines size the gui in an almost full size application
		# pad=3
		# master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
		
		# Frames
		titleFrame = Frame(root, bg='white', padx=3, pady=3)
		buttonsFrame = Frame(root, bg='cyan', padx=3, pady=3)
		displayFrame = Frame(root, bg='red', padx=3, pady=3)

		# Configure root grid
		root.grid_rowconfigure(2, weight=1)
		root.grid_columnconfigure(0, weight=1)

		# Place the frames on the grid
		titleFrame.grid(row=0, sticky="n")
		buttonsFrame.grid(row=1, sticky="n")
		displayFrame.grid(row=2, sticky="news")

		# Title
		titlePage = Label(titleFrame, text="Data Analysis of Document Tracker",font=("Arial", 36), anchor=CENTER)
		titlePage.grid(row=0, column=2)
		docNameLabel = Label(titleFrame, text="Search Bar",font=("Arial"), anchor=CENTER)
		docNameLabel.grid(row=1, column=1)
		input=Entry(titleFrame, width=50)
		input.grid(row=1, column=2)

		# Buttons
		# First rows of buttons
		t2 = Task2(self.file)
		task2aButton = Button(buttonsFrame, text="Histogram of countries\nof the viewers (2a)", anchor=CENTER,command=lambda:t2.task2a(root,displayFrame, input.get()))
		task2aButton.grid(row=1,column=0, padx=30, pady=10)
		task2bButton = Button(buttonsFrame, text="Histogram of the continents\nof the viewers (2b)", anchor=CENTER,command=lambda:t2.task2b(root,displayFrame, input.get()))
		task2bButton.grid(row=1, column=1, padx=30, pady=10)
		t3 = Task3(self.file)
		task3aButton = Button(buttonsFrame, text="Histogram of all browser identifiers\nof the viewers (3a)", anchor=CENTER, command=lambda:t3.task3a(root,displayFrame))
		task3aButton.grid(row=1,column=2, padx=30, pady=10)
		task3bButton = Button(buttonsFrame, text="Histogram of main browsers name identifiers\nof the viewers (3b)", anchor=CENTER, command=lambda:t3.task3b(root,displayFrame))
		task3bButton.grid(row=1, column=3, padx=30, pady=10)
		t4 = Task4(self.file)
		task4Button = Button(buttonsFrame, text="Top 10 readers (4)", anchor=CENTER, command=lambda:t4.task4(root,displayFrame))
		task4Button.grid(row=1, column=4, padx=30, pady=10)
		# Second row of buttons
		t5 = Task5(self.file)
		task5aButton = Button(buttonsFrame, text="List of all readers UUID (5a)", anchor=CENTER,command=lambda:t5.task5a(root,displayFrame, input.get()))
		task5aButton.grid(row=2,column=0, padx=30, pady=10)
		task5bButton = Button(buttonsFrame, text="List of all document UUIDs that\nhave been read by this visitor (5b)", anchor=CENTER, command=lambda:t5.task5b(root,displayFrame, input.get()))
		task5bButton.grid(row=2, column=1, padx=30, pady=10)
		task5cButton = Button(buttonsFrame, text="List of “liked” documents (5c)", anchor=CENTER, command=lambda:t5.task5c(root,displayFrame, input.get()))
		task5cButton.grid(row=2,column=2, padx=30, pady=10)
		task5dButton = Button(buttonsFrame, text="List of top 10 document UUIDs (5d)", anchor=CENTER, command=lambda:t5.task5d(root,displayFrame, input.get()))
		task5dButton.grid(row=2, column=3, padx=30, pady=10)
		task6Button = Button(buttonsFrame, text="“Also likes” graph (6)", anchor=CENTER)
		task6Button.grid(row=2, column=4, padx=30, pady=10)

		# Configure displayFrame grid
		displayFrame.grid_rowconfigure(0, weight=1)
		displayFrame.grid_columnconfigure(1, weight=1)

		# Display
		display = Frame(displayFrame, bg='red', width=250, height=190, padx=3, pady=3)
		display.grid(row=0, column=1, sticky="nsew")
	
	def readJson(self,file):
		f = open(file)
		data = []
		lines = f.readlines()
		for line in lines:
			data.append(line)
		f.close() 
		return data

if __name__ == "__main__":
	root = Tk()
	root.state('zoomed') #fullscreen on Windows
	#root.attributes('-zoomed', True) #fullscreen on Linux
	app = DefaultGui(root,"sample_100k_lines.json")
	root.mainloop()
import tkinter as tk
from tkinter import *
import json
import operator
from prettytable import PrettyTable

class Task4:
	def __init__(self, data):
		self.data = data

	def getAllReadTime(self):
		timeRead = {}
		assert isinstance(self.data,list)
		for line in self.data:
			tmp = json.loads(line)
			if(tmp["event_type"] == "pagereadtime"):
				visitorNum = tmp["visitor_uuid"]
				if visitorNum in timeRead: # the key already exists
					timeRead[visitorNum] = timeRead[visitorNum] + tmp["event_readtime"]
				else:
					timeRead[visitorNum] = tmp["event_readtime"]
		return timeRead
	
	def createDictionnary(self,resultList):
		result={}
		key = resultList.keys()
		values = resultList.values()
		result={"visitor":key,"time":values}
		return result

	def task4(self, root, displayFrame):
		# Configure displayFrame grid
		displayFrame.grid_rowconfigure(0, weight=1)
		displayFrame.grid_columnconfigure(1, weight=1)

		readersTime = self.getAllReadTime()
		sortedTime = dict(sorted(readersTime.items(), key=operator.itemgetter(1), reverse=True))
		res = "Top 10 readers: \n"
		t = PrettyTable(['          visitor_uuid               ', '     event_readtime     '])
		for i in range(0,10):
			t.add_row([list(sortedTime.keys())[i], list(sortedTime.values())[i]])


		txt = Label(displayFrame, text=t,font=("Arial"), anchor=CENTER)
		txt.grid(row=0, column=1, sticky="news")

	
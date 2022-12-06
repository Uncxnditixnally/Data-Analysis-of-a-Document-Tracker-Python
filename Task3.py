import tkinter as tk
from tkinter import Frame
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import Counter

from user_agents import parse

import json
import re

class Task3:
	def __init__(self, data):
		self.data = data
		self.browsersList = self.allBrowsers()

	def allBrowsers(self):
		assert isinstance(self.data,list)
		listBrowser = []
		for line in self.data:
			data = json.loads(line)
			listBrowser.append(data["visitor_useragent"])
		return listBrowser

	def countOccurence(self, data):
		return Counter(data)

	def formatResult(self,resultList):
		result={}
		key = resultList.keys()
		values = resultList.values()
		result={"browser":key,"count":values}
		return result

	def task3a(self, root, displayFrame):
		# Configure displayFrame grid
		displayFrame.grid_rowconfigure(0, weight=1)
		displayFrame.grid_columnconfigure(1, weight=1)

		originalData = self.countOccurence(self.browsersList)
		data = self.formatResult(originalData)

		# plotting
		df = pd.DataFrame(data)
		figure = plt.Figure(figsize=(6, 5), dpi=100)
		ax= figure.add_subplot(111)
		bar = FigureCanvasTkAgg(figure, displayFrame)
		bar.get_tk_widget().grid(row=0, column=1, sticky="nsew")
		df = df[['browser', 'count']].groupby('browser').sum()
		df.plot(kind='bar', legend=True, ax=ax)
		ax.set_title('Browsers in term of count')

	def allBrowserName(self, data):
		browserName = []
		for browser in data:
			user_agent = parse(browser)
			browserName.append(user_agent.browser.family)
		return browserName
	
	def task3b(self, root, displayFrame):
		# Configure displayFrame grid
		displayFrame.grid_rowconfigure(0, weight=1)
		displayFrame.grid_columnconfigure(1, weight=1)

		originalData = self.countOccurence(self.allBrowserName(self.browsersList))

		# plotting
		data = self.formatResult(originalData)
		df = pd.DataFrame(data)
		figure = plt.Figure(figsize=(6, 5), dpi=100)
		ax= figure.add_subplot(111)
		bar = FigureCanvasTkAgg(figure, displayFrame)
		bar.get_tk_widget().grid(row=0, column=1, sticky="nsew")
		df = df[['browser', 'count']].groupby('browser').sum()
		df.plot(kind='bar', legend=True, ax=ax)
		ax.set_title('Browsers in term of count')
		return
	
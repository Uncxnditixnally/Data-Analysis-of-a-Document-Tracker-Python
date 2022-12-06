import json
import pandas as pd
import tkinter as tk
from tkinter import Frame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import Counter
import pycountry_convert as pc

class Task2:
	listCountries = []
	CountryCount = {}
	def __init__(self, data):
		self.data = data
		pass

	def getAllCountries(self, nameDoc):
		assert isinstance(self.data,list)
		for line in self.data:
			tmp = json.loads(line)
			if "subject_doc_id" in tmp:
				if(tmp["subject_doc_id"] == nameDoc):
					self.listCountries.append(tmp["visitor_country"])

	def countOccurence(self, data):
		return Counter(data)

	def createDictionnary(self,resultList):
		result={}
		key = resultList.keys()
		values = resultList.values()
		result={"name":key,"count":values}
		return result

	def getAllContinent(self):
		result = []
		for country in self.listCountries:
			try:
				country_continent_code = pc.country_alpha2_to_continent_code(country)
				country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
				result.append(country_continent_name)
			except KeyError:
				result.append("Unknown")
		return result

	def task2a(self, root, displayFrame, docName):
		# Configure displayFrame grid
		displayFrame.grid_rowconfigure(0, weight=1)
		displayFrame.grid_columnconfigure(1, weight=1)

		self.listCountries.clear()
		self.getAllCountries(docName)
		countCountries = self.countOccurence(self.listCountries)
		final = self.createDictionnary(countCountries)

		# plotting
		df = pd.DataFrame(final)
		figure = plt.Figure(figsize=(6, 5), dpi=100)
		ax = figure.add_subplot(111)
		bar = FigureCanvasTkAgg(figure, displayFrame)
		bar.get_tk_widget().grid(row=0, column=1, sticky="nsew")
		df = df[['name', 'count']].groupby('name').sum()
		df.plot(kind='bar', legend=True, ax=ax)
		ax.set_title('Viewers country of the document')

	def task2b(self, root, displayFrame, docName):
		# Configure displayFrame grid
		displayFrame.grid_rowconfigure(0, weight=1)
		displayFrame.grid_columnconfigure(1, weight=1)

		self.listCountries.clear()
		self.getAllCountries(docName)
		continent = self.getAllContinent()
		continentCount = self.countOccurence(continent)
		final = self.createDictionnary(continentCount)

		# plotting
		df = pd.DataFrame(final)
		figure = plt.Figure(figsize=(6, 5), dpi=100)
		ax = figure.add_subplot(111)
		bar = FigureCanvasTkAgg(figure, displayFrame)
		bar.get_tk_widget().grid(row=0, column=1, sticky="nsew")
		df = df[['name', 'count']].groupby('name').sum()
		df.plot(kind='bar', legend=True, ax=ax)
		ax.set_title('Viewers continent of the document')

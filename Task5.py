import tkinter as tk
from tkinter import *
import json
import operator

class Task5:
	readers = []
	documents = []
	docNameToFind = ""
	docReader= {}
	allDoc = []
	AlsoLike = []

	def __init__(self, data):
		self.data = data

	def getAllVisitors(self, docName):
		self.docNameToFind = docName
		self.readers.clear()
		assert isinstance(self.data,list)
		for line in self.data:
			tmp = json.loads(line)
			if "subject_doc_id" in tmp:
				if(tmp["subject_doc_id"] == docName and not tmp["visitor_uuid"] in self.readers):
					self.readers.append(tmp["visitor_uuid"])

	def getallDocuments(self, visitorNum):
		self.documents.clear()
		assert isinstance(self.data,list)
		for line in self.data:
			tmp = json.loads(line)
			if "subject_doc_id" in tmp:
				if(tmp["visitor_uuid"] == visitorNum and not tmp["subject_doc_id"] in self.documents):
					self.documents.append(tmp["subject_doc_id"])

	def task5a(self, root, displayFrame, docName):
		# Configure displayFrame grid
		displayFrame.grid_rowconfigure(0, weight=1)
		displayFrame.grid_columnconfigure(1, weight=1)

		self.docNameToFind = docName
		self.getAllVisitors(docName)

		t = "All visitors_uuid of the document \n\n"
		for visitor in self.readers:
			t += visitor + "\n"

		txt = Label(displayFrame, text=t,font=("Arial"), anchor=CENTER)
		txt.grid(row=0, column=1, sticky="news")

	def task5b(self, root, displayFrame, visitorNum):
		displayFrame.grid_rowconfigure(0, weight=1)
		displayFrame.grid_columnconfigure(1, weight=1)

		self.getallDocuments(visitorNum)
		t = "All documents consulted by the visitor \n\n"
		for document in self.documents:
			t += document + "\n"

		txt = Label(displayFrame, text=t,font=("Arial"), anchor=CENTER)
		txt.grid(row=0, column=1, sticky="news")

	def getAllDocReader(self):
		for visitor in self.readers:
			self.getallDocuments(visitor)
			if not set(self.documents).issubset(self.AlsoLike):
				self.AlsoLike = self.AlsoLike + self.documents
				self.docReader[visitor] = self.documents

	def task5c(self, root, displayFrame, docName):
		displayFrame.grid_rowconfigure(0, weight=1)
		displayFrame.grid_columnconfigure(1, weight=1)

		if(docName != ""):
			self.docNameToFind = docName
		
		self.getAllVisitors(self.docNameToFind)
		self.getAllDocReader()
		
		t = "Also liked documents \n\n"
		for document in self.AlsoLike:
			t += str(document) + "\n"

		txt = Label(displayFrame, text=t,font=("Arial"), anchor=CENTER)
		txt.grid(row=0, column=1, sticky="news")

	def task5d(self, root, displayFrame, docName):
		if(docName != ""):
			self.docNameToFind = docName
		
		self.getAllVisitors(self.docNameToFind)
		self.getAllDocReader()

		counterDoc = {}
		for doc in self.AlsoLike:
			occurence = operator.countOf(self.allDoc, doc)
			counterDoc[doc] = occurence

		sortedDoc = dict(sorted(counterDoc.items(), key=operator.itemgetter(1), reverse=True))
		tmp = list(sortedDoc.keys())
		t = "Top 10 documents \n\n"
		for i in range(0,len(tmp)):
			if(i == 10):
				break
			t += tmp[i] + "\n"

		txt = Label(displayFrame, text=t,font=("Arial"), anchor=CENTER)
		txt.grid(row=0, column=1, sticky="news")
		
		



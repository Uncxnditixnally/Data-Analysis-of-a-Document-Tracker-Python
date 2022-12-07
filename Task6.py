from graphviz import *

from Task5 import *
import sys
sys.path.append("graphviz-0.10.1")

from graphviz import *

class Task6:
	def __init__(self, data):
		self.data = data
		self.t5 = Task5(data)
		self.dot = Digraph(comment='The Round Table')

	def initNode(self):
		for visitor in self.t5.docReader.keys():
			self.dot.node('A', 'King Arthur', shape=box)

	def task6(self, root, displayFrame, docName):
		self.t5.getAllVisitors(docName)
		# self.t5.getallDocuments()
		self.t5.getAllDocReader()

		print(self.t5.docReader)

		dot = Digraph(name='The graph')
		dot.node('Readers', shape='none')
		dot.node('Documents', shape='none')
		dot.edge('Readers', 'Documents', label=('Size: %s' % size))

		try:
			for visitor in self.t5.docReader:
				if visitor == visitorID:
					dot.node(str(visitor)[-4:], fillcolor='green', style='filled', shape='box')
				else:
					dot.node(str(visitor)[-4:], shape='box')
				for document in data[visitor]:
					if document == docID:
						dot.node(str(document)[-4:], fillcolor='green', style='filled')
					else:
						dot.node(str(document)[-4:])
					dot.edge(str(visitor)[-4:], str(document)[-4:])
		except TypeError:
			print('Incorrect type passed to drawAlsoLikesGraph')
		except:
			print('Unexpected error when trying to create also likes graph')

		try:
			dot.render(self.savename, view=True)
		except:
			print('Cannot save graph to file with filename \'%s\'. Check if the file is open or locked' % self.savename)


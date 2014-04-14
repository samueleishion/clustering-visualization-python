'''
	clustering_visualization.py 
		@author: Samuel Acuna
		@date: 04-02-14

	This program generates a visualization of the clustering algorithm 
	presented in Jason Baldridge LIN 313 class, SPRING 2013 at the 
	University of Texas at Austin. 

'''
from graphics import * 
from math import sqrt 
from random import randint 

X = 500 
Y = 500 

COLORS = [ color_rgb(255,0,0), 
			color_rgb(0,255,0), 
			color_rgb(0,0,255), 
			color_rgb(255,255,0), 
			color_rgb(255,0,255), 
			color_rgb(0,255,255), 
			color_rgb(100,0,0), 
			color_rgb(0,100,0), 
			color_rgb(0,0,100), 
			color_rgb(100,100,0), 
			color_rgb(100,0,100), 
			color_rgb(0,100,100) ]

def avg(nums): 
	if(len(nums)==0):
		return 0 

	s = 0
	for i in nums: 
		s += i 
	return s/len(nums) 

class Document:
	def __init__(self,id_num): 
		self.x = randint(0,X) 
		self.y = randint(0,Y) 
		self.id = id_num 
		self.color = color_rgb(0,0,0)


	def draw(self,win): 
		self.p = Circle(Point(X-self.x,Y-self.y),3) 
		self.p.setFill(self.color)
		self.p.setOutline(color_rgb(255,255,255)) 
		self.p.draw(win) 

class Category:
	def __init__(self,id_num): 
		self.x = randint(0,X) 
		self.y = randint(0,Y) 
		self.id = id_num 
		self.distances = {} 
		self.attributions = [] 
		self.color = COLORS[self.id % len(COLORS)] 

	def draw(self,win): 
		self.p = Circle(Point(X-self.x,Y-self.y),7) 
		self.p.setFill(self.color)
		self.p.setOutline(color_rgb(0,0,0)) 
		self.p.draw(win) 

	def move(self,win): 
		o = self.p.getCenter() 
		q = Point(X-self.x,Y-self.y) 
		line = Line(o,q) 
		line.draw(win) 
		self.draw(win) 


	def dist(self,doc): 
		d = sqrt((doc.x-self.x)**2 + (doc.y-self.y)**2) 
		self.distances[doc.id] = d 

	def attribute(self,doc): 
		self.attributions.append(doc) 

	def repos(self,win): 
		px = 0
		py = 0 
		for d in self.attributions: 
			px += d.x 
			py += d.y 
			d.color = self.color 
			d.draw(win) 

		if len(self.attributions)==0:
			self.x = 0
			self.y = 0 
		else: 
			self.x = round(px/len(self.attributions),2) 
			self.y = round(py/len(self.attributions),2) 
		self.move(win) 




def main(args): 
	win = GraphWin("test",X,Y) 
	try:
		docs = [None for x in range(int(args[1]))] 
		cats = [None for x in range(int(args[2]))] 
	except IndexError: 
		args = [args[0],50,2] 
		docs = [None for x in range(int(args[1]))] 
		cats = [None for x in range(int(args[2]))] 

	# create documents and centroids (categories) 
	for i in range(len(docs)): 
		docs[i] = Document(i) 
		docs[i].draw(win) 

	for i in range(len(cats)): 
		cats[i] = Category(i) 
		cats[i].draw(win) 

	
	for i in range(4): 
		# calculate respective categorization 
		for c in cats: 
			c.distances = {} 
			c.attributions = [] 
			for d in docs: 
				c.dist(d) 

		# attribute documents to categories 
		for d in docs: 
			nominated = [None]
			value = sys.maxint
			for c in cats: 
				if d.id in c.distances: 
					if c.distances[d.id] < value:
						value = c.distances[d.id] 
						nominated[0] = c 
				for k in cats: 
					if d in k.attributions:
						k.attributions.remove(d) 
				nominated[0].attribute(d) 

		# reposition and recolor categories 
		for c in cats: 
			c.repos(win) 

	print "DONE" 

	win.getMouse() 
	win.close() 

main(sys.argv) 
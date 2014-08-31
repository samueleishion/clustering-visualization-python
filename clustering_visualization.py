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

COLORS = [ color_rgb(227,74,51), 
		   color_rgb(166,189,219),
		   color_rgb(253,187,132),
		   color_rgb(44,127,184),
		   color_rgb(127,205,187),
		   color_rgb(117,107,177), 
		   color_rgb(28,144,153) ]

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
		self.p = Circle(Point(self.x,Y-self.y),3) 
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
		self.p = Circle(Point(self.x,Y-self.y),7) 
		self.p.setFill(self.color)
		self.p.setOutline(color_rgb(0,0,0)) 
		self.p.draw(win) 

	def move(self,win): 
		o = self.p.getCenter() 
		q = Point(self.x,Y-self.y) 
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
	protocol = args[1] 

	if(protocol=="random"):

		f = open('data.txt','w') 

		f.write(str(randint(2, 7))+"\n") 

		ranges = [58,49,34,25,49] 
		# xbounds = [[25,240],[100,380],[200,420],[350,500],[70,440]]
		# ybounds = [[90,499],[380,420],[200,400],[130,240],[20,189]] 
		xbounds = [[25,140],[200,280],[300,320],[450,500],[40,440]]
		ybounds = [[40,499],[380,420],[200,300],[130,240],[20,109]] 

		for i in range(len(ranges)): 
			for j in range(0,ranges[i]): 
				x = randint(xbounds[i][0],xbounds[i][1]) 
				y = randint(ybounds[i][0],ybounds[i][1]) 
				f.write(str(x)+","+str(y)+"\n") 


		f.close() 

		return 

	if(protocol=="file"):
		# file
		try: 
			print args[2] 
			f = open(args[2],'r') 
			i = -1
			
			# create documents and centroids (categories) 
			for line in f: 
				line = line.rstrip() 
				if(i==-1): 
					cats = [None for x in range(int(line))] 
					docs = [] 
				else: 
					s = line.split(',') 
					docs.append(Document(i)) 
					docs[i].x = int(s[0]) 
					docs[i].y = int(s[1]) 
					docs[i].draw(win) 
				i += 1 
			f.close() 

		except Exception as e: 
			print "there was an error" 
			print e.args 
	else: 
		# demo 
		try:
			docs = [None for x in range(int(args[2]))] 
			cats = [None for x in range(int(args[3]))] 
		except IndexError: 
			args = [args[0],50,2] 
			docs = [None for x in range(int(args[2]))] 
			cats = [None for x in range(int(args[3]))] 

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
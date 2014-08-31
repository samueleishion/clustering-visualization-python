DOCS = 100
CATS = 2 
FILE = null 

random: clustering_visualization.py 
	python clustering_visualization.py random

demo: clustering_visualization.py 
	python clustering_visualization.py demo $(DOCS) $(CATS) 

file: clustering_visualization.py 
	python clustering_visualization.py file $(FILE) 

clean: 
	rm *.pyc *~ 
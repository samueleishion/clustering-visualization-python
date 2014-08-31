DOCS = 100
CATS = 2 
FILE = null 

demo: clustering_visualization.py 
	python clustering_visualization.py demo $(DOCS) $(CATS) 

file: clustering_visualization.py 
	python clustering_visualization.py file $(FILE) 

random: clustering_visualization.py 
	python clustering_visualization.py random

clean: 
	rm *.pyc *~ .DS_Store 
DOCS = 100
CATS = 2 

cluster: clustering_visualization.py 
	python clustering_visualization.py $(DOCS) $(CATS) 

clean: 
	rm *.pyc *~ 
Clustering Visualization (Python)
=================================

This program generates a visualization of the clustering algorithm presented in Jason Baldridge LIN 313 class, SPRING 2013 at the University of Texas at Austin. 

## How to use
It's easy to run and all packages are included. You just need to have python 2.* running on your computer. 

#### Quick demo 
```
make
```
Runs a quick demo. You can just type this on your terminal (once you've navigated to the directory with these files). 

By default, the program will load 100 randomly placed documents and 2 randomly placed centroids (categories). 

#### Customize it 
```
make DOCS=200 CATS=3 
```
You can specify how many documents and categories (or centroids) to visualize. For example, this will test for 200 documents and 3 categories. 

#### About making 
```
make cluster 
make cluster DOCS=400 CATS=7
``` 
These commands will specifically call for the cluster python program. 

```
make clean 
``` 
This command will delete unnecessary files and clean your directory. 

## That's it
Now you can visualize the clustering process with Python! 
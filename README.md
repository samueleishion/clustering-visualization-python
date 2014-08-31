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
make demo DOCS=200 CATS=3 
```
You can specify how many documents and categories (or centroids) to visualize. For example, this will test for 200 documents and 3 categories. 
``` 
make file FILE=data.txt 
``` 
You can also specify a file with data for visualization. The file structure is as follows: 

```
4
123,234
345,123
...
```
The first line determines the number of categories, or centroids. after that, the program will look for coordinates points with domain and range of [0,500] separated with a comma and no spaces. 

We provide 4 example files: data1.txt, data2.txt, data3.txt, and data4.txt.

#### About making 
```
make demo 
make demo DOCS=400 CATS=7
make file FILE=data.txt
make random
``` 
These commands will specifically call for the cluster python program. 

`make random` will create a randomly generated data.txt file. 

```
make clean 
``` 
This command will delete unnecessary files and clean your directory. 

## That's it
Now you can visualize the clustering process with Python! 
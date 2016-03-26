Provided a list of genus and species names (in csv format), TimeTree.py creates an nxn matrix for n taxa of divergence times using TimeTree.org. I wrote it for my advisor last summer when I was asked to look up the divergence times of over 35 pairs of species. I have a general policy regarding anything that has to be done more than 20 times - it warrants the writing of a script. 



How to run

To Run TimeTree.py, type into the command line

```$python TimeTree.py list.csv```

list.csv is a file of the genus and species names, each separated by a tab.
The delimiter is hardcoded but can be changed (for example, ',' or ' ').

The result is a textfile (timeTree.txt) that contains a matrix of each if the pairwise divergence times

comments:
Those times that were not available in TimeTree.org appear as a -1 in the matrix.
This takes a while to run because it gets the same divergence time twice. 
It should be fixed to only calculate the top half. To use, compile and run as a .pyc.

Note: Should use beatuifulSoup instead of RE like my other programs. Will update soon.
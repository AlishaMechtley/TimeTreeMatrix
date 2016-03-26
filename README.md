TimeTree.py creates an nxn matrix for n taxa of divergence times using TimeTree.org.

To Run TimeTree.py, type into the command line
$python TimeTree.py list.csv

list.csv is a file of the genus and species names, each separated by a tab.
The delimiter is hardcoded but can be changed (for example, ',' or ' ').

The result is a textfile (timeTree.txt) that contains a matrix of each if the pairwise divergence times

comments:
Those times that were not available in TimeTree.org appear as a -1 in the matrix.
This takes a while to run because it gets the same divergence time twice. 
It should be fixed to only calculate the top half. To use, compile and run as a .pyc.
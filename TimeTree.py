#!/usr/bin/python
# Alisha Rossi
# 3/1/13
# Creates an nxn matrix for n taxa
# of divergence times
# using TimeTree.org

import csv
import httplib
import numpy as np
import re
import sys

#######################################
#read in file
#######################################
try:
	filename = sys.argv[1]
except:
	print "please specify a filename"


#######################################
#Assign Variables
#######################################
_server = 'timetree.org'
conn = httplib.HTTPConnection(_server, 80) # Setup HTTP session with the server
divergenceArray=[]
arrayLength=0

#######################################
#Functions
#######################################

class HTTPResponseError(Exception):
    def __init__(self, response):
        self.message = 'Bad response from server\n{} {}'.format(
            response.status, response.reason)


def getDivergenceTime(Genus1, species1, Genus2, species2): #Note: can not have spaces in names
	url='/index.php?taxon_a=' + Genus1 + '+' + species1 + '&taxon_b=' + Genus2 + '+' +  species2 + '&submit=Search'
	
	## Do http request for epost util
	conn.request('GET', url)
	response = conn.getresponse()

	if response.status != httplib.OK:
            raise HTTPResponseError(response)

	rData = response.read()
	
	pattern='class="panel year block"[^<]+<h1[^>]+>([0-9\.]+)<' 
	# + indicates one or more of stuff in the brackets, ^ means not, 
	# () for subpattern to extract
	# NOTE: THIS PATTERN MAY HAVE CHANGED IN THE LAST COUPLE YEARS. 
	# SHOULD SWITCH TO BEAUTIFULSOUP
	match = re.search(pattern, rData) 
	if match != None:
		return match.group(1) # zero is whole match, group 1 is the subpattern
	#raise ValueError('Found no match') #This will work in a try block. Currently puts a -1 in cells that failed
	print url
	print str(Genus1) + ' ' + str(species1) + ' vs ' + str(Genus2) + ' ' + str(species2)  + ' failed'
	return -1
	

#######################################
# Main method
# prints array of divergence times 
# to file and to terminal
#######################################

if __name__ == '__main__':
	with open(filename, 'rb') as csvfile:
		reader1 = csv.reader(csvfile, delimiter='\t')
		for firstSpecies in reader1:
			Genus1=firstSpecies[0]
			species1=firstSpecies[1]
			arrayLength+=1
			print 'Calculating divergence times for ' + str(Genus1) + ' ' + (species1)
			with open(filename, 'rb') as csvfile:
				reader2 = csv.reader(csvfile, delimiter='\t')
				for secondSpecies in reader2: #Get all other species
					Genus2=secondSpecies[0]
					species2=secondSpecies[1]
					if Genus2==Genus1 and species2==species1: #same species
						divTime=0
					else:
						divTime=getDivergenceTime(Genus1, species1, Genus2, species2)
					divergenceArray+=[divTime]
					#print str(Genus1) + str(species1) + 'vs' + str(Genus2) + str(species2)
				
	divergenceArray=np.array(divergenceArray)	
	d=divergenceArray.reshape(arrayLength,arrayLength)
	print d
	d=d.astype(np.float)
	np.savetxt('timeTree.txt', d, fmt='%-7.1f') #save in file with 1 decimal place
	
			
	
	
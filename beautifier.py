# Beautifier QA Engine
# This uses googles YAPF module to parse python files and reformat them 
# No backups are kept of the files since you can go back in Git and retrieve them.
#
#

import os
import sys
import string
import yapf #yapf library

from yapf.yapflib.yapf_api import FormatFile  # reformat a file

globalFileList = [] #a global file list


directoryList = ['SoftwareEngineering', 'QualityAssurance', 'MachineLearning', 'Visualization']

#NOTE ADD CONSTRAINT ON INPUT OF MAIN FUNCTION 

def main(passedRootFolder):
	print "This will beautify python files using googles YAPF"
	mainFolder = "../"
	
	if passedRootFolder:
		mainFolder = passedRootFolder
		print "parsing in" + mainFolder
	
	os.chdir(mainFolder) #going to main folder here
	
	for x in directoryList:
		print mainFolder + x
		#~ FormatFile("foo.py", in_place=True)
	
	
	return 0

if __name__ == "__main__": main(sys.argv[1])
